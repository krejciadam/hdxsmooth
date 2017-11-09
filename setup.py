#!/usr/bin/env python3
from distutils.core import setup

setup(
    name='HDXsmooth',
    version='0.1.0',
    author='Adam Krejci',
    author_email='krejciadam@gmail.com',
    packages=['hdxsmooth'],
    scripts=['bin/hdxsmooth'],
    license='LICENSE.txt',
    description='Calculate per-position deuteration levels from HDX (hydrogen-deuterium exchange) data.',
    long_description=open('README.md').read(),
)
