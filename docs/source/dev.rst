
Development Guide
=================

The Data Access Framework allows developers to retrieve different types
of data without having dependencies on those types of data. It provides
a single, unified data type that can be customized by individual
implementing plug-ins to provide full functionality pertinent to each
data type.

Writing a New Factory
---------------------

Factories will most often be written in a dataplugin, but should always
be written in a common plug-in. This will allow for clean dependencies
from both CAVE and EDEX.

A new plug-in’s data access class must implement IDataFactory. For ease
of use, abstract classes have been created to combine similar methods.
Data factories do not have to implement both types of data (grid and
geometry). They can if they choose, but if they choose not to, they
should do the following:

::

    throw new UnsupportedOutputTypeException(request.getDatatype(), "grid");

This lets the code know that grid type is not supported for this data
factory. Depending on where the data is coming from, helpers have been
written to make writing a new data type factory easier. For example,
PluginDataObjects can use AbstractDataPluginFactory as a start and not
have to create everything from scratch.

Each data type is allowed to implement retrieval in any manner that is
felt necessary. The power of the framework means that the code
retrieving data does not have to know anything of the underlying
retrieval methods, only that it is getting data in a certain manner. To
see some examples of ways to retrieve data, reference
**SatelliteGridFactory** and **RadarGridFactory**.

Methods required for implementation:

**public DataTime[] getAvailableTimes(IDataRequest request)**

-  This method returns an array of DataTime objects corresponding to
   what times are available for the data being retrieved, based on the
   parameters and identifiers being passed in.

**public DataTime[] getAvailableTimes(IDataRequest request, BinOffset
binOffset)**

-  This method returns available times as above, only with a bin offset
   applied.

Note: Both of the preceding methods can throw TimeAgnosticDataException
exceptions if times do not apply to the data type.

**public IGridData[] getGridData(IDataRequest request,
DataTime...times)**

-  This method returns IGridData objects (an array) based on the request
   and times to request for. There can be multiple times or a single
   time.

**public IGridData[] getGridData(IDataRequest request, TimeRange
range)**

-  Similar to the preceding method, this returns IGridData objects based
   on a range of times.

**public IGeometryData[] getGeometryData(IDataRequest request, DataTime
times)**

-  This method returns IGeometryData objects based on a request and
   times.

**public IGeometryData[] getGeometryData(IDataRequest request, TimeRange
range)**

-  Like the preceding method, this method returns IGeometryData objects
   based on a range of times.

**public String[] getAvailableLocationNames(IDataRequest request)**

-  This method returns location names that match the request. If this
   does not apply to the data type, an IncompatibleRequestException
   should be thrown.

Registering the Factory with the Framework
------------------------------------------

The following needs to be added in a spring file in the plug-in that
contains the new factory:

::

    <bean id="radarGridFactory"
        class="com.raytheon.uf.common.dataplugin.radar.dataaccess.RadarGridFactory" /> 
    <bean factory-bean="dataAccessRegistry" factorymethod="register">
        <constructor-arg value="radar"/>
        <constructor-arg ref="radarGridFactory"/>
    </bean>

This takes the RadarGridFactory and registers it with the registry and
allows it to be used any time the code makes a request for the data type
“radar.”

Retrieving Data Using the Factory
---------------------------------

For ease of use and more diverse use, there are multiple interfaces into
the Data Access Layer. Currently, there is a Python implementation and a
Java implementation, which have very similar method calls and work in a
similar manner. Plug-ins that want to use the data access framework to
retrieve data should include **com.raytheon.uf.common.dataaccess** as a
Required Bundle in their MANIFEST.MF.

To retrieve data using the Python interface :

::

    from awips.dataaccess import DataAccessLayer
    req = DataAccessLayer.newDataRequest()
    req.setDatatype("grid")
    req.setParameters("T")
    req.setLevels("2FHAG")
    req.addIdentifier("info.datasetId", "GFS40")
    times = DataAccessLayer.getAvailableTimes(req)
    data = DataAccessLayer.getGridData(req, times)

To retrieve data using the Java interface :

::

    IDataRequest req = DataAccessLayer.newDataRequest();
    req.setDatatype("grid");
    req.setParameters("T");
    req.setLevels("2FHAG");
    req.addIdentifier("info.datasetId", "GFS40");
    DataTime[] times = DataAccessLayer.getAvailableTimes(req)
    IData data = DataAccessLayer.getGridData(req, times);

