=====
About AWIPS II
=====

.. raw:: html

AWIPS II is a weather forecasting display and analysis package being
developed by the National Weather Service and Raytheon. AWIPS II is a
Java application consisting of a data-rendering client (CAVE, which runs
on Red Hat/CentOS Linux and Mac OS X) and a backend data server (EDEX,
which runs only on Linux)

AWIPS II takes a unified approach to data ingest, and most data types
follow a standard path through the system. At a high level, data flow
describes the path taken by a piece of data from its source to its
display by a client system. This path starts with data requested and
stored by an `LDM <#ldm>`_ client and includes the decoding of the data
and storing of decoded data in a form readable and displayable by the
end user.

The AWIPS II ingest and request processes are a highly distributed
system, and the messaging broken `Qpid <#qpid>`_ is used for
inter-process communication.

.. figure:: http://www.unidata.ucar.edu/software/awips2/images/awips2_coms.png
   :align: center
   :alt: image

   image

The primary AWIPS II application for data ingest, processing, and
storage is the Environmental Data EXchange (**EDEX**) server; the
primary AWIPS II application for visualization/data manipulation is the
Common AWIPS Visualization Environment (**CAVE**) client, which is
typically installed on a workstation separate from other AWIPS II
components.

In addition to programs developed specifically for AWIPS, AWIPS II uses
several commercial off-the-shelf (COTS) and Free or Open Source software
(FOSS) products to assist in its operation. The following components,
working together and communicating, compose the entire AWIPS II system.

AWIPS II Python Stack
---------------------

A number of Python packages are bundled with the AWIPS II EDEX and CAVE
installations, on top of base Python 2.7.9.


======================  ==============  ==============================
Package                 Version         RPM Name
======================  ==============  ==============================
Python                  2.7.9           awips2-python
pyparsing               2.1.0           awips2-python-pyparsing
scientific              2.8             awips2-python-scientific
pupynere                1.0.13          awips2-python-pupynere
tpg                     3.1.2           awips2-python-tpg
numpy                   1.10.4          awips2-python-numpy
jimporter               15.1.2          awips2-python-jimporter
basemap                 1.0.7           awips2-python-basemap
cherrypy                3.1.2           awips2-python-cherrypy
werkzeug                3.1.2           awips2-python-werkzeug
pycairo                 1.2.2           awips2-python-pycairo
six                     1.10.0          awips2-python-six
dateutil                2.5.0           awips2-python-dateutil
scipy                   0.17.0          awips2-python-scipy
metpy                   0.3.0           awips2-python-metpy
pygtk                   2.8.6           awips2-python-pygtk
**awips**               **0.9.2**       **awips2-python-awips**
shapely                 1.5.9           awips2-python-shapely
matplotlib              1.5.1           awips2-python-matplotlib
cython                  0.23.4          awips2-python-cython
pil                     1.1.6           awips2-python-pil
thrift                  20080411p1      awips2-python-thrift
cartopy                 0.13.0          awips2-python-cartopy
nose                    0.11.1          awips2-python-nose
pmw                     1.3.2           awips2-python-pmw
h5py                    1.3.0           awips2-python-h5py
tables                  2.1.2           awips2-python-tables
dynamicserialize        15.1.2          awips2-python-dynamicserialize
qpid                    0.32            awips2-python-qpid
======================  ==============  ==============================


EDEX
-------------------

The main server for AWIPS II. Qpid sends alerts to EDEX when data stored
by the LDM is ready for processing. These Qpid messages include file
header information which allows EDEX to determine the appropriate data
decoder to use. The default ingest server (simply named ingest) handles
all data ingest other than grib messages, which are processed by a
separate ingestGrib server. After decoding, EDEX writes metadata to the
database via Postgres and saves the processed data in HDF5 via PyPIES. A
third EDEX server, request, feeds requested data to CAVE clients. EDEX
ingest and request servers are started and stopped with the commands
``edex start`` and ``edex stop``, which runs the system script
``/etc/rc.d/init.d/edex_camel``

CAVE
-------------------

Common AWIPS Visualization Environment. The data rendering and
visualization tool for AWIPS II. CAVE contains of a number of different
data display configurations called perspectives. Perspectives used in
operational forecasting environments include **D2D** (Display
Two-Dimensional), **GFE** (Graphical Forecast Editor), and **NCP**
(National Centers Perspective). CAVE is started with the command
``/awips2/cave/cave.sh`` or ``cave.sh``

