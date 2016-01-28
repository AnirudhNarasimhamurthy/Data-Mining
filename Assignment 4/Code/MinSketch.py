import random


""" Reading the input file S1 """
with open('S1.txt', 'r') as inputFile:
	data1 = inputFile.readlines()


""" Reading the input file S2 """

with open('S2.txt', 'r') as inputFile:
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



def all_primes(start, end):
        return list(sorted(set(range(start,end+1)).difference(set((p * f) for p in range(2, int(end ** 0.5) + 2) for f in range(2, (end/p) + 1)))))


def count_MinSketch(stream1):

	k=10
	t=5
	m=10
	maxval=0
	a=[]
	b=[]
	p=[]
	s1_alist,s1_blist,s1_clist,s1_wlist=[],[],[],[]
	s2_alist,s2_blist,s2_clist,s2_wlist=[],[],[],[]
	

	input_stream=['a','b','c','w']
	counter=[[ 0 for x in range(k)] for x in range(t)]
	#counter2=[[ 0 for x in range(k)] for x in range(t)]
	
	print 't is :', t
	print 'Length of stream is :', len(stream1)

	""" Finding the maximum ascii value in the stream1"""
	for i in range(0, len(stream1)):
		val=ord(stream1[i])
		#print 'Val is :', val
		if val >maxval:
			maxval=val


	p_list=all_primes(maxval, 2*maxval)


	for i in range(0,t):

		p_element=random.choice(p_list)
		p.append(p_element)
	

	for i in range(0, t):
		a_list=random.randint(1,p[i]-1)
		b_list=random.randint(0,p[i])
		a.append(a_list)
		b.append(b_list)


	for i in range(0, len(stream1)):
		for j in range(0, t):		
			k= ((a[j]* ord(stream1[i]) + b[j]) % p[j]) % m
			#print 'K value is :', k
			counter[j][k]=counter[j][k] +1

	print 'Counter is :', counter			

	for i in range(0,len(input_stream)):
		for j in range(0,t):
			if i==0:
				k= ((a[j]* ord(input_stream[i]) + b[j]) % p[j]) % m
				s1_alist.append(counter[j][k])
			elif i==1:
				k= ((a[j]* ord(input_stream[i]) + b[j]) % p[j]) % m
				s1_blist.append(counter[j][k])
			elif i==2:	
				k= ((a[j]* ord(input_stream[i]) + b[j]) % p[j]) % m
				s1_clist.append(counter[j][k])
			elif i==3:
				k= ((a[j]* ord(input_stream[i]) + b[j]) % p[j]) % m
				s1_wlist.append(counter[j][k])

				
				
			
			
	print 'alist for Stream  is :', s1_alist,
	print '\nblist for Stream  is :', s1_blist,
	print '\nclist for Stream  is :', s1_clist,
	print '\nwlist for Stream  is :', s1_wlist,

	print '\n==================================='

	print '\n==================================='

	print 'Estimated count of a for Stream:', min(s1_alist)
	print 'Estimated count of b for Stream :', min(s1_blist)
	print 'Estimated count of c for Stream:', min(s1_clist)
	print 'Estimated count of w for Stream:', min(s1_wlist)
	
	print '\n==================================='


	return min(s1_alist),min(s1_blist),min(s1_clist)


""" Streams S1 and S2 """
s1a_estimate,s1b_estimate,s1c_estimate=count_MinSketch(stream1)
s1a_estimate,s1b_estimate,s1c_estimate=count_MinSketch(stream2)




								