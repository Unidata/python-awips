==================================
Python AWIPS Data Access Framework 
==================================

The python-awips package provides a data access framework for requesting meteorological and geographic datasets from an `EDEX <http://unidata.github.io/awips2/#edex>`_ server.

`AWIPS <http://unidata.github.io/awips2>`_ is a weather display and analysis package developed by the National Weather Service for operational forecasting.  UCAR's `Unidata Program Center <http://www.unidata.ucar.edu/software/awips2/>`_ supports a non-operational open-source release of the AWIPS software (`EDEX <http://unidata.github.io/awips2/#edex>`_, `CAVE <http://unidata.github.io/awips2/#cave>`_, and `python-awips <https://github.com/Unidata/python-awips>`_).

.. _Jupyter Notebook: http://nbviewer.jupyter.org/github/Unidata/python-awips/tree/master/examples/notebooks


.. important:: There is now a :ref:`Beta Python-AWIPS<Beta Python-AWIPS Install>` available for v20.

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
    
    

Beta Python-AWIPS Install
-------------------------

The beta version of python-awips (v20) is currently only available as a source code download and installation.  The beta version only works with our beta EDEX server (edex-beta.unidata.ucar.edu) and is not backwards compatible with our production (v18) EDEX server.

Similar to the :ref:`Source Code Install <Source Code with Examples Install>` above, these instructions will create a new environment called ``python-awips-beta20`` and launch a browser with our jupyter notebook examples.

When AWIPS v20 becomes production, this version of python-awips will be the default that is on pip and conda, but until then, this is how you can access and use python-awips v20.

::
  
    git clone --single-branch --branch v20 https://github.com/Unidata/python-awips.git
    cd python-awips
    conda env create -f environment.yml
    conda activate python-awips-beta20
    python setup.py install --force
    jupyter notebook examples



Questions -- Contact Us!
------------------------

Please feel free to reach out to us at our support email at **support-awips@unidata.ucar.edu**

.. toctree::
   :maxdepth: 2
   :hidden:

   api/index
   datatypes
   examples/index
   dev
   gridparms
   about
