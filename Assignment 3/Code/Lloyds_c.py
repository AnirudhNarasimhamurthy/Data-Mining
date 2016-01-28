import matplotlib.pyplot as plt
import HC
import pickle

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
subset1,subset2,subset3=[],[],[]
indexes1,indexes2,indexes3=[],[],[]
means_cost=0
c0_x,c0_y,c1_x,c1_y,c2_x,c2_y=0,0,0,0,0,0
c0_center, c1_center,c2_center=0,0,0
centers_average=[]
centers_count=[]
means_dist=0
centers_list=[]
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
	
"""kmeans_output=[(-19.0748, -8.536), (17.69664852, -11.09156605),(-20.82806376, -6.69717012)],
[(-19.0748, -8.536), (21.1856984, -10.72501219), (-19.65417726, -8.211477352)],
[(-19.0748, -8.536), (-18.91841383, -7.185415379), (-19.65417726, -8.211477352)],
[(-19.0748, -8.536), (23.84763233, -8.82214252), (-17.37534526, -9.134230943)],
[(-19.0748, -8.536), (-21.19373865, -13.20813852), (26.48638347, -7.798021124)],
[(-19.0748, -8.536), (20.98059136, -11.7393288), (-15.35133402, -6.943039921)],
[(-19.0748, -8.536), (-19.88994284, -8.550733987), (22.77209724, -11.00912555)],
[(-19.0748, -8.536), (20.71204687, -11.58808224), (-16.38603445, -7.205324413)],
[(-19.0748, -8.536), (22.0108, -10.9737), (-21.55599843, -8.968839013)],
[(-19.0748, -8.536), (21.21060698, -9.901650142), (-16.7464568, -4.865147852)],
[(-19.0748, -8.536), (26.47908199, -10.10558625), (-19.88994284, -8.550733987)],
[(-19.0748, -8.536), (21.21060698, -9.901650142), (-19.28529157, -13.21985521)],
[(-19.0748, -8.536), (22.71382947, -7.709164073), (-16.73449977, -6.379830594)],
[(-19.0748, -8.536), (22.79469945, -6.976994888), (-22.22948053, -12.69644013)],
[(-19.0748, -8.536), (20.71204687, -11.58808224), (-20.00417586, -8.269751735)],
[(-19.0748, -8.536), (-21.79875609, -8.32260884), (-16.8768945, -9.048859779)],
[(-19.0748, -8.536), (-17.34306487, -7.516827343), (-16.64916083, -4.672177852)],
[(-19.0748, -8.536), (22.77209724, -11.00912555), (-19.5530913, -9.584532025)],
[(-19.0748, -8.536), (26.48638347, -7.798021124), (-19.0162303, -9.627969052)],
[(-19.0748, -8.536), (-18.35149093, -7.805921311), (22.24432794, -8.562356865)]]"""

kmeans_output=[[(-19.0748, -8.536),(27.90222182, -9.059452238),(11.57067451, 22.66727805)],
[(-19.0748, -8.536),(7.101926809, 19.74838441),(24.41273839, -8.643681766)],
[(-19.0748, -8.536),(22.82378427, -10.85431086),(13.81771924, 21.10374953)],
[(-19.0748, -8.536),(20.67631286, -10.68194926),(14.46736499, 21.33656992)],
[(-19.0748, -8.536),(21.9170255, -10.87966211),(12.45604826, 19.85666834)],
[(-19.0748, -8.536),(23.24556797, -6.253570524),(13.78850398, 17.92526179)],
[(-19.0748, -8.536),(13.1365447, 17.36962924),(17.69664852, -11.09156605)],
[(-19.0748, -8.536),(10.70949951, 15.42318515),(19.12725042, -12.37738888)],
[(-19.0748, -8.536),(13.81771924, 21.10374953), (24.8033178, -9.492314322)],
[(-19.0748, -8.536),(19.64248637, -11.57580407), (14.82835236, 19.01391508)],
[(-19.0748, -8.536),(20.75226192, -10.05593427),(13.65906964, 24.46717901)],
[(-19.0748, -8.536), (13.58499272, 20.52568697),(23.87925343, -8.684086277) ],
[(-19.0748, -8.536),(11.31209739, 18.98044749),(21.00683444, -12.33589101) ],
[(-19.0748, -8.536),(22.81051543, -13.80295414),(12.03809816, 18.78797292) ],
[(-19.0748, -8.536),(13.70633953, 19.91530597),(23.05060035, -12.51886147) ],
[(-19.0748, -8.536),(13.52864688, 19.26926304),(18.37302084, -10.57981669) ],
[(-19.0748, -8.536),(12.56638318, 19.82895821),(19.99936759, -10.97303185) ],
[(-19.0748, -8.536),(13.57111799, 17.29652831),(23.55254848, -9.451680864) ],
[(-19.0748, -8.536),(11.37964761, 17.68770314),(26.84039676, -9.960570837) ],
[(-19.0748, -8.536),(23.10847486, -10.2003253),(12.44177011, 20.92152635) ]]

for k in range(0,len(kmeans_output)):
	c=[]
	x_temp=kmeans_output[k]
	c=kmeans_output[k]
	print 'c is :', x
	phi=[]

	
	for j in range(0, len(cluster)):
		phi.append(0)

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

		for i in range(0, no_of_clusters):
			cx=centers_average[i][0]/float(centers_count[i])
			cy=centers_average[i][1] /float(centers_count[i])
			c+=[(cx,cy)]	
	
		centers_average[:]=[]
		centers_count[:]=[]
	
		if (set(b).intersection(c) == set(c)):
			print 'The centers are :', c
			print 'Counter is :', counter
			break

	for j in range(0, len(cluster)):
		x=phi[j]
		three_means_cost+=(c[x][0]-cluster[j][0])**2 + (c[x][1]-cluster[j][1]) **2


	#three_means_cost=means_dist / float(len(cluster))

	print '3 means cost is :', three_means_cost	
	
	
	""" Plotting the data """

	title="Output of Llyods algorithm when the centers correspond to output of k-Means++"
	HC.lloyds_plot(cluster,phi,c,title)	
	
	""" Writing the data to the file"""
	val1=str(three_means_cost)
	val2=str(c)
	#val3=str(x_temp)
	f = open( 'Lloyds_k_means++++.txt', 'a' )
	f.write (val1 + '\t'+ val2 + '\n' )
	f.close()

	three_means_cost=0