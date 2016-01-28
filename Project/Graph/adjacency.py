""" with open('sample.txt', 'r') as inputFile:
	data1 = inputFile.readlines()


from_node=[]
to_node=[]
	
for data in data1:
	
	#data=data.replace("'","")
	data=data.strip()
	
	input_data1=data.split('	')[0]
	input_data2=data.split('	')[1]
	from_node.append(input_data1)
	to_node.append(input_data2)

print 'Data is :', input_data		

from_node=map(float,from_node)
to_node=map(float,to_node)  """


  

