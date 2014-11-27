from numpy import genfromtxt
import numpy

TPO_data = genfromtxt('TPO_NoGraphics.csv', delimiter=',',dtype="str")
Time_Data = genfromtxt('TravelTime.csv', delimiter=',',dtype="str")
time = 0
cubes = 20

def StackTPO(z,LastPosition,y,g):
	#fairly simply - move function is already accounted for. just need to calculate time to add the next skyrise peg.


def ScoreTPO(z,LastPosition):
	thistime = 0
	runs = []
	points = []
	tpo = []
	capacity = int(z[3])
	if capacity < 3:
		while x in xrange (1,capacity+1):
			#intaking code goes here
			if z[2] == "Small": #replace with a switch statement
				if x == 1:
					runs[0] = 3
					points[0] = 2
				else:
					runs[1] = 6
					points[1] = 4
			else if z[2] == "Medium":
				if x == 1:
					runs[0] = 6
					points[0] = 2
				else:
					runs[1] = 9
					points[1] = 4
			else if z[2] == "Large":
				if x == 1:
					runs[0] = 8
					points[0] = 2
				else:
					runs[1] = 13
					points[1] = 4
			else:
				if x == 1:
					runs[0] = 3
					points[0] = 2
				else:
					runs[1] = 6
					points[1] = 4
	else:
		while x in xrange(1,4):
			#intaking code goes here
			else if z[2] == "Medium":
				if x == 1:
					runs[0] = 6
					points[0] = 2
				else if x == 2:
					runs[1] = 9
					points[1] = 4
				else if x == 3:
					runs[2] = 11
					points[2] = 6
			else if z[2] == "Large":
				if x == 1:
					runs[0] = 8
					points[0] = 2
				else if x == 2:
					runs[1] = 13
					points[1] = 4
				else if x == 3:
					runs[2] = 16
					points[2] = 6
			else:
				if x == 1:
					runs[0] = 3
					points[0] = 2
				else if x == 2:
					runs[1] = 6
					points[1] = 4
				else if x == 3:
					runs[2] = 9
					points[2] = 6
	for x in xrange(0,len(runs)):
		tpo[x] = points[x]/runs[x] #need to return the tpo, time, and points. 

def TimeToTile(Start,End):
	#returns time taken from one tile to the next

def intaking(Start,numberofcubes):
	#returns time taken to intake, position of intaken cubes, and end position

def OptimizedPath():
	StartingPosition = 7;
	LastPosition = StartingPosition;
	time = 15;
	while time < 120:
		print "It has been "+time+" seconds "+" and we're starting on Tile "+LastPosition;
		this_run = numpy.empty((0,4),str)
		for x in activities:
			if int(x[3]) > 0:
				if x[2] != "Stack":
					this_run = numpy.append(this_run,[x[0],x[1],x[2],ScoreTPO(x,LastPosition)])


	/* remaining = numpy.empty((0,8),str)
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
			lastp = d[2] */
		

OptimizedPath()

