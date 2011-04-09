

import os, sys

from ctypes import *

# mkdir libvpx/x86_build ; cd libvpx/x86_build ; ../configure --target=x86_64-linux-gcc --enable-shared

#_vpx = cdll.LoadLibrary('/xtra/libvpx/x86_build/libvpx.so.0.9.6')



import numpy as np


from mapsaw.rasterio import Nimage
from mapsaw.grid import Grid

from vpxwrap import *



'''
ys = np.zeros((ny,nx), np.uint8)
hnx = (nx + 1)//2
hny = (ny + 1)//2
us = np.zeros((hny,hnx), np.uint8)
vs = np.zeros((hny,hnx), np.uint8)
'''


import operator


buf_from_ptr = pythonapi.PyBuffer_FromReadWriteMemory
buf_from_ptr.restype = py_object


def array_from_ptr(ptr, shape):
    # ptr is a ctypes.LP_c_ubyte

    size = reduce(operator.mul, shape)

    # get a wrapper to an internal python func
    buf = buf_from_ptr(ptr, size)
    a = np.frombuffer(buf, np.uint8)

    return a.reshape(shape)


def imgplanes(raw, nplanes):
    """

    note that the returned arrays have unchecked ctypes
    pointers.  the vpx_image pointed to by raw must
    not be freed until the numpy arrays have been freed.
    """
    raw = raw.contents

    nx = raw.w
    ny = raw.h
    hnx = (nx + 1)//2
    hny = (ny + 1)//2

    # assume I420 yuv
    # what would dimension of alpha be?
    planes = []

    for planei in range(nplanes):
        cstride = raw.stride[planei]
        cplane = raw.planes[planei]

        #print 'RAW', raw, cstride, cplane, nx, ny

        pnx = nx if planei==0 else hnx
        pny = ny if planei==0 else hny

        # stride rather than pnx determines memory layout
        a = array_from_ptr(cplane, (pny, cstride))

        # screen off any extra data indices afterward
        if cstride > pnx:
            a = a[:,:pnx]
        planes.append(a)

    return planes

def checkvpxres(res, s):
    """check the result of a vpx_codec_* function and throw an exception if not ok"""
    if not res: return
    raise Exception("%s: %s" % (s,vpx_codec_err_to_string(res)))


