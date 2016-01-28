import matplotlib.pyplot as plt

def scatterplot(cluster1,cluster2,cluster3,cluster4,title):

	for i in range(0,len(cluster1)):
		plt.scatter(cluster1[i][0],cluster1[i][1],color='r')

	for i in range(0, len(cluster2)):
		plt.scatter(cluster2[i][0],cluster2[i][1],color='g')
	
	for i in range(0, len(cluster3)):
		plt.scatter(cluster3[i][0],cluster3[i][1],color='b')

	for i in range(0, len(cluster4)):
		plt.scatter(cluster4[i][0],cluster4[i][1],color='DarkOrange')
	
	plt.axis([0, 1, 0, 1])
	plt.title(title,color='Blue')
	plt.show()