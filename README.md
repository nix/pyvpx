
A proof of concept for accessing Google's libvpx VP8 encoder using Python's ctypes.

Uses ctypeslib(http://pypi.python.org/pypi/ctypeslib/) and GCC-XML to build the low-level libvpx ctypes wrapper.

See also http://starship.python.net/crew/theller/ctypes/old/codegen.html

A pre-built wrapper is included.

This is in a very raw state, but may be useful to somebody.

The vpx.py file basically transcodes a series of PNG images through the
VP8 encoder and decoder just to make sure things are working.
It's based on simple_encoder.c and simple_decoder.c from the libvpx
example source.

Images are passed as Numpy arrays.

This code uses my own image i/o library, most people will want PIL instead.

