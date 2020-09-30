==================================
Python AWIPS Data Access Framework 
==================================

The python-awips package provides a data access framework for requesting grid and geometry datasets from an `EDEX <http://unidata.github.io/awips2/#edex>`_ server.

`AWIPS <http://unidata.github.io/awips2>`_ is a weather display and analysis package developed by the National Weather Service for operational forecasting.  UCAR's `Unidata Program Center <http://www.unidata.ucar.edu/software/awips2/>`_ supports a non-operational open-source release of the AWIPS software (`EDEX <http://unidata.github.io/awips2/#edex>`_, `CAVE <http://unidata.github.io/awips2/#cave>`_, and `python-awips <https://github.com/Unidata/python-awips>`_).

.. _Jupyter Notebook: http://nbviewer.jupyter.org/github/Unidata/python-awips/tree/master/examples/notebooks

Pip Install
-----------

::

    pip install python-awips


Conda Environment Install
-------------------------

To install the latest version of python-awips, with all required and optional packages:

::

    git clone https://github.com/Unidata/python-awips.git
    cd python-awips
    conda env create -f environment.yml
    conda activate python3-awips
    python setup.py install --force
    jupyter notebook examples
    
**If you are experiencing issues, and have previously setup the conda environment, you may need to run:**
::
    conda update --all


Requirements
------------

These are specified in the environment.yml file that is used to create the 'python3-awips' conda environment:

   - python 3
   - numpy
   - nomkl
   - matplotlib
   - cartopy
   - jupyter
   - netcdf4
   - owslib
   - metpy
   - pint
   - h5py
   - nbconvert 4.1
   - siphon
   - xarray
   - ffmpeg
   - pytest
   - shapely
   - six
   - pip


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
