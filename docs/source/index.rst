==================================
Python AWIPS Data Access Framework
==================================

`AWIPS <http://unidata.github.io/awips2>`_ is a weather display and analysis package developed by the National Weather Service for operational forecasting.  UCAR's `Unidata Program Center <http://www.unidata.ucar.edu/software/awips2/>`_ supports a non-operational open-source release of the AWIPS software (`EDEX <http://unidata.github.io/awips2/#edex>`_, `CAVE <http://unidata.github.io/awips2/#cave>`_, and `python-awips <https://github.com/Unidata/python-awips>`_). 

The python-awips package provides a data access framework for requesting grid and geometry datasets from an `EDEX <http://unidata.github.io/awips2/#edex>`_ server.

.. _Jupyter Notebook: http://nbviewer.jupyter.org/github/Unidata/python-awips/tree/master/examples/notebooks

Install 
-------

- pip install python-awips

Requirements
~~~~~~~~~~~~

- Python 2.7+
- Shapely 1.4+
- MetPy and enum34 to run the `Jupyter Notebook`_ examples

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
    'grid',
    'hydro',
    'maps',
    'modelsounding',
    'obs',
    'practicewarning',
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

-------------
Documentation
-------------

.. toctree::
   :maxdepth: 2

   install
   api/index
   examples/index
   dev
   gridparms
   about
