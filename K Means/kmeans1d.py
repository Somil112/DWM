import pandas as pd 
import numpy as np

# To import from csv uncomment
# dataset = pd.read_csv('filename.csv')


dataset = [2,4,10,12,3,20,33,11,25]

"""
Choose initial centroids as the first two values
from the dataset.
"""
centroid1 = dataset[0]
centroid2 = dataset[1]



flag = 0

# Lists for storing clusters
c1new = []
c2new = []

while(flag!=1):
	c1 = c1new
	c2 = c2new
	c1new = []
	c2new = []
	"""
	Check distance between centroid and data points.
	Jiska bhi kam hai woh cluster mai jaayga.
	"""
	for i in range(len(dataset)):
		dist1 = abs(centroid1 - dataset[i])
		dist2 = abs(centroid2 - dataset[i])
		if(dist1>dist2):
			c2new.append(dataset[i])
		else:
			c1new.append(dataset[i])
	"""
	Finally after the clusters are created,
	calculate the new centroid, which is the
	mean of the cluster values.
	"""
	centroid1 = np.mean(c1new)
	centroid2 = np.mean(c2new)
	"""
	Check if the old cluster and new cluster is not same.
	If it is same, then end the loop.
	"""
	if(c1new != c1 and c2new != c2):
		flag = 0
		print("Cluster 1:\n",c1new)
		print("Cluster 2:\n",c2new)
	else:
		flag = 1

print("Final Centroid Values:")
print("Centroid 1: \n ",centroid1)
print("Centroid 2: \n ",centroid2)


