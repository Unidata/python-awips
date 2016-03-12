Python Data Access Framework for AWIPS II
=========================================

.. image:: https://img.shields.io/pypi/v/python-awips.svg
       :target: https://pypi.python.org/pypi/python-awips/
    :alt: PyPI Package

.. image:: https://img.shields.io/pypi/dm/python-awips.svg
       :target: https://pypi.python.org/pypi/python-awips/
    :alt: PyPI Downloads

Install
-------

- pip install python-awips

Prerequisites
-------------

- yum install geos geos-devel
- pip install numpy shapely


From Github
-----------

- git clone https://github.com/Unidata/python-awips.git
- cd python-awips
-  python setup.py install


Install for AWIPS II Python
--------------------

- wget https://bootstrap.pypa.io/ez_setup.py -O - | /awips2/python/bin/python
- easy_install pip
- /awips2/python/bin/pip install python-awips

Grid Inventory
--------------

A short script to request availavle grid names from an EDEX server::

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

        

