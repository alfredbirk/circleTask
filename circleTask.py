#Given 2 points randomly placed  in a circle, 
#what is the probability that the distance between the two points 
#is greater than the sum of the shortest distances from each point to the outer edge of the circle

from math import sqrt
from random import uniform


r = 6 #arbitrary radius
trials = 1000000
numYes = 0

def getRandomPoint():
	x = uniform(-6, 6)

	maxY = sqrt(36-x**2)
	minY = -maxY

	y = uniform(minY, maxY)

	return x, y

def getDistToCircle(x, y):
	return abs(sqrt(x**2+y**2) - r)

def getDistBetweenPoints(x1, y1, x2, y2):
	return sqrt((x2-x1)**2 + (y2-y1)**2)

for i in range(trials):
	x1, y1 = getRandomPoint()
	x2, y2 = getRandomPoint()
	#print("x1: ", x1, "y1", y1)
	#print("x2: ", x2, "y2", y2)

	dist = getDistBetweenPoints(x1, y1, x2, y2)

	#print("dist: ", dist)

	d1 = getDistToCircle(x1, y1)
	d2 = getDistToCircle(x2, y2)
	#print("d1: ", d1)
	#print("d2: ", d2)

	summ = d1 + d2
	#print(summ)

	if(dist > summ):
		numYes += 1

print(numYes/trials)


