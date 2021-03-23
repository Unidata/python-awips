AWIPS Python Data Access Framework
==================================

|License| |PyPI| |Conda| |CondaDownloads| |circleci| |Travis| |LatestDocs|

|Codacy| |Scrutinizer| |CodeClimate| |PRWelcome|

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

.. |Travis| image:: https://travis-ci.org/Unidata/python-awips.svg?branch=main
        :target: https://travis-ci.org/Unidata/python-awips
        :alt: Travis Build Status

.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/e281f05c69164779814cad93eb3585cc
        :target: https://www.codacy.com/app/mjames/python-awips
        :alt: Codacy issues

.. |CodeClimate| image:: https://codeclimate.com/github/Unidata/python-awips/badges/gpa.svg
    :target: https://codeclimate.com/github/Unidata/python-awips
    :alt: Code Climate

.. |Scrutinizer| image:: https://scrutinizer-ci.com/g/Unidata/python-awips/badges/quality-score.png?b=main
    :target: https://scrutinizer-ci.com/g/Unidata/python-awips/?branch=main)
    :alt: Scrutinizer Code Quality

.. |Conda| image:: https://anaconda.org/conda-forge/python-awips/badges/version.svg
    :target: https://anaconda.org/conda-forge/python-awips
    :alt: Conda Package

.. |PRWelcome|
    image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=round-square
    :target: https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github
    :alt: PRs Welcome

.. |circleci|
    image:: https://img.shields.io/circleci/project/github/conda-forge/python-awips-feedstock/master.svg?label=noarch
    :target: https://circleci.com/gh/conda-forge/python-awips-feedstock
    :alt: circleci

.. |CondaDownloads|
   image:: https://img.shields.io/conda/dn/conda-forge/python-awips.svg
   :target: https://anaconda.org/conda-forge/python-awips
   :alt: Conda Downloads


About
-----

The python-awips package provides a data access framework for requesting grid and geometry datasets from an AWIPS `EDEX <http://unidata.github.io/awips2/#edex>`_ server. AWIPS and python-awips packages are released and maintained by UCAR's `Unidata Program Center <http://www.unidata.ucar.edu/software/awips2/>`_ in Boulder, Colorado.

Install
-------

- pip install python-awips

  or

- conda install -c conda-forge python-awips

Conda Environment
-----------------

- git clone https://github.com/Unidata/python-awips.git
- cd python-awips
- conda env create -f environment.yml
- conda activate python3-awips
- python setup.py install --force
- jupyter notebook examples


Documentation
-------------

* http://unidata.github.io/python-awips/
* http://nbviewer.jupyter.org/github/Unidata/python-awips/tree/main/examples/notebooks


License
-------

Unidata AWIPS source code and binaries (RPMs) are considered to be in the public domain, meaning there are no restrictions on any download, modification, or distribution in any form (original or modified). The Python AWIPS package contains no proprietery content and is therefore not subject to export controls as stated in the Master Rights licensing file and source code headers.