**newDataRequest()**

-  This creates a new data request. Most often this is a
   DefaultDataRequest, but saves for future implentations as well.

**setDatatype(String)**

-  This is the data type being retrieved. This can be found as the value
   that is registered when creating the new factory (See section above
   **Registering the Factory with the Framework** [radar in that case]).

**setParameters(String...)**

-  This can differ depending on data type. It is most often used as a
   main difference between products.

**setLevels(String...)**

-  This is often used to identify the same products on different
   mathematical angles, heights, levels, etc.

**addIdentifier(String, String)**

-  This differs based on data type, but is often used for more
   fine-tuned querying.

Both methods return a similar set of data and can be manipulated by
their respective languages. See DataAccessLayer.py and
DataAccessLayer.java for more methods that can be called to retrieve
data and different parts of the data. Because each data type has
different parameters, levels, and identifiers, it is best to see the
actual data type for the available options. If it is undocumented, then
the best way to identify what parameters are to be used is to reference
the code.

Development Background
----------------------

In support of Hazard Services Raytheon Technical Services is building a
generic data access framework that can be called via JAVA or Python. The
data access framework code can be found within the AWIPS Baseline in

::

    com.raytheon.uf.common.dataaccess

As of 2016, plugins have been written for grid, radar, satellite, Hydro
(SHEF), point data (METAR, SYNOP, Profiler, ACARS, AIREP, PIREP), maps
data, and other data types. The Factories for each can be found in the
following packages (you may need to look at the development baseline to
see these):

::

    com.raytheon.uf.common.dataplugin.grid.dataaccess
    com.raytheon.uf.common.dataplugin.radar.dataaccess
    com.raytheon.uf.common.dataplugin.satellite.dataaccess
    com.raytheon.uf.common.dataplugin.binlightning.dataaccess
    com.raytheon.uf.common.dataplugin.sfc.dataaccess
    com.raytheon.uf.common.dataplugin.sfcobs.dataaccess
    com.raytheon.uf.common.dataplugin.acars.dataaccess
    com.raytheon.uf.common.dataplugin.ffmp.dataaccess
    com.raytheon.uf.common.dataplugin.bufrua.dataaccess
    com.raytheon.uf.common.dataplugin.profiler.dataaccess
    com.raytheon.uf.common.dataplugin.moddelsounding.dataaccess
    com.raytheon.uf.common.dataplugin.ldadmesonet.dataaccess
    com.raytheon.uf.common.dataplugin.binlightning.dataaccess
    com.raytheon.uf.common.dataplugin.gfe.dataaccess
    com.raytheon.uf.common.hydro.dataaccess
    com.raytheon.uf.common.pointdata.dataaccess
    com.raytheon.uf.common.dataplugin.maps.dataaccess

Additional data types may be added in the future. To determine what
datatypes are supported display the "type hierarchy" associated with the
classes

**AbstractGridDataPluginFactory**,

**AbstractGeometryDatabaseFactory**, and

**AbstractGeometryTimeAgnosticDatabaseFactory**.

The following content was taken from the design review document which is
attached and modified slightly.

Design/Implementation
---------------------

The Data Access Framework is designed to provide a consistent interface
for requesting and using geospatial data within CAVE or EDEX. Examples
of geospatial data are grids, satellite, radar, metars, maps, river gage
heights, FFMP basin data, airmets, etc. To allow for convenient use of
geospatial data, the framework will support two types of requests: grids
and geometries (points, polygons, etc). The framework will also hide
implementation details of specific data types from users, making it
easier to use data without worrying about how the data objects are
structured or retrieved.

A suggested mapping of some current data types to one of the two
supported data requests is listed below. This list is not definitive and
can be expanded. If a developer can dream up an interpretation of the
data in the other supported request type, that support can be added.

Grids

-  Grib
-  Satellite
-  Radar
-  GFE

Geometries

-  Map (states, counties, zones, etc)
-  Hydro DB (IHFS)
-  Obs (metar)
-  FFMP
-  Hazard
-  Warning
-  CCFP
-  Airmet

