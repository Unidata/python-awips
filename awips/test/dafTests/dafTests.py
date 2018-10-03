from testClimate import ClimateTestCase

geomData = ClimateTestCase.testGetGeometryData
for record in geomData:
    print(record.getGeometry())
print(dir(ClimateTestCase.testGetGeometryDataWithEnvelopeThrowsException))
print(dir(ClimateTestCase.testGetGeometryDataForYearAndDayOfYearTable))
print(dir(ClimateTestCase.testGetGeometryDataForPeriodTable))
print(dir(ClimateTestCase.testGetGeometryDataForDateTable))
print(dir(ClimateTestCase.testGetGeometryDataWithShortParameter))
print(dir(ClimateTestCase.testGetDataWithTimeRangeWithForDateTable))