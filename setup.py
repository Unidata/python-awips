from distutils.core import setup
from setuptools import find_packages

setup(
    name='python-awips',
    version='0.9.9',
    description='A framework for requesting AWIPS meteorological datasets from an EDEX server',
    packages=find_packages(exclude='data'),
    license='Open Source',
    url='http://python-awips.readthedocs.io',
    download_url='https://github.com/Unidata/python-awips/tarball/0.9.9',
    author='Unidata',
    author_email='mjames@ucar.edu',
    requires=['argparse','shapely','numpy','six']
)