The framework is designed around the concept of each data type plugin
contributing the necessary code for the framework to support its data.
For example, the satellite plugin provides a factory class for
interacting with the framework and registers itself as being compatible
with the Data Access Framework. This concept is similar to how EDEX in
AWIPS expects a plugin developer to provide a decoder class and
record class and register them, but then automatically manages the rest
of the ingest process including routing, storing, and alerting on new
data. This style of plugin architecture effectively enables the
framework to expand its capabilities to more data types without having
to alter the framework code itself. This will enable software developers
to incrementally add support for more data types as time allows, and
allow the framework to expand to new data types as they become
available.

The Data Access Framework will not break any existing functionality or
APIs, and there are no plans to retrofit existing cosde to use the new
API at this time. Ideally code will be retrofitted in the future to
improve ease of maintainability. The plugin pecific code that hooks into
the framework will make use of existing APIs such as **IDataStore** and
**IServerRequest** to complete the requests.

The Data Access Framework can be understood as three parts:

-  How users of the framework retrieve and use the data
-  How plugin developers contribute support for new data types
-  How the framework works when it receives a request

How users of the framework retrieve and use the data
----------------------------------------------------

When a user of the framework wishes to request data, they must
instantiate a request object and set some of the values on that request.
Two request interfaces will be supported, for detailed methods see
section "Detailed Code" below.

**IDataRequest**

**IGridRequest** extends **IDataRequest**

**IGeometryRequest** extends **IDataRequest**

For the request interfaces, default implementations of
**DefaultGridRequest** and **DefaultGeometryRequest** will be provided
to handle most cases. However, the use of interfaces allows for custom
special cases in the future. If necessary, the developer of a plugin can
write their own custom request implementation to handle a special case.

After the request object has been prepared, the user will pass it to the
Data Access Layer to receive a data object in return. See the "Detailed
Code" section below for detailed methods of the Data Access Layer. The
Data Access Layer will return one of two data interfaces.

**IData**

**IGridData** extends **IData**

**IGeometryData** extends **IData**

For the data interfaces, the use of interfaces effectively hides the
implementation details of specific data types from the user of the
framework. For example, the user receives an **IGridData** and knows the
data time, grid geometry, parameter, and level, but does not know that
the data is actually a **GFEGridData** vs **D2DGridData** vs
**SatelliteGridData**. This enables users of the framework to write
generic code that can support multiple data types.

For python users of the framework, the interfaces will be very similar
with a few key distinctions. Geometries will be represented by python
geometries from the open source Shapely project. For grids, the python
**IGridData** will have a method for requesting the raw data as a numpy
array, and the Data Access Layer will have methods for requesting the
latitude coordinates and the longitude coordinates of grids as numpy
arrays. The python requests and data objects will be pure python and not
JEP PyJObjects that wrap Java objects. A future goal of the Data Access
Framework is to provide support to python local apps and therefore
enable requests of data outside of CAVE and EDEX to go through the same
familiar interfaces. This goal is out of scope for this project but by
making the request and returned data objects pure python it will not be
a huge undertaking to add this support in the future.

How plugin developers contribute support for new datatypes
----------------------------------------------------------

When a developer wishes to add support for another data type to the
framework, they must implement one or both of the factory interfaces
within a common plugin. Two factory interfaces will be supported, for
detailed methods see below.

**IDataFactory**

**IGridFactory** extends **IDataFactory**

**IGeometryFactory** extends **IDataFactory**

For some data types, it may be desired to add support for both types of
requests. For example, the developer of grid data may want to provide
support for both grid requests and geometry requests. In this case the
developer would write two separate classes where one implements
**IGridFactory** and the other implements **IGeometryFactory**.
Furthermore, factories could be stacked on top of one another by having
factory implementations call into the Data Access Layer.

For example, a custom factory keyed to "derived" could be written for
derived parameters, and the implementation of that factory may then call
into the Data Access Layer to retrieve “grid” data. In this example the
raw data would be retrieved through the **GridDataFactory** while the
derived factory then applies the calculations before returning the data.

Implementations do not need to support all methods on the interfaces or
all values on the request objects. For example, a developer writing the
**MapGeometryFactory** does not need to support **getAvailableTimes()**
because map data such as US counties is time agnostic. In this case the
method should throw **UnsupportedOperationException** and the javadoc
will indicate this.

