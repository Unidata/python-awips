---
layout: default
type: about
title: Unidata AWIPS II
subtitle: About
shortname: Introducing
---

<style>
  .benchmark img {
    max-width: 500px;
  }
  .benchmark figcaption {
    font-weight: bold;
    margin-bottom: 16px;
  }
</style>

AWIPS II is a weather forecasting display and analysis package being developed by the National Weather Service and Raytheon. AWIPS II is a Java application consisting of a data-rendering client (CAVE, which runs on Red Hat/CentOS Linux and Mac OS X) and a backend data server (EDEX, which runs only on Linux)

AWIPS II takes a unified approach to data ingest, and most data types follow a standard path through the system. At a high level, data flow describes the path taken by a piece of data from its source to its display by a client system. This path starts with data requested and stored by an [LDM](#ldm) client and includes the decoding of the data and storing of decoded data in a form readable and displayable by the end user.

The AWIPS II ingest and request processes are a highly distributed system, and the messaging broken [Qpid](#qpid) is used for inter-process communication. 

![image](http://www.unidata.ucar.edu/software/awips2/images/awips2_coms.png)

[ldm]: http://www.unidata.ucar.edu/software/ldm/
[idd]: http://www.unidata.ucar.edu/projects/#idd
[gempak]: http://www.unidata.ucar.edu/software/gempak/
[awips2]: http://www.unidata.ucar.edu/software/awips2/
[ncep]: http://www.ncep.noaa.gov
[apache]: http://httpd.apache.org
[postgres]: www.postgresql.org
[hdf5]: http://www.hdfgroup.org/HDF5/
[eclipse]: http://www.eclipse.org
[camel]: http://camel.apache.org/ 
[spring]: http://www.springsource.org/ 
[hibernate]: http://www.hibernate.org/ 
[qpid]: http://qpid.apache.org 


## Software Components

* [EDEX](#edex)
* [CAVE](#cave)
* [Alertviz](#alertviz)
* [LDM](#ldm)
* [edexBridge](#edexbridge)
* [Qpid](#qpid)
* [PostgreSQL](#postgresql)
* [HDF5](#hdf5)
* [PyPIES](#pypies)


The primary AWIPS II application for data ingest, processing, and storage is the Environmental Data EXchange (**EDEX**) server; the primary AWIPS II application for visualization/data manipulation is the Common AWIPS Visualization Environment (**CAVE**) client, which is typically installed on a workstation separate from other AWIPS II components.  

In addition to programs developed specifically for AWIPS, AWIPS II uses several commercial off-the-shelf (COTS) and Free or Open Source software (FOSS) products to assist in its operation. The following components, working together and communicating, compose the entire AWIPS II system.

### EDEX

The main server for AWIPS II.  Qpid sends alerts to EDEX when data stored by the LDM is ready for processing.  These Qpid messages include file header information which allows EDEX to determine the appropriate data decoder to use.  The default ingest server (simply named ingest) handles all data ingest other than grib messages, which are processed by a separate ingestGrib server.  After decoding, EDEX writes metadata to the database via Postgres and saves the processed data in HDF5 via PyPIES.   A third EDEX server, request, feeds requested data to CAVE clients. EDEX ingest and request servers are started and stopped with the commands `edex start` and `edex stop`, which runs the system script `/etc/rc.d/init.d/edex_camel`

### CAVE

Common AWIPS Visualization Environment. The data rendering and visualization tool for AWIPS II. CAVE contains of a number of different data display configurations called perspectives.  Perspectives used in operational forecasting environments include **D2D** (Display Two-Dimensional), **GFE** (Graphical Forecast Editor), and **NCP** (National Centers Perspective). CAVE is started with the command `/awips2/cave/cave.sh` or `cave.sh`

![CAVE](http://www.unidata.ucar.edu/software/awips2/images/Unidata_AWIPS2_CAVE.png)

### Alertviz

**Alertviz** is a modernized version of an AWIPS I application, designed to present various notifications, error messages, and alarms to the user (forecaster). AlertViz can be executed either independently or from CAVE itself.  In the Unidata CAVE client, Alertviz is run within CAVE and is not required to be run separately.  The toolbar is also **hidden from view** and is accessed by right-click on the desktop taskbar icon.

### LDM

[http://www.unidata.ucar.edu/software/ldm/](http://www.unidata.ucar.edu/software/ldm/)

The **LDM** (Local Data Manager), developed and supported by Unidata, is a suite of client and server programs designed for data distribution, and is the fundamental component comprising the Unidata Internet Data Distribution (IDD) system. In AWIPS II, the LDM provides data feeds for grids, surface observations, upper-air profiles, satellite and radar imagery and various other meteorological datasets.   The LDM writes data directly to file and alerts EDEX via Qpid when a file is available for processing.  The LDM is started and stopped with the commands `edex start` and `edex stop`, which runs the commands `service edex_ldm start` and `service edex_ldm stop`

### edexBridge

edexBridge, invoked in the LDM configuration file `/awips2/ldm/etc/ldmd.conf`, is used by the LDM to post "data available" messaged to Qpid, which alerts the EDEX Ingest server that a file is ready for processing.

### Qpid

[http://qpid.apache.org](http://qpid.apache.org)

**Apache Qpid**, the Queue Processor Interface Daemon, is the messaging system used by AWIPS II to facilitate communication between services.  When the LDM receives a data file to be processed, it employs **edexBridge** to send EDEX ingest servers a message via Qpid.  When EDEX has finished decoding the file, it sends CAVE a message via Qpid that data are available for display or further processing. Qpid is started and stopped by `edex start` and `edex stop`, and is controlled by the system script `/etc/rc.d/init.d/qpidd`

### PostgreSQL
[http://www.postgresql.org](http://www.postgresql.org)

**PostgreSQL**, known simply as Postgres, is a relational database management system (DBMS) which handles the storage and retrieval of metadata, database tables and some decoded data.  The storage and reading of EDEX metadata is handled by the Postgres DBMS.  Users may query the metadata tables by using the termainal-based front-end for Postgres called **psql**. Postgres is started and stopped by `edex start` and `edex stop`, and is controlled by the system script `/etc/rc.d/init.d/edex_postgres`

### HDF5

[http://www.hdfgroup.org/HDF5/](http://www.hdfgroup.org/HDF5/)

[**Hierarchical Data Format (v.5)**][hdf5] is the primary data storage format used by AWIPS II for processed grids, satellite and radar imagery and other products.   Similar to netCDF, developed and supported by Unidata, HDF5 supports multiple types of data within a single file.  For example, a single HDF5 file of radar data may contain multiple volume scans of base reflectivity and base velocity as well as derived products such as composite reflectivity.  The file may also contain data from multiple radars. HDF5 is stored in `/awips2/edex/data/hdf5/`

### PyPIES (httpd-pypies)

**PyPIES**, Python Process Isolated Enhanced Storage, was created for AWIPS II to isolate the management of HDF5 Processed Data Storage from the EDEX processes.  PyPIES manages access, i.e., reads and writes, of data in the HDF5 files.  In a sense, PyPIES provides functionality similar to a DBMS (i.e PostgreSQL for metadata); all data being written to an HDF5 file is sent to PyPIES, and requests for data stored in HDF5 are processed by PyPIES.

PyPIES is implemented in two parts: 1. The PyPIES manager is a Python application that runs as part of an Apache HTTP server, and handles requests to store and retrieve data. 2. The PyPIES logger is a Python process that coordinates logging. PyPIES is started and stopped by `edex start` and `edex stop`, and is controlled by the system script `/etc/rc.d/init.d/https-pypies` 

