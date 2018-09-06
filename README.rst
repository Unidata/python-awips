AWIPS Python Data Access Framework
==================================

|License| |PyPI| |LatestDocs| 

|Travis| |Codacy|

.. |License| image:: https://img.shields.io/pypi/l/python-awips.svg
    :target: https://pypi.python.org/pypi/python-awips/
    :alt: License

.. |PyPI| image:: https://img.shields.io/pypi/v/python-awips.svg
        :target: https://pypi.python.org/pypi/python-awips/
        :alt: PyPI Package

.. |PyPIDownloads| image:: https://img.shields.io/pypi/dm/python-awips.svg
        :target: https://pypi.python.org/pypi/python-awips/
        :alt: PyPI Downloads

.. |LatestDocs| image:: https://readthedocs.org/projects/pip/badge/?version=latest
        :target: http://python-awips.readthedocs.org/en/latest/
        :alt: Latest Doc Build Status

.. |Travis| image:: https://travis-ci.org/Unidata/python-awips.svg?branch=master
        :target: https://travis-ci.org/Unidata/python-awips
        :alt: Travis Build Status

.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/560b27db294449ed9484da1aadeaee91
        :target: https://www.codacy.com/app/mjames/python-awips
        :alt: Codacy issues


Install
-------

- pip install python-awips

Conda Environment
-----------------

- git clone https://github.com/Unidata/python-awips.git
- cd python-awips
- conda env create -f environment.yml
- source activate python-awips
- python setup.py install --force
- jupyter notebook examples

Requirements
------------

- Python 2.7+
- pip install numpy shapely six
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


License
-------

Unidata AWIPS source code and binaries (RPMs) are considered to be in the public domain, meaning there are no restrictions on any download, modification, or distribution in any form (original or modified). The Python AWIPS package contains no proprietery content and is therefore not subject to export controls as stated in the Master Rights licensing file and source code headers.
