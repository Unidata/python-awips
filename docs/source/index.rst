==================================
Python AWIPS Data Access Framework 
==================================

The python-awips package provides a data access framework for requesting grid and geometry datasets from an `EDEX <http://unidata.github.io/awips2/#edex>`_ server.

`AWIPS <http://unidata.github.io/awips2>`_ is a weather display and analysis package developed by the National Weather Service for operational forecasting.  UCAR's `Unidata Program Center <http://www.unidata.ucar.edu/software/awips2/>`_ supports a non-operational open-source release of the AWIPS software (`EDEX <http://unidata.github.io/awips2/#edex>`_, `CAVE <http://unidata.github.io/awips2/#cave>`_, and `python-awips <https://github.com/Unidata/python-awips>`_).

.. _Jupyter Notebook: http://nbviewer.jupyter.org/github/Unidata/python-awips/tree/master/examples/notebooks

Pip Install
-----------

- pip install python-awips

Conda Environment Install
-------------------------

To install the latest version of python-awips, with all required and optional packages:

- git clone https://github.com/Unidata/python-awips.git
- cd python-awips
- conda env create -f environment.yml
- conda activate python3-awips
- conda update - -all
- python setup.py install - -force
- jupyter notebook examples

Requirements
------------

- python 2.7+
- numpy
- shapely
- six


Quick Example
~~~~~~~~~~~~~

::

    from awips.dataaccess import DataAccessLayer
    DataAccessLayer.changeEDEXHost("edex-cloud.unidata.ucar.edu")
    dataTypes = DataAccessLayer.getSupportedDatatypes()
    list(dataTypes)

    ['acars',
     'binlightning',
     'bufrmosavn',
     'bufrmoseta',
     'bufrmosgfs',
     'bufrmoshpc',
     'bufrmoslamp',
     'bufrmosmrf',
     'bufrua',
     'climate',
     'common_obs_spatial',
     'gfe',
     'gfeeditarea',
     'grid',
     'maps',
     'modelsounding',
     'obs',
     'practicewarning',
     'profiler',
     'radar',
     'radar_spatial',
     'satellite',
     'sfcobs',
     'topo',
     'warning']


    request = DataAccessLayer.newDataRequest()
    request.setDatatype("satellite")
    availableSectors = DataAccessLayer.getAvailableLocationNames(request)
    availableSectors.sort()
    for sector in availableSectors:
        print sector
        request.setLocationNames(sector)
        availableProducts = DataAccessLayer.getAvailableParameters(request)
        availableProducts.sort()
        for product in availableProducts:
            print " - " + product

    ECONUS
     - ACTP
     - ADP
     - AOD
     - CAPE
     - CH-01-0.47um
     - CH-02-0.64um
     - CH-03-0.87um
     - CH-04-1.38um
     ...
    EFD
     - ACTP
     - ADP
     - AOD
     - CAPE
     - CH-01-0.47um
     - CH-02-0.64um
     - CH-03-0.87um
     - CH-04-1.38um
     ...


See the `API Documentation <api/DataAccessLayer.html>`_ for more information.

----------------------
Read The Docs Contents
----------------------

.. toctree::
   :maxdepth: 2

   api/index
   datatypes
   examples/index
   dev
   gridparms
   about
