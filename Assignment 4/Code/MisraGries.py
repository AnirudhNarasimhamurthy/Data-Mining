""" Reading the input file S1 """
with open('S1.txt', 'r') as inputFile:
	data1 = inputFile.readlines()


""" Reading the input file S2 """

with open('S21.txt', 'r') as inputFile:
	data2 = inputFile.readlines()	
	
""" Data pre-processing for file S1 """

for data in data1:
	
	data=data.replace("'","")
	data=data.strip()
	stream1=data.split(' ')
	
""" Data pre-processing for file S2 """	
	
for data in data2:
	
	data=data.replace("' ","")
	data=data.strip()
	stream2=data.split(' ')	

print 'Stream 1 first character is :', stream1[0]	
#print 'Stream1 is :', stream1 
print 'Stream 2 first character is :', stream2[0]	
#print 'Stream2 is :', stream2




def misra_gries(stream):

	k=10
	counter=[0] * (k-1)
	#print 'Counter is :', counter
	L=[None] * (k-1)
	#print 'Label is :', L

	a=len(L)
	tracking=0
	check=0
	modL=0

	print 'Length of stream is :', len(stream)

	for i in range(0, len(stream)):
		#print 'stream[i] is :', stream[i]
		if (stream[i] in L):
			for j in range(0,len(L)):
				if stream[i]==L[j]:
					counter[j]=counter[j]+1
				
		else:
	
			for j in range(0,len(L)):
				if (L[j]== None):
					modL=1
		
			if modL > 0:	
				for j in range(0,len(L)):
					if(L[j]== None):
						counter[j]=1
						L[j]=stream[i]	
						break
			else:
		
				for j in range(0, k-1):
					counter[j]=counter[j]-1
			
		for j in range(0, k-1):
			if counter[j] <= 0 :#and L[j] != None:
				L[j]=None
				
		
		modL=0				

		#print 'L is now :', L
		#print 'Counter is now :', counter
		#print 'Tracking is :', tracking
	

	return L,counter


L1,counter1=misra_gries(stream1)
print 'Final Counter for Stream 1 is :', counter1
print 'Final location/label for Stream 1 is :', L1


L2,counter2=misra_gries(stream2)
print 'Final Counter for Stream 2 is :', counter2
print 'Final location/label for Stream 2 is :', L2

								