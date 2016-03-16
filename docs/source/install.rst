Installation Guide
==================

- pip install python-awips

Requirements
-------------

- Python 2.7 or later 
- pip install numpy shapely

From Github
-----------

- git clone https://github.com/Unidata/python-awips.git
- cd python-awips
-  python setup.py install


Install for AWIPS II Python
--------------------

AWIPS II >=15.1.3 (March 2016) has `python-awips` installed in /awips2/python, as well as a full meteorological data stack (metpy, matplotlib, numpy, etc).

For AWIPS II systems 15.1.2 and lower:

- wget https://bootstrap.pypa.io/ez_setup.py -O - | /awips2/python/bin/python
- /awips2/python/bin/easy_install pip
- /awips2/python/bin/pip install python-awips
