# Copyright (c) 2017 UCAR Unidata Program Center.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
from __future__ import print_function
import sys
from distutils.core import setup
from setuptools import find_packages

dependencies = ['numpy']
if sys.version_info < (3, 4):
    dependencies.append('enum34')

ver = "20.1"

setup(
    name='python-awips',
    version=ver,
    description='A framework for requesting AWIPS meteorological datasets from an EDEX server',
    packages=find_packages(exclude='data'),
    license='BSD',
    url='http://unidata.github.io/python-awips',
    author='NSF Unidata',
    author_email='support-awips@ucar.edu',
    install_requires=dependencies,
    extras_require={
        'cdm': ['pyproj>=1.9.4'],
        'dev': ['ipython[all]>=3.1'],
        'doc': ['sphinx>=1.4', 'sphinx-gallery', 'doc8'],
        'examples': ['cartopy>=0.13.1', 'metpy>=0.4.0']
    }
)
