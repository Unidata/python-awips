## Python Data Access Framework for AWIPS II EDEX

### Install Requirements

* easy_install argparse
* easy_install shapely
* yum install geos geos-devel (or "brew install goes" for OS X)

### Install

* git clone https://github.com/mjames-upc/edexpy.git
* cd edexpy
* python setup.py install

### Use

#### GRID

./data/grid/gridInventory.csh HRRR T

#### Radar

python data/radar/a2invradStub.py --icao kftg --date 2015-06-22 --time 17:09

#### Obs

python data/metar/a2gtmtrStub.py -b "2015-06-18 21:40" -e "2015-06-18 22:00" -s KCLK
