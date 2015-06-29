== Using the DAF from Python to determine available model runs and available forecast steps for each model run ==

Apr 2, 2015 - Virgil Middendorf

The code below creates a Python Dictionary called ModelRunDict, where the keys are the available Model Run date/times (example key: Apr 02 15 06:00:00). Associated with each key, is a list array of Forecast Steps (in seconds after initialization) available for each Model Run.

```
#!python
# Getting the Model Run Date/Times and put them into a sorted dictionary, with latest run first.
ModelRunDict = dict()
ModelRunList = []
ModelRunTimes = DataAccessLayer.getAvailableTimes(req, refTimeOnly=True)
for ModelRunTime in ModelRunTimes:
	if not ModelRunDict.has_key(ModelRunTime.getRefTime()):
		ModelRunDateTimeObject = datetime.strptime(str(ModelRunTime.getRefTime()), '%b %d %y %H:%M:%S %Z')
		ModelRunList.append(ModelRunDateTimeObject)
ModelRunList.sort(reverse=True)
for ModelRun in ModelRunList:
	ModelRunDict[ModelRun.strftime('%b %d %y %H:%M:%S %Z') + "GMT"] = []

# Get the available forecast steps for each model run.
availableTimes = DataAccessLayer.getAvailableTimes(req)
for time in availableTimes:
	ModelRunDict[str(time.getRefTime())].append(time.getFcstTime())

# Printing out available model runs and forecast steps.
for ModelRun in ModelRunDict.keys():
	print "Model Run = {}".format(ModelRun)
	for step in ModelRunDict[ModelRun]:
		print "Forecast Step: {} Hours".format(int(step)/3600)

```

