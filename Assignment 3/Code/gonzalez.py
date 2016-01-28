import matplotlib.pyplot as plt
import HC


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
means_cost=0

""" Reading the input file C1 """
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


""" Making copies of the cluster list for the 3 variants 

slink_cluster=cluster
clink_cluster=cluster
meanlink_cluster=cluster"""


c1=[(cluster[0][0],cluster[0][1])]
c+=c1
Centers.append(c1)

for j in range(0, len(cluster)):
	phi.append(0)

for i in range(1, no_of_clusters):
	max=-99999
	c+=[(cluster[0])]
	for j in range(0, len(cluster)):
		x=phi[j]
		dist= ((c[x][0]-cluster[j][0])** 2 + (c[x][1] - cluster[j][1])**2 )**0.5
		#print 'Distance is :', dist
		if dist > max:
			max=dist
			c_temp=(cluster[j])
	c[i]=c_temp
	#print 'c is :', c
	#print 'Max distance is :', max		
	for j in range(0, len(cluster)):
		x=phi[j]
		dist1=	((c[x][0]-cluster[j][0])** 2 + (c[x][1] - cluster[j][1])**2 )**0.5
		dist2=	((c[i][0] -cluster[j][0])** 2 + (c[i][1] - cluster[j][1])**2 )**0.5
		if( dist1 > dist2):
			#print 'here :'
			phi[j]=i
	
""" Calculating subsets and indexes to the cluster centers"""

for j in range(0, len(phi)):
	if phi[j]==0:
		subset1.append(cluster[j])
		indexes1.append(j+1)
	elif phi[j]==1:
		subset2.append(cluster[j])
		indexes2.append(j+1)
	else:
		subset3.append(cluster[j])
		indexes3.append(j+1)

""" Calculating the 3-center cost """

for i in range(0,len(cluster)):
	x=phi[i]
	center_dist=((c[x][0] - cluster[i][0]) **2 + (c[x][1] - cluster[i][1])**2 )** 0.5
	if center_dist > max_dist:
		max_dist=center_dist
		#print 'Max is :', max_dist
	else:
		a=1
		#print 'Distance is :', center_dist	

print 'Centers are :', c

print '3-center cost is :', max_dist		


""" Calculating the 3-means cost """

for i in range(0, len(cluster)):
	x=phi[i]
	means_cost+=(((c[x][0] - cluster[i][0]) **2 + (c[x][1] - cluster[i][1])**2 )** 0.5)**2

#means_cost=means_cost/ float(len(cluster))

print '3-means cost is :', means_cost

 
				

print '\n Indexes are :'
print '******************************'
print 'Cluster 1:', indexes1
print '******************************'
print 'Cluster 2:', indexes2
print '******************************'
print 'Cluster 3:', indexes3
print '******************************'


""" Plotting the data """

title="Clustering using Gonzalez algorithm "
HC.lloyds_plot(cluster,phi,c,title)



"""
print '\n Subsets are :'
print '******************************'
print 'Subset 1:', subset1
print '******************************'
print 'Subset 2:', subset2
print '******************************'
print 'Subset 3:', subset3
print '******************************'
"""
			