Another example would be the developer writing **ObsGeometryFactory**
can ignore the Level field of the **IDataRequest** as there are not
different levels of metar data, it is all at the surface. It is up to
the factory writer to determine which methods and fields to support and
which to ignore, but the factory writer should always code the factory
with the user requesting data in mind. If a user of the framework could
reasonably expect certain behavior from the framework based on the
request, the factory writer should implement support for that behavior.

Abstract factories will be provided and can be extended to reduce the
amount of code a factory developer has to write to complete some common
actions that will be used by multiple factories. The factory should be
capable of working within either CAVE or EDEX, therefore all of its
server specific actions (e.g. database queries) should go through the
Request/Handler API by using **IServerRequests**. CAVE can then send the
**IServerRequests** to EDEX with **ThriftClient** while EDEX can use the
**ServerRequestRouter** to process the **IServerRequests**, making the
code compatible regardless of which JVM it is running inside.

Once the factory code is written, it must be registered with the
framework as an available factory. This will be done through spring xml
in a common plugin, with the xml file inside the res/spring folder of
the plugin. Registering the factory will identify the datatype name that
must match what users would use as the datatype on the **IDataRequest**,
e.g. the word "satellite". Registering the factory also indicates to the
framework what request types are supported, i.e. grid vs geometry or
both.

An example of the spring xml for a satellite factory is provided below:

::

    <bean id="satelliteFactory" 
      class="com.raytheon.uf.common.dataplugin.satellite.SatelliteFactory" />

    <bean id="satelliteFactoryRegistered" factory-bean="dataFactoryRegistry" factory-method="register">
        <constructor-arg value="satellite" />
        <constructor-arg value="com.raytheon.uf.common.dataaccess.grid.IGridRequest" />
        <constructor-arg value="satelliteFactory" />
    </bean>

How the framework works when it receives a request
--------------------------------------------------

**IDataRequest** requires a datatype to be set on every request. The
framework will have a registry of existing factories for each data type
(grid and geometry). When the Data Access Layer methods are called, it
will first lookup in the registry for the factory that corresponds to
the datatype on the **IDataRequest**. If no corresponding factory is
found, it will throw an exception with a useful error message that
indicates there is no current support for that datatype request. If a
factory is found, it will delegate the processing of the request to the
factory. The factory will receive the request and process it, returning
the result back to the Data Access Layer which then returns it to the
caller.

By going through the Data Access Layer, the user is able to retrieve the
data and use it without understanding which factory was used, how the
factory retrieved the data, or what implementation of data was returned.
This effectively frees the framework and users of the framework from any
dependencies on any particular data types. Since these dependencies are
avoided, the specific **IDataFactory** and **IData** implementations can
be altered in the future if necessary and the code making use of the
framework will not need to be changed as long as the interfaces continue
to be met.

Essentially, the Data Access Framework is a service that provides data
in a consistent way, with the service capabilities being expanded by
plugin developers who write support for more data types. Note that the
framework itself is useless without plugins contributing and registering
**IDataFactories**. Once the framework is coded, developers will need to
be tasked to add the factories necessary to support the needed data
types.

Request interfaces
------------------

Requests and returned data interfaces will exist in both Java and
Python. The Java interfaces are listed below and the Python interfaces
will match the Java interfaces except where noted. Factories will only
be written in Java.

**IDataRequest**

-  **void setDatatype(String datatype)** - the datatype name and
   also the key to which factory will be used. Frequently pluginName
   such as radar, satellite, gfe, ffmp, etc

-  **void addIdentifier(String key, Object value)** - an identifier the
   factory can use to determine which data to return, e.g. for grib data
   key "modelName" and value “GFS40”

-  **void setParameters(String... params)**

-  **void setLevels(Level... levels)**

-  **String getDatatype()**

-  **Map getIdentifiers()**

-  **String[] getParameters()**

-  **Level[] getLevels()**

-  Python Differences

-  **Levels** will be represented as **Strings**

**IGridRequest extends IDataRequest**

-  **void setStorageRequest(Request request)** - a datastorage request
   that allows for slab, line, and point requests for faster performance
   and less data retrieval

-  **Request getStorageRequest()**

-  Python Differences

-  No support for storage requests

**IGeometryRequest extends IDataRequest**

-  **void setEnvelope(Envelope env)** - a bounding box envelope to limit
   the data that is searched through and returned. Not all factories may
   support this.

