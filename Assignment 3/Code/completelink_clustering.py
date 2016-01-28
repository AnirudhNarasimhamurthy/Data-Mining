
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


clink_cluster=cluster



""" Complete-link hierarchical clustering """


while len(clink_cluster)!=4:
	for i in range(0,len(clink_cluster)):
		for j in range(0,len(clink_cluster)):
			if clink_cluster[i]==clink_cluster[j]:
				continue
			else:
				tdist=HC.complete_link(clink_cluster[i],clink_cluster[j])
				if tdist <= min:
					min=tdist
					#print 'min at this point is :', min
					c_cluster1=clink_cluster[i]
					c_cluster2=clink_cluster[j]
	
	#print 'Cluster 1 going to be removed is :', c_cluster1
	#print 'Cluster 2 going to be removed is :', c_cluster2
	clink_cluster.remove(c_cluster1)
	clink_cluster.remove(c_cluster2)
	clink_cluster.append(c_cluster1 + c_cluster2)
	#print 'Clusters at this stage are :', clink_cluster
	min=99999



clink_cluster1=clink_cluster[0]
clink_cluster2=clink_cluster[1]
clink_cluster3=clink_cluster[2]
clink_cluster4=clink_cluster[3]

#print ' After clustering the clusters are given by:', cluster
print '****************************************************'
print ' The individual clusters after complete link hierarchical clustering are given by :'
print '****************************************************'
print '\n Cluster 1:', clink_cluster[0]
print '\n Cluster 2:', clink_cluster[1]
print '\n Cluster 3:', clink_cluster[2]
print '\n Cluster 4:', clink_cluster[3]

""" Plotting the clusters to check for correctness"""

title="Hierarchical clustering - Complete link"

HC.scatterplot(clink_cluster1,clink_cluster2,clink_cluster3,clink_cluster4,title)

#HC.scatterplot2(clink_cluster1,clink_cluster2,clink_cluster3,title)