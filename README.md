
A proof of concept for accessing Google's libvpx VP8 encoder using Python's ctypes.

Uses ctypeslib and GCC-XML to build the low-level libvpx ctypes wrapper.
A pre-built wrapper is included.

This is in a very raw state, but will hopefully be useful to somebody.
Maybe it will turn into something more, maybe not.

The vpx.py file basically transcodes a series of PNG images through the
VP8 encoder and decoder just to make sure things are working.
It's based on simple_encoder.c and simple_decoder.c from the libvpx
example source.



