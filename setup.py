from distutils.core import setup
from setuptools import find_packages

setup(
    name='ufpy',
    version='',
    #packages=['ufpy','ufpy.dataaccess',],
    packages=find_packages(exclude='data'),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
)
