Python Data Access Framework for AWIPS II
=========================================

|PyPI| |PyPIDownloads| |LatestDocs|

.. |PyPI| image:: https://img.shields.io/pypi/v/python-awips.svg
        :target: https://pypi.python.org/pypi/python-awips/
        :alt: PyPI Package

.. |PyPIDownloads| image:: https://img.shields.io/pypi/dm/python-awips.svg
        :target: https://pypi.python.org/pypi/python-awips/
        :alt: PyPI Downloads

.. |LatestDocs| image:: https://readthedocs.org/projects/pip/badge/?version=latest
        :target: http://python-awips.readthedocs.org/en/latest/
        :alt: Latest Doc Build Status

Install
-------

- pip install python-awips

Requirements
------------

- Python 2.7 minimum
- pip install numpy shapely
- pip install metpy enum34 - to run Jupyter Notebook examples

Documentation
-------------

* http://python-awips.readthedocs.org/en/latest/
* http://nbviewer.jupyter.org/github/Unidata/python-awips/tree/master/examples/notebooks

Install from Github
-------------------

- git clone https://github.com/Unidata/python-awips.git
- cd python-awips
- python setup.py install


Install for AWIPS (/awips2/python)
-----------------------------------------

AWIPS II >=15.1.3 (March 2016) has `python-awips` bundled with the awips2-server and awips2-cave groups, as well as a full meteorological data stack (metpy, matplotlib, numpy, etc).

Easy install on an AWIPS system

- wget https://bootstrap.pypa.io/ez_setup.py -O - | /awips2/python/bin/python
- /awips2/python/bin/easy_install pip
- /awips2/python/bin/pip install python-awips
