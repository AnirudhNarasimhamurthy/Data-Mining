import matplotlib.pyplot as plt
import HC
import random
import numpy as np

x_coord=[]
y_coord=[]
point=[]	
cluster=[]
min=999999
max_dist=-999
mean=9999
no_of_clusters=3
Centers=[]
phi=[]
c=[]
subset1,subset2,subset3=[],[],[]
indexes1,indexes2,indexes3=[],[],[]
cluster1,cluster2,cluster3=[],[],[]
means_cost=0
total_dist=0
means_dist=0
dist_matrix=[]
r=[]
cum_dist=0
means_cost=0
new_cost=0
""" Reading the input file C2 """
with open('C2.txt', 'r') as inputFile:
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

""" Building the cluster list of lists """

for i in range(0,len(point)):
	cluster+=[(x_coord[i],y_coord[i])]


"Picking the first center as the first point in the data  set """



"""Initializing the phi array with center 0 """
for counter in range(0, 1):

	c=[]
	c1=[(cluster[0][0],cluster[0][1])]
	c+=c1
	phi=[]
	for j in range(0, len(cluster)):
		phi.append(0)


	"""Finding the cluster centers """

	for i in range(1, no_of_clusters):
		c+=[(cluster[0])]
	
		#print 'Iteration :',i
		print 'c is :', c
		for j in range(0,len(cluster)):
			x=phi[j]
	
		""" Calculating the weight for fitting a distribution """
	
		for j in range(0, len(cluster)):
			x=phi[j]
			dist_matrix.append((c[x][0]-cluster[j][0])** 2 + (c[x][1] - cluster[j][1])**2) 
			total_dist+= (c[x][0]-cluster[j][0])** 2 + (c[x][1] - cluster[j][1])**2 
	
		""" Constructing the r matrix/array which has (distance)^2 / sum of all distances"""
	
		for j in range(0, len(cluster)):
			cum_dist+=dist_matrix[j] / float(total_dist)
			r.append(cum_dist)
		#print 'r is :', r
	
		""" Determining the cluster center """
	
		u= random.uniform(0,1)
		print 'Random no generated is :', u
	
		for j in range(0, len(cluster)):
			if u <= r[j]:
				temp=(cluster[j])
				break
			else:
				u=u-r[j]
		c[i]=temp
	
		""" Updating a points center to the new center if its distance to the new center is 
		smaller """
	
		for j in range(0, len(cluster)):
			x=phi[j]
			dist1=	((c[x][0]-cluster[j][0])** 2 + (c[x][1] - cluster[j][1])**2 )**0.5
			dist2=	((c[i][0] -cluster[j][0])** 2 + (c[i][1] - cluster[j][1])**2 )**0.5
			if dist1 > dist2 :
				phi[j]=i

		r=[]
		dist_matrix=[]
		cum_dist=0
		total_dist=0
		print 'Center is :', c


	""" Calculating the 3-means cost """


	for j in range(0,len(cluster)):
		x=phi[j]
		new_cost+=(c[x][0]-cluster[j][0])**2 + (c[x][1]-cluster[j][1]) **2
		#means_cost=means_dist /float(len(cluster))
	
	""" Printing information about indexes and clusters """

	for j in range(0, len(cluster)):
		if phi[j]==0:
			cluster1.append(cluster[j])
			indexes1.append(j+1)
		elif phi[j]==1:
			cluster2.append(cluster[j])
			indexes2.append(j+1)
		elif phi[j]==2:
			cluster3.append(cluster[j])
			indexes3.append(j+1)


	print '\n Indexes are :'
	print '******************************'
	print 'Cluster 1:', indexes1
	print '******************************'
	print 'Cluster 2:', indexes2
	print '******************************'
	print 'Cluster 3:', indexes3
	print '******************************'

	print 'Centers calculated are :', c

	print '3-means cost is :', new_cost

	indexes1=[]
	indexes2=[]
	indexes3=[]
	""" Plotting the data """

	title="Clustering using k-Means++ algorithm "
	HC.kmeansplusplus_plot(cluster,phi,c,title)


	val1=str(new_cost)
	val2=str(c)
	f = open( 'k_means+.txt', 'a' )
	#headers='3-means cost'
	#f.write(''.join(headers) + '\n')
	#f.write ( '3 means cost =' +'\n')
	f.write (val1 + '\t'+ val2 +'\n' )
	f.close()
	new_cost=0 	
   

