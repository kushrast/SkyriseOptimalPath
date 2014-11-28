import numpy

def ScoreTPO(z,LastPosition):
	thistime = 0
	points = numpy.empty((0,2),float)
	capacity = int(z[3])
	if capacity < 3:
		for x in xrange (1,capacity+1):
			#intaking code goes here
			if z[2] == "Small": #replace with a switch statement
				if x == 1:
					points = numpy.vstack((points,[3,2]))
				else:
					points = numpy.vstack((points,[6,4]))
			elif z[2] == "Medium":
				if x == 1:
					points = numpy.vstack((points,[6,2]))
				else:
					points = numpy.vstack((points,[9,4]))
			elif z[2] == "Large":
				if x == 1:
					points = numpy.vstack((points,[8,2]))
				else:
					points = numpy.vstack((points,[13,4]))
			else:
				if x == 1:
					points = numpy.vstack((points,[3,4]))
				else:
					points = numpy.vstack((points,[6,8]))
	else:
		for x in xrange(1,4):
			#intaking code goes here
			if z[2] == "Medium":
				if x == 1:
					points = numpy.vstack((points,[6,2]))
				elif x == 2:
					points = numpy.vstack((points,[9,4]))
				elif x == 3:
					points = numpy.vstack((points,[11,6]))
			elif z[2] == "Large":
				if x == 1:
					points = numpy.vstack((points,[8,2]))
				elif x == 2:
					points = numpy.vstack((points,[13,4]))
				elif x == 3:
					points = numpy.vstack((points,[16,6]))
			else:
				if x == 1:
					points = numpy.vstack((points,[3,4]))
				elif x == 2:
					points = numpy.vstack((points,[6,8]))
				elif x == 3:
					points = numpy.vstack((points,[9,12]))
	tpo = numpy.empty(len(points),float)
	for x in xrange(0,len(points)):
		tpo[x] = (points[x][1])/(points[x][0])
	tpox = numpy.argsort(tpo)
	numCubes = tpox[len(points)-1]
	return numCubes+1,tpo[numCubes]

print ScoreTPO(["7","9","Skyrise","6"],5)