class VpxEncodeStream(object):
    """encode a series of frames to a VP8 stream"""

    def __init__(self, shape):
        self.shape = shape

        self.interface = vpx_codec_vp8_cx()
        print 'codec',vpx_codec_iface_name(self.interface)

        self.vpxconfig()
    
        self.codec = vpx_codec_ctx_t()
    
        checkvpxres(vpx_codec_enc_init(self.codec, self.interface, self.cfg, 0),
                    'vpx_codec_enc_init')

        # frame buffer vpx_img
        self.frame = None

        # frame buffer as numpy arrays
        self.planes = None

        self.outfp = None
        self.decoder = None

        self.framei = 0
        writing = 1
        raw = None

    def encpng(self, filename):

        nim = Nimage.load(filename)
        if len(nim.data.shape) == 3:
            ys = nim.data[:,:,3]
        else:
            ys = nim.data
        assert ys.shape == self.shape

        self.hshape = [(n+1)//2 for n in self.shape]
        us = 0 * np.ones(self.hshape, np.uint8)
        vs = 0 * np.ones(self.hshape, np.uint8)

        self.encframe((ys,us,vs))
        self.drain()
        self.framei += 1


    def encgrey(self):
        """test: a solid gray frame"""
        self.hshape = [(n+1)//2 for n in self.shape]
        
        ys = 127 * np.ones(self.shape, np.uint8)
        us = 0 * np.ones(self.hshape, np.uint8)
        vs = 0 * np.ones(self.hshape, np.uint8)

        self.encframe((ys,us,vs))
        self.drain()

        self.framei += 1


    def drain(self):
        """process output from the encoder
        """
        for pkt in self.iterpackets():
            fr = pkt.data.frame

            print pkt.kind,

            if pkt.kind == VPX_CODEC_CX_FRAME_PKT:
                #write_frame_header(pkt)
                #write_ivf_frame_header(outfile, pkt)

                if self.decoder:
                    bufptr = cast(fr.buf, POINTER(c_ubyte))
                    #print 'FB',bufptr,'X',fr.sz
                    self.decoder.decode(bufptr, fr.sz)

                if self.outfp:
                    buf = buf_from_ptr(fr.buf, fr.sz)
                    #print 'blen',len(buf), fr.sz
                    self.outfp.write(buf)
                print ('K' if fr.flags & VPX_FRAME_IS_KEY
                       else ' '),
            else:
                pass
            print fr.sz


    def vpxconfig(self):
        cfg = vpx_codec_enc_cfg()
    
        res = vpx_codec_enc_config_default(self.interface, cfg, 0)
        checkvpxres(res, 'vpx_codec_enc_config_default')
    
        # start with the default target bitrate, and scale it
        # to however many pixels we're using
        ny,nx = self.shape
        scale = nx * ny / cfg.g_w / cfg.g_h
        cfg.rc_target_bitrate *= scale
        cfg.g_w = nx
        cfg.g_h = ny
    
        self.cfg = cfg

    
    def encframe(self, ysusvs):
        """send an uncompressed frame to the encoder
        """

        if not self.frame:
            ny,nx = self.shape
            self.frame = vpx_img_alloc(None, VPX_IMG_FMT_I420, nx, ny, 1)

            # get a numpy wrapper around the image plane objects
            self.planes = imgplanes(self.frame, 3)

    
            #print 'PL', planes[0].shape, planes[1].shape, planes[2].shape

        # write into the image
        for buf,src in zip(self.planes, ysusvs):
            buf[:,:] = src

        #print 'ENC'

        flags = 0

        res = vpx_codec_encode(self.codec, self.frame, self.framei,
                             1, flags, VPX_DL_GOOD_QUALITY)
        assert not res

    def iterpackets(self):
        """iterate through packets generated by the encoder so far
        """
        iter = vpx_codec_iter_t()
        while 1:
            pktp = vpx_codec_get_cx_data(self.codec, iter)
            if not pktp:
                break
            yield pktp.contents




class VpxDecodeStream(object):
    """encode a series of frames to a VP8 stream"""

    def __init__(self):
        #self.shape = shape

        self.interface = vpx_codec_vp8_dx()
        print 'codec',vpx_codec_iface_name(self.interface)

        self.codec = vpx_codec_ctx_t()

        flags = 0
        res = vpx_codec_dec_init(self.codec, self.interface, None, flags)

        self.framei = 0

    def decode(self, buf, buf_sz):
        """frame is a buffer object
        """
        # buf should be a ctypes.LP_c_ubyte
        res = vpx_codec_decode(self.codec, buf, buf_sz, None, 0)
        checkvpxres(res, 'vpx_codec_decode')

        # drain
        for i,(ys,us,vs) in enumerate(self.iterframes()):

            nim = Nimage(Grid(None, shape=ys.shape), data=ys)
            nim.save_raster(os.path.join(self.outdir, '%04d.png'%self.framei))
            self.framei += 1

    def iterframes(self):
        iter = vpx_codec_iter_t()
        while 1:
            img = vpx_codec_get_frame(self.codec, iter)
            if not img: break

            print 'DEC'

            # copy the arrays since they point into external storage
            arrs = [np.array(a) for a in imgplanes(img, 3)]

            # XXX destroy img?

            yield arrs


    

if __name__ == '__main__':
    enc = VpxEncodeStream((256,256))
    #while 1:
    #    enc.encgrey()

    enc.outfp = open('out.vp8','wb')
    enc.decoder = VpxDecodeStream()
    enc.decoder.outdir = 'pngs'

    from glob import glob
    #for fn in glob('/xtra/run/download/2011-03-24T12Z/gfsmap/*/1/0/0.png'):
    for fn in glob('/xtra/pyvpx/satanim/*.png'):
        enc.encpng(fn)

