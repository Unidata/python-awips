##
##


#
# __init__.py for Dynamic Serialize adapters.
#  
#    
#     SOFTWARE HISTORY
#    
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    08/31/10                      njensen       Initial Creation.
#    03/20/13           #1774      randerso      Added TimeConstraintsAdapter
#    04/22/13           #1949      rjpeter       Added LockTableAdapter
#    02/06/14           #2672      bsteffen      Added JTSEnvelopeAdapter
#    06/22/2015         #4573      randerso      Added JobProgressAdapter
#    09/21/2015         #4486      rjpeter       Added FormattedDateAdapter
#    06/23/2016         #5696      rjpeter       Added CommutativeTimestampAdapter
#

__all__ = [
           'PointAdapter',
           'StackTraceElementAdapter',
           'WsIdAdapter',
           'CalendarAdapter',
           'GregorianCalendarAdapter',
           'ActiveTableModeAdapter',
           'DateAdapter',
           'FormattedDateAdapter',
           'LocalizationLevelSerializationAdapter',
           'LocalizationTypeSerializationAdapter',
           'GeometryTypeAdapter',
           'CoordAdapter',
           'TimeRangeTypeAdapter',
           'ParmIDAdapter',
           'DatabaseIDAdapter',
           'TimestampAdapter',
           'CommutativeTimestampAdapter',
           'EnumSetAdapter',
           'FloatBufferAdapter',
           'ByteBufferAdapter',
           'TimeConstraintsAdapter',
           'LockTableAdapter',
           'JTSEnvelopeAdapter',
           'JobProgressAdapter',
           ]
 
classAdapterRegistry = {}

 
def getAdapterRegistry():
    import sys    
    for x in __all__:
        exec('import dynamicserialize.adapters.' + x )
        m = sys.modules['dynamicserialize.adapters.' + x]
        d = m.__dict__
        if 'ClassAdapter' in d:
            if isinstance(m.ClassAdapter, list):
                for clz in m.ClassAdapter:
                    classAdapterRegistry[clz] = m
            else:
                clzName = m.ClassAdapter
                classAdapterRegistry[clzName] = m
        else:
            raise LookupError('Adapter class ' + x + ' has no ClassAdapter field ' + \
                              'and cannot be registered.')
                               

getAdapterRegistry()

