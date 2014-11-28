from numpy import genfromtxt
import numpy

TPO_data = genfromtxt('TPO_NoGraphics.csv', delimiter=',',dtype="str")
Time_Data = genfromtxt('TravelTime.csv', delimiter=',',dtype="str")
cubeloc = numpy.array([1,1,0,1,12,1,2,1,1])

time = 0
cubes = 20
#Region,ID,Pole Type,Time,Points Scored,Number of Cubes/Skyrises,TPO
def StackTPO(Capacity,LastPosition):
	#fairly simply - move function is already accounted for. just need to calculate time to add the next skyrise peg.
	if Capacity == 5:
		return 4,4,1,4.0/4.0
	elif Capacity == 4:
		return 8,4,1,4.0/8.0
	elif Capacity == 3:
		return 9,4,1,4.0/9.0
	elif Capacity == 2:
		return 9,4,1,4.0/9.0
	else:
		return 15,4,1,4.0/15.0


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
		points[x][0] += TimeToTile(LastPosition,z[0])
		tpo[x] = (points[x][1])/(points[x][0])
	tpox = numpy.argsort(tpo)
	numCubes = tpox[len(points)-1]
	return points[numCubes],numCubes+1,tpo[numCubes]

def TimeToTile(Start,End):
	#returns time taken from one tile to the next
	for x in Time_Data:
		if (Start == x[0] and End ==x[1]) or (End == x[0] and Start ==x[1]):
			return float(x[3])
	return 0

#def intaking(Start,numberofcubes):
	#returns time taken to intake, position of intaken cubes, and end position

def OptimizedPath():
	StartingPosition = "7";
	LastPosition = StartingPosition;
	time = 0.0;
	pointcounter = 0
	while time < 120.0:
		activities = numpy.empty((0,4),str)
		print "It has been "+str(time)+" seconds "+" and we're starting on Tile "+str(LastPosition);
		this_run = numpy.empty((0,7),str) #Region,ID,Pole Type,Time,Points Scored,Number of Cubes/Skyrises,TPO
		for x in TPO_data:
			if x[0] != "Region":
				if int(x[3]) > 0:
					activities = numpy.vstack((activities,x))
		for x in activities:
			if x[2] != "Stack":
				act_info = ScoreTPO(x,LastPosition)
				runtime = act_info[0][0]
				pointscored = act_info[0][1]
				numCubes = act_info[1]
				tpo = act_info[2]
				this_run = numpy.vstack((this_run,[x[0],x[1],x[2],runtime,pointscored,numCubes,tpo]))
			else:
				act_info = StackTPO(int(x[3]),LastPosition)
				runtime = act_info[0]
				pointscored = act_info[1]
				numCubes = act_info[2]
				tpo = act_info[3]
				this_run = numpy.vstack((this_run,[x[0],x[1],x[2],runtime,pointscored,numCubes,tpo]))
		best = numpy.argsort(this_run[:,6])
		bestsize = len(best)
		winner = this_run[best[bestsize-1]]
		for l in best[::-1]:
			newtime = time + float(this_run[l][3])
			if newtime < 120.0:
				winner = this_run[l]
				time = newtime
				break
			elif newtime > 120.0:
				time = 120				
				break
		place = int(TPO_data[int(winner[1])][3]) - 1
		TPO_data[int(winner[1])][3] = str(place)
		if winner[2] == "Stack":
			val = int(TPO_data[9][3]) + 1
			TPO_data[9][3] = str(val)
		LastPosition = winner[0]
		pointcounter += float(winner[4])
		if winner[2] == "Stack":
			print "We are now going to stack our "+str(5-int(TPO_data[8][3]))+"th skyrise"
		else:
			print "We are now going to score "+str(winner[5])+" cubes onto the "+winner[2]+" in region "+winner[0]+". This gives us another "+str(winner[4])+" points for a total of "+str(pointcounter)+" points."



OptimizedPath()

