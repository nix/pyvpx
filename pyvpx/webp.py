
import os, sys

import struct





def wavwrap(buf, extradata=''):
    fmthdr = struct.pack('<HHLLHHH',
                         format_tag,
                         nchan,
                         samplerate,
                         byterate,
                         blockalighn,
                         bitspersample,
                         len(extradata))

    fmtblock = fmthdr + extradata

    wavhdr = struct.pack('<8sL',
                         'WAVEfmt ',
                         len(fmtblock))

    datahdr = struct.pack('<4sL',
                          'DATA ',
                          len(buf))

    return wavhdr + fmtblock + datahdr + buf



def webpwrap(buf):
    webphdr = struct.pack('<4s4sL',
                          'WEBP',
                          'VP8 ',
                          len(buf))

    return webphdr + buf


def riffwrap(buf):
    hdr = struct.pack('<4sL', 'RIFF', len(buf))
    return hdr + buf



