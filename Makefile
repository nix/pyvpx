# Copyright (c) 2011 Nick Thompson
# Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

#
#  Makefile for pyvpx
#
#  Should transition to setup.py
#
#  to rebuild vpxwrap.py, 
#    
#

LIBVPX=/xtra/libvpx
LIBVPX_SO=$(LIBVPX)/x86_build/libvpx.so.0.9.6

VPXHEADERS = vpx_image.h vpx_codec.h vp8cx.h vp8dx.h vpx_encoder.h vpx_decoder.h

ABSHEADERS = $(patsubst %,$(LIBVPX)/vpx/%,$(VPXHEADERS))

#MKVHEADERS = EbmlIDs.h EbmlWriter.h
#ABSHEADERS += $(patsubst %,$(LIBVPX)/libmkv/%,$(MKVHEADERS))

GENCTYPES = pyvpx/vpxwrap.py

test: $(GENCTYPES)
	python pyvpx/vpx.py

HEADERXML=pyvpx/vpxwrap.xml

$(HEADERXML): $(ABSHEADERS) Makefile
	h2xml.py $(ABSHEADERS) -I $(LIBVPX) -o $@ -c -k

$(GENCTYPES): $(HEADERXML)
	xml2py.py $^ -d -l $(LIBVPX_SO) -o $@ -v
