from numpy import genfromtxt
import numpy

TPO_data = genfromtxt('TPO_NoGraphics.csv', delimiter=',',dtype="str")
Time_Data = genfromtxt('TravelTime.csv', delimiter=',',dtype="str")
time = 0

def select_row(key):
        return A[Time_Data[key],1:]

def StackTPO(z,LastPosition,y,g):
	TravelTime = 0
	if LastPosition == "7":
		return 0
	else:
		greaterint = "7"
		if int(LastPosition) > 7:
			greaterint = LastPosition
			LastPosition = "7"
		for x in Time_Data:
			if x[0] == LastPosition:
				if x[1] == greaterint:
					TravelTime = int(x[3])
	TravelTime += int(z[6])
	TotalPoints = float(z[5])
	if z[4] != "":
		return [(TotalPoints+y)/(TravelTime+g),TravelTime,TotalPoints]
	else:
		return [TotalPoints/TravelTime,TravelTime,TotalPoints]


def ScoreTPO(z,LastPosition):
	return LastPosition

def OptimizedPath():
	LastPosition = "9"
	remaining = numpy.empty((0,8),str)
	tpo_rem = numpy.empty(63,str)
	for x in TPO_data:
		if x[0] != "Starting Position":
			if x[7] != "Done":
				remaining = numpy.vstack((remaining,x))
	lastp = 0
	lastt = 0
	for x in remaining:
		if x[1] == "Stack":
			d = StackTPO(x,LastPosition,lastp,lastt)
			print d[0]
			lastt = d[1]
			lastp = d[2]
		

OptimizedPath()

