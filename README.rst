Python Data Access Framework for AWIPS II
=========================================

.. _Jupyter Notebook examples: http://nbviewer.jupyter.org/github/Unidata/python-awips/tree/master/examples/notebooks

.. image:: https://img.shields.io/pypi/v/python-awips.svg
        :target: https://pypi.python.org/pypi/python-awips/
        :alt: PyPI Package

.. image:: https://img.shields.io/pypi/dm/python-awips.svg
        :target: https://pypi.python.org/pypi/python-awips/
        :alt: PyPI Downloads

.. image:: https://readthedocs.org/projects/pip/badge/?version=latest
        :target: http://python-awips.readthedocs.org/en/latest/
        :alt: Latest Doc Build Status

Install
-------

- pip install python-awips

Requirements
-------------

- Python 2.7 minimum
- pip install numpy shapely
- pip install metpy enum34 - to run `Jupyter Notebook examples`_

Documentation
------------------

* http://python-awips.readthedocs.org/en/latest/
* `Jupyter Notebook examples`_

Install from Github
-----------

- git clone https://github.com/Unidata/python-awips.git
- cd python-awips
- python setup.py install


Install for AWIPS Python (/awips2/python)
--------------------

AWIPS II >=15.1.3 (March 2016) has `python-awips` bundled with the awips2-server and awips2-cave groups, as well as a full meteorological data stack (metpy, matplotlib, numpy, etc).

Easy install on an AWIPS system

- wget https://bootstrap.pypa.io/ez_setup.py -O - | /awips2/python/bin/python
- /awips2/python/bin/easy_install pip
- /awips2/python/bin/pip install python-awips

Grid Inventory
--------------

A short script to request available grid names from an EDEX server::

        #!python
        from awips.dataaccess import DataAccessLayer

        # Set host
        DataAccessLayer.changeEDEXHost("edex-cloud.unidata.ucar.edu")

        # Init data request
        request = DataAccessLayer.newDataRequest()

        # Set datatype
        request.setDatatype("grid")

        #
        # getAvailableLocationNames method will return a list of all available models
        #
        # LocationNames mean different things to different plugins beware...radar is icao,
        # satellite is sector, etc
        #
        available_grids = DataAccessLayer.getAvailableLocationNames(request)
        for grid in available_grids:
            print grid

