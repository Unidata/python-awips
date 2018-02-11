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
    request = DataAccessLayer.newDataRequest()
    dataTypes = DataAccessLayer.getSupportedDatatypes()
    request.setDatatype("grid")
    request.addLocationNames("RAP13")
    request.setParameters("T")
    request.setLevels("0.0SFC")
    cycles = DataAccessLayer.getAvailableTimes(request, True)
    times = DataAccessLayer.getAvailableTimes(request)
    response = DataAccessLayer.getGridData(request, times[-1])
    for grid in response:
        data = grid.getRawData()
        lons, lats = grid.getLatLonCoords()

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
