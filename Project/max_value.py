with open('dblp.txt', 'r') as inputFile:
	data2 = inputFile.readlines()	
	
output=[]
	
for data in data2:
	data=data.replace('\n','')
	output+=data.split('	')	
	
#print 'Output is :', output	

output=map(int,output)
maximum=max(output)

print 'Maximum is :', maximum