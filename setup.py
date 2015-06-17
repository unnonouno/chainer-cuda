#!/usr/bin/env python
from setuptools import setup

setup(
    name='chainer-cuda',
    version='1.0.0',
    description='A flexible framework of neural networks',
    author='Seiya Tokui',
    author_email='tokui@preferred.jp',
    url='http://chainer.org/',
    packages=[],
    install_requires=[
        'pycuda>=2014.1',
        'scikits.cuda>=0.5.0b1,!=0.042',
        'Mako',
        'six>=1.9.0',
    ],
)
