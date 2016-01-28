
point=[]
newlist=[]

with open('k_means++.txt', 'r') as inputFile:
	data1 = inputFile.readlines()
	
""" Data cleaning and pre-processing"""
for data in data1:
	
	data=data.replace('\n','')
	point_id=data.split('	')[0]
	point.append(point_id)
	

print 'Point is :', point
point=map(float,point)


for i in range(0, len(point)):
	x=1004 * point[i]
	print 'X is :', x
	newlist.append(x) 
	
print 'newlist is :', newlist	
		