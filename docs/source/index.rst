==================================
Python AWIPS Data Access Framework 
==================================

The python-awips package provides a data access framework for requesting meteorological and geographic datasets from an `EDEX <http://unidata.github.io/awips2/#edex>`_ server.

`AWIPS <http://unidata.github.io/awips2>`_ is a weather display and analysis package developed by the National Weather Service for operational forecasting.  UCAR's `Unidata Program Center <http://www.unidata.ucar.edu/software/awips2/>`_ supports a non-operational open-source release of the AWIPS software (`EDEX <http://unidata.github.io/awips2/#edex>`_, `CAVE <http://unidata.github.io/awips2/#cave>`_, and `python-awips <https://github.com/Unidata/python-awips>`_).

.. _Jupyter Notebook: http://nbviewer.jupyter.org/github/Unidata/python-awips/tree/master/examples/notebooks


Pre-requisite Software
----------------------

In order to effictively use python-awips you'll need to have these installed already:
  - python3
  - conda
  - git *(for the source code and examples installation)*

Package-Only Install
--------------------

If you already work with Python, you might just be interested in how to install the python-awips pacakge.
The package can be installed with either of the two well known package managers: **pip** and **conda**.

Pip Install
~~~~~~~~~~~

::

    pip install python-awips


Conda Install
~~~~~~~~~~~~~

::

    conda install -c conda-forge python-awips



Source Code with Examples Install
---------------------------------

Below are instructions on how to install the source code of python-awips, with all included example notebooks.  This will create a new conda environment called ``python3-awips`` and start up a browser for the jupyter notebook examples.

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
    
    
Questions -- Contact Us!
------------------------

Please feel free to reach out to us at our support email at **support-awips@unidata.ucar.edu**
