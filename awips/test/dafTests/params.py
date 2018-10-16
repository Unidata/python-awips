#
# Site-specific parameters for DAF tests
#
#     SOFTWARE HISTORY
#
#    Date            Ticket#       Engineer       Description
#    ------------    ----------    -----------    --------------------------
#    12/07/16        5981          tgurney        Initial creation
#    12/15/16        5981          tgurney        Add ENVELOPE
#
#

from shapely.geometry import box


AIRPORT = 'OMA'
OBS_STATION = 'KOMA'
SITE_ID = 'OAX'
STATION_ID = '72558'
RADAR = 'KOAX'
SAMPLE_AREA = (-97.0, 41.0, -96.0, 42.0)

ENVELOPE = box(*SAMPLE_AREA)
