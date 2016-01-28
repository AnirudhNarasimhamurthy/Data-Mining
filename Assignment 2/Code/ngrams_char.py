#!/usr/bin/python
import hashlib
import math
import random

n=3 #n grams

############ D1 ##########
fo = open("D1.txt", "r+")
array=[]
countDict1={}

for x in range(0, n):
    c = fo.read(1)
    if not ( c.isalpha() or c==" "):
       continue
    array.append(c);
countDict1={''.join(array[0:n]):1}

while True:
    c = fo.read(1)
    if not c:
       break
    if not ( c.isalpha() or c==" "):
       continue
    array=array[1:]
    array.append(c)
    if ''.join(array[0:n]) in countDict1:
        countDict1.update({''.join(array[0:n]): (countDict1.get(''.join(array[0:n]))) +1 })
    else:
        countDict1.update({''.join(array[0:n]): 1})


fo.close()

############ D2 ##########
fo = open("D2.txt", "r+")
array=[]
countDict2={}

for x in range(0, n):
    c = fo.read(1)
    if not ( c.isalpha() or c==" "):
       continue
    array.append(c);
countDict2={''.join(array[0:n]):1}

while True:
    c = fo.read(1)
    if not c:
       break
    if not ( c.isalpha() or c==" "):
       continue
    array=array[1:]
    array.append(c)
    if ''.join(array[0:n]) in countDict2:
        countDict2.update({''.join(array[0:n]): (countDict2.get(''.join(array[0:n]))) +1 })
    else:
        countDict2.update({''.join(array[0:n]): 1})


fo.close()

############ D3 ##########

fo = open("D3.txt", "r+")
array=[]
countDict3={}

for x in range(0, n):
    c = fo.read(1)
    if not ( c.isalpha() or c==" "):
       continue
    array.append(c);
countDict3={''.join(array[0:n]):1}

while True:
    c = fo.read(1)
    if not c:
       break
    if not ( c.isalpha() or c==" "):
       continue
    array=array[1:]
    array.append(c)
    if ''.join(array[0:n]) in countDict3:
        countDict3.update({''.join(array[0:n]): (countDict3.get(''.join(array[0:n]))) +1 })
    else:
        countDict3.update({''.join(array[0:n]): 1})


fo.close()

############ D4 ##########

fo = open("D4.txt", "r+")
array=[]
countDict4={}

for x in range(0, n):
    c = fo.read(1)
    if not ( c.isalpha() or c==" "):
       continue
    array.append(c);
countDict4={''.join(array[0:n]):1}

while True:
    c = fo.read(1)
    if not c:
       break
    if not ( c.isalpha() or c==" "):
       continue
    array=array[1:]
    array.append(c)
    if ''.join(array[0:n]) in countDict4:
        countDict4.update({''.join(array[0:n]): (countDict4.get(''.join(array[0:n]))) +1 })
    else:
        countDict4.update({''.join(array[0:n]): 1})


fo.close()
"""

print(countDict1)
print(countDict2)
print(countDict3)
print(countDict4)
print(len(countDict1))
print(len(countDict2))
print(len(countDict3))
print(len(countDict4))
"""
############ Calculate JD countDict1 ##########

print("JD(D1,D2)")
common_keys = countDict1.keys() & countDict2.keys()
union_keys = countDict1.keys() | countDict2.keys()
#dict_with_d1_values = {k: countDict1[k]+countDict2[k] for k in common_keys}
print("= 1- (",len(common_keys),"/",len(union_keys),")")
print("= ",1-(len(common_keys)/len(union_keys)))

print("JD(D1,D3)")
common_keys = countDict1.keys() & countDict3.keys()
union_keys = countDict1.keys() | countDict3.keys()
#dict_with_d1_values = {k: countDict1[k]+countDict2[k] for k in common_keys}
print("= 1- (",len(common_keys),"/",len(union_keys),")")
print("= ",1-(len(common_keys)/len(union_keys)))

print("JD(D1,D4)")
common_keys = countDict1.keys() & countDict4.keys()
union_keys = countDict1.keys() | countDict4.keys()
#dict_with_d1_values = {k: countDict1[k]+countDict2[k] for k in common_keys}
print("= 1- (",len(common_keys),"/",len(union_keys),")")
print("= ",1-(len(common_keys)/len(union_keys)))

############ Calculate JD countDict2 ##########

print("JD(D2,D3)")
common_keys = countDict2.keys() & countDict3.keys()
union_keys = countDict2.keys() | countDict3.keys()
#dict_with_d1_values = {k: countDict1[k]+countDict2[k] for k in common_keys}
print("= 1- (",len(common_keys),"/",len(union_keys),")")
print("= ",1-(len(common_keys)/len(union_keys)))

print("JD(D2,D4)")
common_keys = countDict2.keys() & countDict4.keys()
union_keys = countDict2.keys() | countDict4.keys()
#dict_with_d1_values = {k: countDict1[k]+countDict2[k] for k in common_keys}
print("= 1- (",len(common_keys),"/",len(union_keys),")")
print("= ",1-(len(common_keys)/len(union_keys)))

############ Calculate JD countDict3 ##########

print("JD(D3,D4)")
common_keys = countDict3.keys() & countDict4.keys()
union_keys = countDict3.keys() | countDict4.keys()
#dict_with_d1_values = {k: countDict1[k]+countDict2[k] for k in common_keys}
print("= 1- (",len(common_keys),"/",len(union_keys),")")
print("= ",1-(len(common_keys)/len(union_keys)))


############ Min hash D1 D2 ##########

def randomhashfn(elem,salt):
    m = hashlib.sha512()
    m.update((salt).encode('utf-8'))
    m.update(elem.encode('utf-8'))
    return (m.hexdigest())

t=4000
salt=[] 
for i in range(t):
  salt.append(str(random.randint(1,math.ceil(t*math.log(t)))))
print

#union_keys = countDict1.keys() | countDict2.keys() #randomly generates the common keys
#print("m=",len(union_keys))
#print("n1=",len(countDict1))
#print("n2=",len(countDict2))
#print(union_keys)
m1={}
m2={}
Numerator=0
for element in countDict1:
    for j in range(1,t):
        temp=randomhashfn(element,salt[j-1])
        if ( not j in m1 or temp < m1.get(j) ):
            m1[j]=temp
#print("m1=",m1);
for element in countDict2:
    for j in range(1,t):
        temp=randomhashfn(element,salt[j-1])
        if ( not j in m2 or temp < m2.get(j) ):
            m2[j]=temp
#print("m2=",m2);
for i in range(1,t):
    if ( m1[j-1] == m2[j-1] ):
        Numerator+=1
print("Ham(A,B)=",Numerator/t);



