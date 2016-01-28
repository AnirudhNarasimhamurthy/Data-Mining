
import matplotlib.pyplot as plt
import HC


x_coord=[]
y_coord=[]
point=[]	
cluster=[]
min=999999
max=-99999
mean=9999
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


""" Mean-link Hierarchical clustering """

while len(meanlink_cluster)!=4:
	for i in range(0,len(meanlink_cluster)):
		for j in range(0,len(meanlink_cluster)):
			if meanlink_cluster[i]==meanlink_cluster[j]:
				continue
			else:
				tdist=HC.mean_link(meanlink_cluster[i],meanlink_cluster[j])
				if tdist <= mean:
					mean=tdist
					#print 'min at this point is :', min
					c_cluster1=meanlink_cluster[i]
					c_cluster2=meanlink_cluster[j]
	
	meanlink_cluster.remove(c_cluster1)
	meanlink_cluster.remove(c_cluster2)
	meanlink_cluster.append(c_cluster1 + c_cluster2)
	mean=999


meanlink_cluster1=meanlink_cluster[0]
meanlink_cluster2=meanlink_cluster[1]
meanlink_cluster3=meanlink_cluster[2]
meanlink_cluster4=meanlink_cluster[3]

#print ' After clustering the clusters are given by:', cluster
print '****************************************************'
print ' The individual clusters after mean link hierarchical clustering are given by :'
print '****************************************************'
print '\n Cluster 1:', meanlink_cluster[0]
print '\n Cluster 2:', meanlink_cluster[1]
print '\n Cluster 3:', meanlink_cluster[2]
print '\n Cluster 4:', meanlink_cluster[3]

""" Plotting the clusters to check for correctness"""

title="Hierarchical clustering - Mean link"

HC.scatterplot(meanlink_cluster1,meanlink_cluster2,meanlink_cluster3,meanlink_cluster4,title)






		