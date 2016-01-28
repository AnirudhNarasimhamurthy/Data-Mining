
import matplotlib.pyplot as plt

""" Variants of hierarchical clustering and their function definitions"""

""" Single link hierarchical clustering"""

def single_link(cluster1,cluster2):
	min=999999
	for i in range(0, len(cluster1)):
		for j in range(0, len(cluster2)):
			min_dist=((cluster1[i][0] -cluster2[j][0]) ** 2 + (cluster1[i][1] -cluster2[j][1]) **2 ) **0.5
			if min_dist <= min:
				min=min_dist
	#print 'The number of combinations is :', len(cluster1) * len(cluster2)			
	return min	

""" Complete link hierarchical clustering"""
def complete_link(cluster1,cluster2):
	max=-9999
	for i in range(0, len(cluster1)):
		for j in range(0, len(cluster2)):
			max_dist=((cluster1[i][0] -cluster2[j][0]) ** 2 + (cluster1[i][1] -cluster2[j][1]) **2 ) **0.5
			if max_dist >=max:
				max=max_dist
	
	#print 'The number of combinations is :', len(cluster1) * len(cluster2)				
	return max


""" Mean link hierarchical clustering """
def mean_link(cluster1,cluster2):
	
	max=-9999
	c1x_dist,c1y_dist,c2x_dist,c2y_dist=0,0,0,0
	
	for i in range(0, len(cluster1)):
		c1x_dist+=cluster1[i][0]
		c1y_dist+=cluster1[i][1]
	for j in range(0, len(cluster2)):	
		c2x_dist+=cluster2[j][0]
		c2y_dist+=cluster2[j][1]
			
	c1x_mean=c1x_dist /float(len(cluster1))
	c1y_mean=c1y_dist /float(len(cluster1))
	c2x_mean=c2x_dist /float(len(cluster2))
	c2y_mean=c2y_dist /float(len(cluster2))
	mean_dist=((c1x_mean - c2x_mean) ** 2 + (c1y_mean - c2y_mean) **2 ) **0.5
			
	return mean_dist		
	
	
	

""" Plotting the data to check the correctness of clusters formed """

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


def scatterplot2(cluster1,cluster2,cluster3,title):

	for i in range(0,len(cluster1)):
		plt.scatter(cluster1[i][0],cluster1[i][1],color='r')

	for i in range(0, len(cluster2)):
		plt.scatter(cluster2[i][0],cluster2[i][1],color='g')
	
	for i in range(0, len(cluster3)):
		plt.scatter(cluster3[i][0],cluster3[i][1],color='b')

	
	plt.axis([0, 1, 0, 1])
	plt.title(title,color='Blue')
	plt.show()	



def lloyds_plot(cluster,phi,c,title):
	
	cluster1,cluster2,cluster3=[],[],[]
	for i in range(0,len(cluster)):
		x=phi[i]
		if x==0:
			cluster1+=[(cluster[i][0],cluster[i][1])]
		elif x==1:
			cluster2+=[(cluster[i][0],cluster[i][1])]
		elif x==2:
			cluster3+=[(cluster[i][0],cluster[i][1])]
	
	"""for i in range(0, len(c)):
		plt.scatter(c[i][0],c[i][1],s=1024,color='orange')"""
			
	for i in range(0,len(cluster1)):		
		plt.scatter(cluster1[i][0],cluster1[i][1], color='r')	
	for i in range(0,len(cluster2)):
		plt.scatter(cluster2[i][0],cluster2[i][1], color='g')
	for i in range(0,len(cluster3)):
		plt.scatter(cluster3[i][0],cluster3[i][1], color='b')
	
	plt.axis([-45, 45, -40, 45])
	plt.title(title,color='Blue')
	plt.show()	
	

def kmeansplusplus_plot(cluster,phi,c,title):
	
	cluster1,cluster2,cluster3=[],[],[]
	for i in range(0,len(cluster)):
		x=phi[i]
		if x==0:
			cluster1+=[(cluster[i][0],cluster[i][1])]
		elif x==1:
			cluster2+=[(cluster[i][0],cluster[i][1])]
		elif x==2:
			cluster3+=[(cluster[i][0],cluster[i][1])]
	
	"""for i in range(0, len(c)):
		plt.scatter(c[i][0],c[i][1],s=1024,color='orange')"""
			
	for i in range(0,len(cluster1)):		
		plt.scatter(cluster1[i][0],cluster1[i][1], color='r')	
	for i in range(0,len(cluster2)):
		plt.scatter(cluster2[i][0],cluster2[i][1], color='g')
	for i in range(0,len(cluster3)):
		plt.scatter(cluster3[i][0],cluster3[i][1], color='b')
	
	plt.axis([-45, 45, -40, 45])
	plt.title(title,color='Blue')
	plt.show()		

	
""" Minimum of 3 numbers """

def my_min(a,b,c):
	if a<= b and a<=c:
		min=a
	elif b<=a and b<=c:
		min=b
	elif c<=a and c<=b:
		min=c
	return min
				
				
""" Minimum of 4 numbers """
def median_min(a,b,c,d):
	minimum=min(a,b,c,d)
	return minimum

""" Minimum of 5 numbers """
def median5_min(a,b,c,d,e):
	minimum=min(a,b,c,d,e)
	return minimum
						

""" Finding L1 median for the given cluster """

def l1_Median(cluster):
		
	c1l1_med_dist=0	
	minimum=99999
	for j in range(0, len(cluster)):
		for i in range(0, len(cluster)):
			if(cluster[i]==cluster[j]):
				continue
			else:	
				c1l1_med_dist+=((cluster[j][0]- cluster[i][0])**2 + (cluster[j][1] - cluster[i][1])**2 +(cluster[j][2] - cluster[i][2])**2 + (cluster[j][3] - cluster[i][3])**2+ (cluster[j][4] - cluster[i][4])**2)*0.5
			
		if  c1l1_med_dist < minimum:
			#print 'Dist is :', c1l1_med_dist
			minimum=c1l1_med_dist
			temp=[(cluster[j][0],cluster[j][1],cluster[j][2],cluster[j][3],cluster[j][4])]
		c1l1_med_dist=0
		
	#print 'Minimum is :', minimum
	#print 'C now is :', temp
	
	return minimum,temp						
						