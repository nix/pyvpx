# Copyright (c) 2011 Nick Thompson
# Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

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

bytes_from_ptr = pythonapi.PyString_FromStringAndSize
if getattr(pythonapi, 'PyBytes_FromStringAndSize', None):
    bytes_from_ptr = pythonapi.PyBytes_FromStringAndSize
bytes_from_ptr.restype = py_object


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

    nx = raw.d_w
    ny = raw.d_h
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

    #errstr = vpx_codec_error(ctx);
    #detail = vpx_codec_error_detail(ctx);

    raise Exception("%s: %s" % (s, vpx_codec_err_to_string(res)))




class VpxEncodeStream(object):
    """encode a series of frames to a VP8 stream"""

    def __init__(self, shape):
        self.shape = shape

        self.interface = vpx_codec_vp8_cx()
        print 'codec',vpx_codec_iface_name(self.interface)

        self.passi = None
        self.npasses = 1

        # statistics data for two-pass encoding
        self.stats = []

        self.vpxconfig()

    def start_pass(self, passi):
        """must call this before encoding frames"""

        self.passi = passi

        if self.npasses > 1:
            if self.passi == 0:
                self.cfg.g_pass = VPX_RC_FIRST_PASS
            else:
                self.cfg.g_pass = VPX_RC_LAST_PASS
                # XXX self.stats is an array of bytestrings
                
                statstr = ''.join(self.stats)
                vpxstats = vpx_fixed_buf_t()
                vpxstats.buf = cast(c_char_p(statstr), c_void_p)
                vpxstats.sz = len(statstr)

                self.cfg.rc_twopass_stats_in = vpxstats
        else:
            self.cfg.g_pass = VPX_RC_ONE_PASS
    
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

            flag = ' '

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
                if fr.flags & VPX_FRAME_IS_KEY:
                    flag = 'K'

                kind = 'F'

            elif pkt.kind == VPX_CODEC_STATS_PKT:
                pktstats = pkt.data.twopass_stats
                buf = bytes_from_ptr(pktstats.buf, pktstats.sz)
                self.stats.append(buf)

                kind = 'S'

            else:
                kind = '%d' % pkt.kind


            print '%s %4d %s %10d' % (kind, self.framei, flag, fr.sz)


    def vpxconfig(self):
        cfg = vpx_codec_enc_cfg()

        res = vpx_codec_enc_config_default(self.interface, cfg, 0)
        checkvpxres(res, 'vpx_codec_enc_config_default')
    
        #print 'default shape', (cfg.g_h, cfg.g_w)
        #print 'default bitrate', cfg.rc_target_bitrate

        fps = 30

        # rc_target_bitrate is in kilobits per second
        default_bits_per_pixel_per_frame = cfg.rc_target_bitrate * 1024.0 / (cfg.g_h * cfg.g_w) / fps

        bits_per_pixel_per_frame = 0.2

        ny,nx = self.shape
        cfg.rc_target_bitrate = int(bits_per_pixel_per_frame * fps * nx * ny / 1024.0)
        cfg.g_w = nx
        cfg.g_h = ny


        print 'shape', (cfg.g_h, cfg.g_w)
        print 'bitrate', cfg.rc_target_bitrate
        print 'bpppf', bits_per_pixel_per_frame
        
        self.cfg = cfg

    def set_ref_frame(self, img):
        ref = vpx_ref_frame_t()
        ref.frame_type = VP8_LAST_FRAME
        ref.img = img

        checkvpxres(vpx_codec_control(self.codec, VP8_SET_REFERENCE, ref))
       
        # XXX free

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

        # force a keyframe every 8 frames
        if not (self.framei & 0x7):
            flags |= VPX_EFLAG_FORCE_KF
        else:
            flags &= ~VPX_EFLAG_FORCE_KF

        # test - oddly seems to break things, all frames after
        # the first are supercompressed
        #flags |= VPX_EFLAG_FORCE_KF

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

            #print 'DECODED', img

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
    fns = list(sorted(glob('/x/pyvpx/satanim/*.png')))

    enc.npasses = 1

    for passi in range(enc.npasses):
        enc.start_pass(passi)
        print '-'*30,'PASS',passi+1,'/',enc.npasses
        for fn in fns:
            enc.encpng(fn)
