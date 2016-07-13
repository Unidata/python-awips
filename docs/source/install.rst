.. _Jupyter Notebook: http://nbviewer.jupyter.org/github/Unidata/python-awips/tree/master/examples/notebooks

Install python-awips
------------------

- pip install python-awips

Requirements
~~~~~~~~~~~~

- Python 2.7 or later
- pip install numpy shapely
- pip install metpy enum34 - to run `Jupyter Notebook`_ examples

Install from Github
~~~~~~~~~~~~~~~~~~~~~~~~~~~

- git clone https://github.com/Unidata/python-awips.git
- cd python-awips
- python setup.py install


Install for AWIPS (/awips2/python)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

AWIPS II >=15.1.3 (March 2016) has `python-awips` bundled with the awips2-server and awips2-cave groups, as well as a full meteorological data stack (metpy, matplotlib, numpy, etc).

Easy install on an AWIPS system

- wget https://bootstrap.pypa.io/ez_setup.py -O - | /awips2/python/bin/python
- /awips2/python/bin/easy_install pip
- /awips2/python/bin/pip install python-awips

