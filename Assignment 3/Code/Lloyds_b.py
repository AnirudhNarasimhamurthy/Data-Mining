import matplotlib.pyplot as plt
import HC


x_coord=[]
y_coord=[]
point=[]	
cluster=[]
max_dist=-999
mean=9999
no_of_clusters=3
Centers=[]
phi=[]
c=[]
cluster1,cluster2,cluster3=[],[],[]
indexes1,indexes2,indexes3=[],[],[]
means_cost=0
c0_x,c0_y,c1_x,c1_y,c2_x,c2_y=0,0,0,0,0,0
c0_center, c1_center,c2_center=0,0,0
centers_average=[]
centers_count=[]
means_dist=0
three_means_cost=0

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



for j in range(0, len(cluster)):
	phi.append(0)

"""for i in range(0, no_of_clusters):
	c+=[(cluster[i][0],cluster[i][1])]"""
c=[(-19.0748, -8.536), (-40.0, 40.0), (29.10710988, -8.527838244)]	


b=set(c)	

#print 'The set b is :', b
counter=0

while (1):

	counter=counter + 1
	b=set(c)
	print 'The set c now is :', b
	#print 'c[0][0] is :', c[0][0]
	#print 'c[1][0] is :', c[1][0]
	#print 'c[2][0] is :', c[2][1]
	
	
	for j in range(0, len(cluster)):
		dist1=((cluster[j][0]- c[0][0])**2 + (cluster[j][1] - c[0][1])**2)**0.5
		dist2=((cluster[j][0]- c[1][0])**2 + (cluster[j][1] - c[1][1])**2)**0.5
		dist3=((cluster[j][0]- c[2][0])**2 + (cluster[j][1] - c[2][1])**2)**0.5
		
		
		#print 'Dist1 is :', dist1
		#print 'Dist2 is :', dist2
		#print 'Dist3 is :', dist3
		min_dist=HC.my_min(dist1,dist2,dist3)
		
		#print 'Minimum is :', min_dist
		if min_dist==dist1:
			phi[j]=0
			c0_x+=cluster[j][0]
			c0_y+=cluster[j][1]
			c0_center+=1
		elif min_dist==dist2:
			phi[j]=1
			c1_x+=cluster[j][0]
			c1_y+=cluster[j][1]
			c1_center+=1
		elif min_dist==dist3:
			phi[j]=2		
			c2_x+=cluster[j][0]
			c2_y+=cluster[j][1]
			c2_center+=1


	#for j in range(0, len(cluster)):
		#print 'Point :', cluster[j], 'its center is :', phi[j] 

	centers_average.append((c0_x,c0_y))
	centers_average.append((c1_x,c1_y))
	centers_average.append((c2_x,c2_y))
	

	#print 'Centers average is :', centers_average


	centers_count.append(c0_center)
	centers_count.append(c1_center)
	centers_count.append(c2_center)

	print 'Centers count is :', centers_count
	
	"""Re-setting counter variables and other arrays to default values"""
	c0_x,c0_y=0,0
	c1_x,c1_y=0,0
	c2_x,c2_y=0,0
	c0_center,c1_center,c2_center=0,0,0 
	c[:]=[]
	
	#print 'Set c is :', c

	for i in range(0, no_of_clusters):
		cx=centers_average[i][0]/float(centers_count[i])
		cy=centers_average[i][1] /float(centers_count[i])
		c+=[(cx,cy)]	
	
	centers_average[:]=[]
	centers_count[:]=[]
	
	#d=set(c)
	
	#print 'Set d is :', d
	#print 'Set b is :', b
	
	if (set(b).intersection(c) == set(c)):
		print 'The centers are :', c
		print 'Counter is :', counter
		break
	


for j in range(0, len(cluster)):
	x=phi[j]
	three_means_cost+=(c[x][0]-cluster[j][0])**2 + (c[x][1]-cluster[j][1]) **2

#three_means_cost=means_dist / float(len(cluster))

print '3 means cost is :', three_means_cost	


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

	
	
""" Plotting the data """

title="Output of Llyods algorithm with C initially as the output of Gonzalez algorithm"
HC.lloyds_plot(cluster,phi,c,title)	
	
	
