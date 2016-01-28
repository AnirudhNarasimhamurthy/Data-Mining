import hashlib, sys
import JS
import random, math
from time import clock

#Reading the input file D1
with open('D1.txt', 'r') as inputFile:
	data1 = inputFile.readlines()
	
#Reading the input file D2
with open('D2.txt', 'r') as inputFile:
	data2 = inputFile.readlines()
			
#Reading the input file D3
with open('D3.txt', 'r') as inputFile:
	data3 = inputFile.readlines()

	
#Reading the input file D4
with open('D4.txt', 'r') as inputFile:
	data4 = inputFile.readlines()    

doc1_kgc,doc2_kgc,doc3_kgc,doc4_kgc="","","",""
doc1_kgw,doc2_kgw,doc3_kgw,doc4_kgw="","","",""

    
doc1_kgc=JS.storewords_kgrams_characters(data1)
doc2_kgc=JS.storewords_kgrams_characters(data2)
doc3_kgc=JS.storewords_kgrams_characters(data3)
doc4_kgc=JS.storewords_kgrams_characters(data4)
 
 # k-Grams --3-grams based on characters

doc1_kgc3grams=JS.k3_grams(doc1_kgc)
doc2_kgc3grams=JS.k3_grams(doc2_kgc)
doc3_kgc3grams=JS.k3_grams(doc3_kgc)
doc4_kgc3grams=JS.k3_grams(doc4_kgc)



start_time= clock()
	
def randomhashfn(elem,salt):
    m = hashlib.sha1()
    print 'm is :', m
    m.update((salt).encode('utf-8'))
    m.update(elem.encode('utf-8'))
    #print 'Value generated is:', m.hexdigest()
    return (m.hexdigest())



doc1=doc1_kgc3grams
doc2=doc2_kgc3grams
doc3=doc3_kgc3grams
doc4=doc4_kgc3grams

m1={}
m2={}
Numerator=0
salt=[]
c=0
#t=10 #0.7 7/10 0.5 5/10
#t=50  #0.72 36/50
#t=100 #0.71 71/100  0.64 64/100
#t=250 #0.692 168/250 173/250
#t=500 #0.7 350/500 0.71 355/500
t=1000 #0.682 682/1000
for i in range(1,t):
  	#print 'Value of i is:',i,'Salt :', math.ceil(t*math.log(t))
  	salt.append(str(random.randint(1,math.ceil(t*math.log(t)))))
  	c=c+1
  	#salt.append(str(math.ceil(t*math.log(t)) + c))

#print 'Salt is:',salt

for element in doc1:
     for j in range(1,t):
        temp=randomhashfn(element,salt[j-1])
        #print 'm1.get() gives :', m1.get(j)
        if (not j in m1 or temp < m1.get(j)):
            m1[j]=temp
			#print("m1=",m1);"""

for element in doc2:
    for j in range(1,t):
        temp=randomhashfn(element,salt[j-1])
        if (not j in m2 or temp < m2.get(j)):
            m2[j]=temp
			#print("m2=",m2);

for i in range(1,t):
    if ( m1[i] == m2[i] ):
        #print 'M1:' ,m1[i], 'M2 :', m2[i]
        Numerator+=1
    else:
    	#print 'Not same:', 'M1:' ,m1[i], 'M2 :', m2[i] 
    	a=1  
print 'Numerator is :', Numerator    
similarity=Numerator/float(t)    
print("Ham(A,B)=",Numerator/float(t))	
total_time= clock()- start_time
print ' Time taken in seconds is :', total_time

