
import matplotlib.pyplot as plt
import HC


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
	cluster+=[[(x_coord[i],y_coord[i])]]


""" Making copies of the cluster list for the 3 variants """

slink_cluster=cluster
clink_cluster=cluster
meanlink_cluster=cluster


""" Single-link Hierarchical clustering """

while len(slink_cluster)!=4:
	for i in range(0,len(slink_cluster)):
		print 'Len is now :', len(slink_cluster)
		for j in range(0,len(slink_cluster)):
			if slink_cluster[i]==slink_cluster[j]:
				continue
			else:
				tdist=HC.single_link(slink_cluster[i],slink_cluster[j])
				print 'tdist here is:', tdist
				if tdist <= min:
					min=tdist
					print 'min at this point is :', min
					index=j
					c_cluster1=slink_cluster[i]
					c_cluster2=slink_cluster[j]
					print' Points are :', c_cluster1 ,'and :', c_cluster2
	
	print 'Cluster 1 going to be removed is :', c_cluster1
	print 'Cluster 2 going to be removed is :', c_cluster2
	slink_cluster.remove(c_cluster1)
	slink_cluster.remove(c_cluster2)
	#slink_cluster.insert(index,c_cluster1 + c_cluster2)
	slink_cluster.append(c_cluster1 + c_cluster2)
	print 'Clusters at this stage are :', slink_cluster
	min=999999


slink_cluster1=slink_cluster[0]
slink_cluster2=slink_cluster[1]
slink_cluster3=slink_cluster[2]
slink_cluster4=slink_cluster[3]

#print ' After clustering the clusters are given by:', cluster
print '****************************************************'
print ' The individual clusters after single link hierarchical clustering are given by :'
print '****************************************************'
print '\n Cluster 1:', slink_cluster[0]
print '\n Cluster 2:', slink_cluster[1]
print '\n Cluster 3:', slink_cluster[2]
print '\n Cluster 4:', slink_cluster[3]

""" Plotting the clusters to check for correctness"""

title="Hierarchical clustering - Single link"

HC.scatterplot(slink_cluster1,slink_cluster2,slink_cluster3,slink_cluster4,title)


#HC.scatterplot2(slink_cluster1,slink_cluster2,slink_cluster3,title)





		