-  **setLocationNames(String... locationNames)** - a convenience of
   requesting data by names such as ICAOs, airports, stationIDs, etc

-  **Envelope getEnvelope()**

-  **String[] getLocationNames()**

-  Python Differences

-  Envelope methods will use a **shapely.geometry.Polygon** instead of
   **Envelopes** (shapely has no concept of envelopes and considers them
   as rectangular polygons)

Data Interfaces
~~~~~~~~~~~~~~~

**IData**

-  **Object getAttribute(String key)** - **getAttribute** provides a way
   to get at attributes of the data that the interface does not provide,
   allowing the user to get more info about the data without adding
   dependencies on the specific data type plugin

-  **DataTime getDataTime()** - some data may return null (e.g. maps)

-  **Level getLevel()** - some data may return null

-  Python Differences

-  **Levels** will be represented by **Strings**

**IGridData extends IData**

-  **String getParameter()**

-  **GridGeometry2D getGridGeometry()**

-  **Unit getUnit()** - some data may return null

-  **DataDestination populateData(DataDestination destination)** - How
   the user gets the raw data by passing in a **DataDestination** such
   as **FloatArrayWrapper** or **ByteBufferWrapper**. This allows the
   user to specify the way the raw data of the grid should be structured
   in memory.

-  **DataDestination populateData(DataDestination destination, Unit
   unit)** - Same as the above method but also attempts to convert the
   raw data to the specified unit when populating the
   **DataDestination**.

-  Python Differences

-  **Units** will be represented by **Strings**

-  **populateData()** methods will not exist, instead there will be
   a **getRawData()** method that returns a numpy array in the native
   type of the data

**IGeometryData extends IData**

-  **Geometry getGeometry()**

-  **Set getParameters()** - Gets the list of parameters included in
   this data

-  **String getString(String param)** - Gets the value of the parameter
   as a String

-  **Number getNumber(String param)** - Gets the value of the parameter
   as a Number

-  **Unit getUnit(String param)** - Gets the unit of the parameter,
   may be null

-  **Type getType(String param)** - Returns an enum of the raw type of
   the parameter, such as Float, Int, or String

-  **String getLocationName()** - Returns the location name of the piece
   of data, typically to correlate if the request was made with
   locationNames. May be null.

-  Python Differences

-  **Geometry** will be **shapely.geometry.Geometry**

-  **getNumber()** will return the python native number of the data

-  **Units** will be represented by **Strings**

-  **getType()** will return the python type object

**DataAccessLayer** (in implementation, these methods delegate
processing to factories)

-  **DataTime[] getAvailableTimes(IDataRequest request)**

-  **DataTime[] getAvailableTimes(IDataRequest request, BinOffset
   binOffset)**

-  **IData[] getData(IDataRequest request, DataTime... times)**

-  **IData[] getData(IDataRequest request, TimeRange timeRange)**

-  **GridGeometry2D getGridGeometry(IGridRequest request)**

-  **String[] getAvailableLocationNames(IGeometryRequest request)**

-  Python Differences

-  No support for **BinOffset**

-  **getGridGeometry(IGridRequest)** will be replaced by
   **getLatCoords(IGridRequest)** and **getLonCoords(IGridRequest)**
   that will return numpy arrays of the lat or lon of every grid
   cell

Factory Interfaces (Java only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **IDataFactory**

-  **DataTime[] getAvailableTimes(R request)** - queries the
   database and returns the times that match the request. Some factories
   may not support this (e.g. maps).

-  **DataTime[] getAvailableTimes(R request, BinOffset binOffset)** -
   queries the database with a bin offset and returns the times that
   match the request. Some factories may not support this.

-  **D[] getData(R request, DataTime... times)** - Gets the data that
   matches the request at the specified times.

-  **D[] getData(R request, TimeRange timeRange)** - Gets the data that
   matches the request and is within the time range.

**IGridDataFactory extends IDataFactory**

-  **GridGeometry2D** **getGeometry(IGridRequest request)** - Returns
   the grid geometry of the data that matches the request BEFORE making
   the request. Useful for then making slab or line requests for subsets
   of the data. Does not support moving grids, but moving grids don’t
   make subset requests either.

**IGeometryDataFactory extends IDataFactory**

-  **getAvailableLocationNames(IGeometryRequest request)** - Convenience
   method to retrieve available location names that match a request. Not
   all factories may support this.

