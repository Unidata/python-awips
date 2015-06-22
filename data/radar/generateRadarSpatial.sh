#!/bin/bash
# creates the radar_spatial table from an sql script file

echo "Generating new radar_spatial table"
psql -U awips -d metadata -c "DELETE FROM radar_spatial"
psql -U awips -d metadata -f ./radarSpatial.sql
echo "Done generating radar_spatial table"
