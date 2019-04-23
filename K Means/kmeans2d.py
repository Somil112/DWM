import numpy as np
import pandas as pd

dataset = pd.read_csv('km.csv')

X = dataset.iloc[:,[0]].values.flatten().tolist()
Y = dataset.iloc[:,[1]].values.flatten().tolist()

centroid1 = [X[0],Y[0]]
centroid2 = [X[1],Y[1]]

print("Initial Centroid Values")

print("Centroid 1: " + str(centroid1))
print("Centroid 2: " +  str(centroid2))


def calcdist2d(X,Y):
	global centroid1
	global centroid2
	c1X = []
	c1Y = []
	c2X = []
	c2Y = []
	c1newX = []
	c1newY = []
	c2newX = []
	c2newY = []
	flag = 0
	count = 0


	while(flag != 1):
		c1X = c1newX
		c1Y = c1newY
		c2X = c2newX
		c2Y = c2newY
		c1newX = []
		c1newY = []
		c2newX = []
		c2newY = []
		for i in range(len(X)):
			dist1 = np.sqrt(np.square(centroid1[0] - X[i]) + np.square(centroid1[1] - Y[i]))
			dist2 = np.sqrt(np.square(centroid2[0] - X[i]) + np.square(centroid2[1] - Y[i]))

			if(dist1>dist2):
				c2newX.append(X[i])
				c2newY.append(Y[i])
			else:
				c1newX.append(X[i])
				c1newY.append(Y[i])
		centroid1 = [np.mean(c1newX),np.mean(c1newY)]
		centroid2 = [np.mean(c2newX),np.mean(c2newY)]
		print("Centroid 1 is " + str(centroid1))
		print("Centroid 2 is " + str(centroid2))
		print("Cluster 1")
		print(c1newX,c1newY)
		print("Cluster 2")
		print(c2newX,c2newY)
		if(c1X != c1newX and c1Y != c1newY and c2X != c2newX and c2Y !=c2newY):
			flag = 0
		else:
			flag = 1
		count = count + 1
	
	print("Final Centroid values: ")
	print("Centroid 1: " + str(centroid1))
	
	print("Centroid 2: " + str(centroid2))

calcdist2d(X,Y)
