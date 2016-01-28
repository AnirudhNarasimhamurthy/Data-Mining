
import matplotlib.pyplot as plt
import HC
import random

x_coord=[]
y_coord=[]
z_coord,v_coord,w_coord=[],[],[]
point=[]	
cluster=[]
max_dist=-999
mean=9999
minimum=99999
no_of_clusters=5
Centers=[]
phi=[]
c=[]
cluster1,cluster2,cluster3,cluster4,cluster5=[],[],[],[],[]
indexes1,indexes2,indexes3=[],[],[]
means_cost=0
c0_x,c0_y,c1_x,c1_y,c2_x,c2_y=0,0,0,0,0,0
c0_center, c1_center,c2_center=0,0,0
centers_average=[]
centers_count=[]
means_dist=0
new_cost_function=[]
cost_function=0
nos_set=[]

""" Reading the input file C3 """
with open('C3.txt', 'r') as inputFile:
	data1 = inputFile.readlines()
	
""" Data cleaning and pre-processing"""
for data in data1:
	
	data=data.replace('\n','')
	point_id=data.split('	')[0]
	v=data.split('	')[1]
	w=data.split('	')[2]
	x=data.split('	')[3]
	y=data.split('	')[4]
	z=data.split('	')[5]
	v_coord.append(v)
	w_coord.append(w)
	x_coord.append(x)
	y_coord.append(y)
	z_coord.append(z)
	point.append(point_id)

""" Converting list of strings into float"""

point=map(int,point)
v_coord=map(float,v_coord)
w_coord=map(float,w_coord)
x_coord=map(float,x_coord)
y_coord=map(float,y_coord)
z_coord=map(float, z_coord)

for i in range(0,len(point)):
	cluster+=[(v_coord[i],w_coord[i],x_coord[i],y_coord[i],z_coord[i])]


#print 'The clusters set is :', cluster


"""k-Median clustering """

for j in range(0, len(cluster)):
	phi.append(0)

"Randomly selecting the initial centers  """
for i in range(0, no_of_clusters):
	y= random.randint(0,len(cluster)-1)
	print 'y is :', y
	if y not in nos_set:
		nos_set.append(y)
		c+=[(cluster[y][0],cluster[y][1],cluster[y][2],cluster[y][3],cluster[y][4])]
	else:
		break

new_cost_function.append(0)
#b=set(c)	

#print 'The set b is :', b
counter=0

while (1):

	counter=counter + 1
	b=set(c)
	print 'The set c now is :', c
	
	
	for j in range(0, len(cluster)):
		dist1=((cluster[j][0]- c[0][0])**2 + (cluster[j][1] - c[0][1])**2 +(cluster[j][2] - c[0][2])**2 + (cluster[j][3] - c[0][3])**2+ (cluster[j][4] - c[0][4])**2)*0.5
		dist2=((cluster[j][0]- c[1][0])**2 + (cluster[j][1] - c[1][1])**2 +(cluster[j][2] - c[1][2])**2 + (cluster[j][3] - c[1][3])**2+ (cluster[j][4] - c[1][4])**2)*0.5
		dist3=((cluster[j][0]- c[2][0])**2 + (cluster[j][1] - c[2][1])**2 +(cluster[j][2] - c[2][2])**2 + (cluster[j][3] - c[2][3])**2+ (cluster[j][4] - c[2][4])**2)*0.5
		dist4=((cluster[j][0]- c[3][0])**2 + (cluster[j][1] - c[3][1])**2 +(cluster[j][2] - c[3][2])**2 + (cluster[j][3] - c[3][3])**2+ (cluster[j][4] - c[3][4])**2)*0.5
		dist5=((cluster[j][0]- c[4][0])**2 + (cluster[j][1] - c[4][1])**2 +(cluster[j][2] - c[4][2])**2 + (cluster[j][3] - c[4][3])**2+ (cluster[j][4] - c[4][4])**2)*0.5
		
		min_dist=HC.median5_min(dist1,dist2,dist3,dist4,dist5)
		
		#print 'Minimum is :', min_dist
		if min_dist==dist1:
			phi[j]=0
			cluster1.append(cluster[j])
		elif min_dist==dist2:
			phi[j]=1
			cluster2.append(cluster[j])
		elif min_dist==dist3:
			phi[j]=2	
			cluster3.append(cluster[j])	
		elif min_dist==dist4:
			phi[j]=3
			cluster4.append(cluster[j])	
		elif min_dist==dist5:
			phi[j]=4
			cluster5.append(cluster[j])	
	

	

	#for j in range(0, len(cluster)):
		#print 'Point :', cluster[j], 'its center is :', phi[j] 

	print 'Len cluster1 is :', len(cluster1)
	print 'Len cluster2 is :', len(cluster2)
	print 'Len cluster3 is :', len(cluster3)
	print 'Len cluster4 is :', len(cluster4)
	print 'Len cluster5 is :', len(cluster5)
	
	#print 'Previous center for cluster1 assigned :', c[0]
	#print 'Previous center for cluster2 assigned :', c[1]
	#print 'Previous center for cluster3 assigned :', c[2]
	#print 'Previous center for cluster4 assigned :', c[3]

		
	"""Estimating the cost-function values """
	
	for j in range(0, len(cluster)):
		x=phi[j]
		#print 'x is :', phi[j]
		cost_function+=((cluster[j][0]- c[x][0])**2 + (cluster[j][1] - c[x][1])**2 +(cluster[j][2] - c[x][2])**2 + (cluster[j][3] - c[x][3])**2+ (cluster[j][4] - c[x][4])**2)**0.5
	
	new_cost_function.append(cost_function)
	print 'Cost function value is :', cost_function
	temp_t=cost_function
	cost_function=0

	subscript=len(new_cost_function) - 1

	t_temp= new_cost_function[subscript] - new_cost_function[subscript-1] 
	diff=abs(t_temp)
	print 'Diff is :', diff
	if (diff  <=0.1):
		print 'center assigned for cluster1  is:', c[0]
		print 'center assigned for cluster2  is:', c[1]
		print 'center assigned for cluster3  is:', c[2]
		print 'center assigned for cluster4  is:', c[3]
		break


	c[:]=[]
	""" Finding L1 median for the four clusters and updating the centers"""

	min_val1,temp1 = HC.l1_Median(cluster1)
	c+=temp1
	
	min_val2,temp2 = HC.l1_Median(cluster2)
	c+=temp2

	min_val3,temp3 = HC.l1_Median(cluster3)
	c+=temp3
	
	min_val4,temp4 = HC.l1_Median(cluster4)
	c+=temp4
	
	min_val5,temp5 = HC.l1_Median(cluster5)
	c+=temp5
	
	#print 'Min now is :', min_val4
	print '\n After finding L1-median the centers are:'
	
	
	cluster1=[]
	cluster2=[]
	cluster3=[]
	cluster4=[]
	cluster5=[]
	
""" Writing the results to a file """	

val1=str(means_cost)
val2=str(c)
cost=str(temp_t)
f = open( '5medians_clustering.txt', 'a' )

for i in range(0,no_of_clusters):
	val1=str(i+1)
	val2=str(c[i][0])
	val3=str(c[i][1])
	val4=str(c[i][2])
	val5=str(c[i][3])
	val6=str(c[i][4])
	
	f.write (val1 + '\t'+ val2 +'\t' + val3 +'\t' + val4 +'\t' + val5 +'\t' + val6 +'\n')
f.write('Cost is :' + cost +'\n')
f.close()
	
	

