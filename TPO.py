from numpy import genfromtxt
import numpy

TPO_data = genfromtxt('TPO_NoGraphics.csv', delimiter=',',dtype="str")
Time_Data = genfromtxt('TravelTime.csv', delimiter=',',dtype="str")
cubeloc = numpy.array([1,1,0,1,12,1,2,1,1])
mountainL = numpy.array([1,1,1,1,1,1])
mountainR = numpy.array([1,1,1,1,1,1])

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
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 3
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,2]))
				else:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 6
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,4]))
			elif z[2] == "Medium":
				if x == 1:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 6
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,2]))
				else:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 9
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,4]))
			elif z[2] == "Large":
				if x == 1:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 8
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,2]))
				else:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 13
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,4]))
			else:
				if x == 1:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 3
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,4]))
				else:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 6
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,8]))
	else:
		for x in xrange(1,4):
			#intaking code goes here
			if z[2] == "Medium":
				if x == 1:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 6
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,2]))
				elif x == 2:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 9
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,4]))
				elif x == 3:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 11
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,6]))
			elif z[2] == "Large":
				if x == 1:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 8
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,2]))
				elif x == 2:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 13
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,4]))
				elif x == 3:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 16
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,6]))
			else:
				if x == 1:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 3
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,4]))
				elif x == 2:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 6
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,8]))
				elif x == 3:
					intake = intaking(LastPosition,x,"No")
					time = intake[0] + 9
					LastPosition = intake[1]
					points = numpy.vstack((points,[time,12]))
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

def side(Start):
	if Start == 1 or Start == 2 or Start == 4 or Start == 7:
		return "L"
	else:
		return "R"

