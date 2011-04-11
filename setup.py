#!/usr/bin/python

# Copyright (c) 2011 Nick Thompson
# Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pyvpx',
    version='0.1',
    author='Nick Thompson',
    author_email='nix@nixweb.com',
    maintainer_email='nix@nixweb.com',
    license='MIT',
    url='http://nixweb.com',
    description='Rudimentary Python wrapper around libvpx',
    long_description="""A wrapper around libvpx using ctypes.""",
    packages=['pyvpx'],
    scripts=[],

    install_requires=[
        # numpy
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console'
        ],
)
