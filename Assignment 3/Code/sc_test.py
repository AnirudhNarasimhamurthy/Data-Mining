import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram


x_coord=[]
y_coord=[]
point=[]	
cluster=[]
min=999999
max=-99999
""" Reading the input file C1 """
with open('C1.txt', 'r') as inputFile:
	data1 = inputFile.readlines()
	
	
	
""" Data cleaning and pre-processing"""
for data in data1:
	
	data=data.replace('\n','')
	point_id=data.split('	')[0]
	x=data.split('	')[1]
	y=data.split('	')[2]
	x_coord.append(x)
	y_coord.append(y)
	point.append(point_id)

""" Converting list of strings into float"""

point=map(int,point)
x_coord=map(float,x_coord)
y_coord=map(float, y_coord)

for i in range(0,len(point)):
	cluster+=[[x_coord[i],y_coord[i]]]


""" Making copies of the cluster list for the 3 variants """

slink_cluster=cluster
clink_cluster=cluster
meanlink_cluster=cluster




data_dist = pdist(slink_cluster) # computing the distance
data_link = linkage(data_dist,metric='Euclidean', method='single') # computing the linkage

dendrogram(data_link,labels=point)
plt.xlabel('Samples')
plt.ylabel('Distance')
plt.suptitle('Samples clustering', fontweight='bold', fontsize=14);
plt.show()