def intaking(Start,numberofcubes,persistent):
	#returns time taken to intake, position of intaken cubes, and end position
	time = 0
	if persistent == "No":
		if cubeloc[int(Start)-1] >= numberofcubes:
			return numberofcubes*2.5,Start
		else:
			if cubeloc[int(Start) -1] != 0:
				numberofcubes -= cubeloc[int(Start)-1]
				time += cubeloc[int(Start)-1]*2.5
			if side(int(Start)) == "L" or numpy.sum(mountainR) == 0:
				for x in xrange(0,7):
					if x == 0 and mountainL[x] == 1:
						time += 2.5
						numberofcubes -= 1
					elif x == 1 and mountainL[x] == 1:
						time += 3.5
						numberofcubes -= 1
					elif x == 2 and mountainL[x] == 1:
						time += 2.5
						numberofcubes -= 1
					elif x == 3 and mountainL[x] == 1:
						time += 4.5
						numberofcubes -= 1
					elif x == 4 and mountainL[x] == 1:
						time += 3.5
						numberofcubes -= 1
					elif x == 5 and mountainL[x] == 1:
						time += 2.5
						numberofcubes -= 1
					if numberofcubes == 0:
						return time,Start
			if side(int(Start)) == "R" or numpy.sum(mountainL) == 0:
				for x in xrange(0,7):
					if x == 0 and mountainR[x] == 1:
						time += 2.5
						numberofcubes -= 1
					elif x == 1 and mountainR[x] == 1:
						time += 3.5
						numberofcubes -= 1
					elif x == 2 and mountainR[x] == 1:
						time += 2.5
						numberofcubes -= 1
					elif x == 3 and mountainR[x] == 1:
						time += 4.5
						numberofcubes -= 1
					elif x == 4 and mountainR[x] == 1:
						time += 3.5
						numberofcubes -= 1
					elif x == 5 and mountainR[x] == 1:
						time += 2.5
						numberofcubes -= 1
					if numberofcubes == 0:
						return time,Start
			if int(Start) > 0 and int(Start) < 4:
				for x in xrange(0,3):
					if cubeloc[x] >= numberofcubes:
						time += TimeToTile(Start,str(x+1))
						return time,str(x+1)
					elif cubeloc[x] < numberofcubes:
						numberofcubes -= cubeloc[x]
			else:
				for x in xrange(3,9):
					if x != 4:
						if cubeloc[x] >= numberofcubes:
							cubeloc[x] -= numberofcubes
							time += TimeToTile(Start,str(x+1))
							return time,str(x+1)
						elif cubeloc[x] < numberofcubes:
							numberofcubes -= cubeloc[x]
							cubeloc[x] = 0
	else:
		if numpy.sum(cubeloc) == 0:
					return 1000,Start
		elif cubeloc[int(Start)-1] >= numberofcubes:
			cubeloc[int(Start)-1] -= numberofcubes
			return numberofcubes*2.5,Start
		else:
			if cubeloc[int(Start) -1] != 0:
				cubeloc[int(Start) -1] -= numberofcubes
				numberofcubes -= cubeloc[int(Start)-1]
				time += cubeloc[int(Start)-1]*2.5
			if side(int(Start)) == "L" or numpy.sum(mountainR) == 0:
				for x in xrange(0,7):
					if x == 0 and mountainL[x] == 1:
						time += 2.5
						numberofcubes -= 1
						cubeloc[4] -= 1
						mountainL[x] = 0
					elif x == 1 and mountainL[x] == 1:
						time += 3.5
						numberofcubes -= 1
						cubeloc[4] -= 1
						mountainL[x] = 0
					elif x == 2 and mountainL[x] == 1:
						time += 2.5
						numberofcubes -= 1
						cubeloc[4] -= 1
						mountainL[x] = 0
					elif x == 3 and mountainL[x] == 1:
						time += 4.5
						numberofcubes -= 1
						cubeloc[4] -= 1
						mountainL[x] = 0
					elif x == 4 and mountainL[x] == 1:
						time += 3.5
						numberofcubes -= 1
						cubeloc[4] -= 1
						mountainL[x] = 0
					elif x == 5 and mountainL[x] == 1:
						time += 2.5
						numberofcubes -= 1
						cubeloc[4] -= 1
						mountainL[x] = 0
					if numberofcubes == 0:
						return time,Start
			if side(int(Start)) == "R" or numpy.sum(mountainL) == 0:
				for x in xrange(0,7):
					if x == 0 and mountainR[x] == 1:
						time += 2.5
						numberofcubes -= 1
						cubeloc[4] -= 1
						mountainR[x] = 0
					elif x == 1 and mountainR[x] == 1:
						time += 3.5
						numberofcubes -= 1
						cubeloc[4] -= 1
						mountainR[x] = 0
					elif x == 2 and mountainR[x] == 1:
						time += 2.5
						numberofcubes -= 1
						cubeloc[4] -= 1
						mountainR[x] = 0
					elif x == 3 and mountainR[x] == 1:
						time += 4.5
						numberofcubes -= 1
						cubeloc[4] -= 1
						mountainR[x] = 0
					elif x == 4 and mountainR[x] == 1:
						time += 3.5
						numberofcubes -= 1
						cubeloc[4] -= 1
						mountainR[x] = 0
					elif x == 5 and mountainR[x] == 1:
						time += 2.5
						numberofcubes -= 1
						cubeloc[4] -= 1
						mountainR[x] = 0
					if numberofcubes == 0:
						return time,Start
			if int(Start) > 0 and int(Start) < 4:
				for x in xrange(0,3):
					if cubeloc[x] >= numberofcubes:
						cubeloc[x] -= numberofcubes
						time += TimeToTile(Start,str(x+1))
						return time,str(x+1)
					elif cubeloc[x] < numberofcubes:
						numberofcubes -= cubeloc[x]
						cubeloc[x] = 0
			else:
				for x in xrange(3,9):
					if x != 4:
						if cubeloc[x] >= numberofcubes:
							cubeloc[x] -= numberofcubes
							time += TimeToTile(Start,str(x+1))
							return time,str(x+1)
						elif cubeloc[x] < numberofcubes:
							numberofcubes -= cubeloc[x]
							cubeloc[x] = 0
	return 1000,Start








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
		place = int(TPO_data[int(winner[1])][3]) - int(winner[5])
		TPO_data[int(winner[1])][3] = str(place)
		if winner[2] == "Stack":
			val = int(TPO_data[9][3]) + 1
			TPO_data[9][3] = str(val)
		pointcounter += float(winner[4])
		if winner[2] == "Stack":
			print "We are now going to stack our "+str(5-int(TPO_data[8][3]))+"th skyrise"

		else:
			intaking(LastPosition,int(winner[5]),"Yes")
			print "We are now going to score "+str(winner[5])+" cubes onto the "+winner[2]+" in region "+winner[0]+". This gives us another "+str(winner[4])+" points for a total of "+str(pointcounter)+" points."
		LastPosition = winner[0]


OptimizedPath()

