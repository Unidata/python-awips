.. _Jupyter Notebook: http://nbviewer.jupyter.org/github/Unidata/python-awips/tree/master/examples/notebooks

Installation
------------------

- pip install python-awips

Requirements
~~~~~~~~~~~~

- Python 2.7 or later
- pip install numpy shapely
- pip install metpy enum34 - to run `Jupyter Notebook`_ examples

Install from Github
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- git clone https://github.com/Unidata/python-awips.git && cd python-awips
- python setup.py install


Install for AWIPS
~~~~~~~~~~~~~~~~~

On standalone AWIPS systems, the full `AWIPS Python Stack <about.html#awips-ii-python-stack>`_ is installed to ``/awips2/python`` as RPM packages. 

Easy install on an AWIPS system

* For Unidata AWIPS release **16.2.2+**:

        * /awips2/python/bin/easy_install pip
        * /awips2/python/bin/pip install python-awips
  
* For releases before and up to **16.1.5** you may need to run

        * yum install awips2-python-setuptools