.. figure:: http://www.unidata.ucar.edu/software/awips2/images/Unidata_AWIPS2_CAVE.png
   :align: center
   :alt: CAVE

   CAVE

Alertviz
-------------------

**Alertviz** is a modernized version of an AWIPS I application, designed
to present various notifications, error messages, and alarms to the user
(forecaster). AlertViz can be executed either independently or from CAVE
itself. In the Unidata CAVE client, Alertviz is run within CAVE and is
not required to be run separately. The toolbar is also **hidden from
view** and is accessed by right-click on the desktop taskbar icon.

LDM
-------------------

`http://www.unidata.ucar.edu/software/ldm/ <http://www.unidata.ucar.edu/software/ldm/>`_

The **LDM** (Local Data Manager), developed and supported by Unidata, is
a suite of client and server programs designed for data distribution,
and is the fundamental component comprising the Unidata Internet Data
Distribution (IDD) system. In AWIPS II, the LDM provides data feeds for
grids, surface observations, upper-air profiles, satellite and radar
imagery and various other meteorological datasets. The LDM writes data
directly to file and alerts EDEX via Qpid when a file is available for
processing. The LDM is started and stopped with the commands
``edex start`` and ``edex stop``, which runs the commands
``service edex_ldm start`` and ``service edex_ldm stop``

edexBridge
-------------------

edexBridge, invoked in the LDM configuration file
``/awips2/ldm/etc/ldmd.conf``, is used by the LDM to post "data
available" messaged to Qpid, which alerts the EDEX Ingest server that a
file is ready for processing.

Qpid
-------------------

`http://qpid.apache.org <http://qpid.apache.org>`_

**Apache Qpid**, the Queue Processor Interface Daemon, is the messaging
system used by AWIPS II to facilitate communication between services.
When the LDM receives a data file to be processed, it employs
**edexBridge** to send EDEX ingest servers a message via Qpid. When EDEX
has finished decoding the file, it sends CAVE a message via Qpid that
data are available for display or further processing. Qpid is started
and stopped by ``edex start`` and ``edex stop``, and is controlled by
the system script ``/etc/rc.d/init.d/qpidd``

PostgreSQL
-------------------

`http://www.postgresql.org <http://www.postgresql.org>`_

**PostgreSQL**, known simply as Postgres, is a relational database
management system (DBMS) which handles the storage and retrieval of
metadata, database tables and some decoded data. The storage and reading
of EDEX metadata is handled by the Postgres DBMS. Users may query the
metadata tables by using the termainal-based front-end for Postgres
called **psql**. Postgres is started and stopped by ``edex start`` and
``edex stop``, and is controlled by the system script
``/etc/rc.d/init.d/edex_postgres``

HDF5
-------------------

`http://www.hdfgroup.org/HDF5/ <http://www.hdfgroup.org/HDF5/>`_

**Hierarchical Data Format (v.5)** is
the primary data storage format used by AWIPS II for processed grids,
satellite and radar imagery and other products. Similar to netCDF,
developed and supported by Unidata, HDF5 supports multiple types of data
within a single file. For example, a single HDF5 file of radar data may
contain multiple volume scans of base reflectivity and base velocity as
well as derived products such as composite reflectivity. The file may
also contain data from multiple radars. HDF5 is stored in
``/awips2/edex/data/hdf5/``

PyPIES (httpd-pypies)
-------------------

**PyPIES**, Python Process Isolated Enhanced Storage, was created for
AWIPS II to isolate the management of HDF5 Processed Data Storage from
the EDEX processes. PyPIES manages access, i.e., reads and writes, of
data in the HDF5 files. In a sense, PyPIES provides functionality
similar to a DBMS (i.e PostgreSQL for metadata); all data being written
to an HDF5 file is sent to PyPIES, and requests for data stored in HDF5
are processed by PyPIES.

PyPIES is implemented in two parts: 1. The PyPIES manager is a Python
application that runs as part of an Apache HTTP server, and handles
requests to store and retrieve data. 2. The PyPIES logger is a Python
process that coordinates logging. PyPIES is started and stopped by
``edex start`` and ``edex stop``, and is controlled by the system script
``/etc/rc.d/init.d/https-pypies``
