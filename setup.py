from distutils.core import setup
from setuptools import find_packages

setup(
    name='python-awips',
    version='0.9.4',
    description='A framework for requesting AWIPS meteorological datasets from an EDEX server',
    packages=find_packages(exclude='data'),
    license='Apache 2.0 / Various + US Export Controlled Technical Data',
    url='http://www.unidata.ucar.edu/software/awips2',
    download_url='https://github.com/Unidata/python-awips/tarball/0.9.4',
    author='Unidata',
    author_email='mjames@ucar.edu',
    requires=['argparse','shapely','numpy']
)

