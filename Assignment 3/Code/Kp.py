from scipy.spatial import distance
import random
import math


clusterCenter={}
clusterLabel={}
dictA={}

def createHashMap(lines):
    for i in lines:
        tokens=i.split("\t")
        indexStr=" ".join(tokens[0:1])
        xCoordStr=" ".join(tokens[1:2])
        yCoordStr=" ".join(tokens[2:3])
        indexInt=int(indexStr)
        xCoordFloat=float(xCoordStr)
        yCoordFloat=float(yCoordStr)
        dictA[indexInt]=(xCoordFloat,yCoordFloat)
    return dictA


def findNewCenterKpp(dictA,k):
    summingList=[]
    #clusterCenter[1]=dictA[1]

    for j in range(1,len(dictA)+1):
        dist=distance.euclidean(clusterCenter[1],dictA[j])
        distSquared=dist*dist
        summingList.append(distSquared)
    summation=sum(summingList)
    randomNumber=random.uniform(0,summation)
    totalDist=0

    for j in dictA:
        dist=distance.euclidean(dictA[j],clusterCenter[1])
        totalDist=totalDist+(dist*dist)
        if(totalDist>=randomNumber):
            clusterCenter[j]=dictA[j]
            return j


def creatingClustersUsingKpp(dictA,k):
    clusterCenter[1]=dictA[1]
    MaxInC1=0
    MaxInC2=0
    SquaredDistancesList1=[]
    SquaredDistancesList2=[]
    currentDistance=0
    TotalDistance={}
    RandomNumber={}
    newCenter=findNewCenterKpp(dictA,k)
    cluster3=0

    for index in dictA:
        clusterLabel[index]=1

    for j in dictA:
        distFromc1=distance.euclidean(dictA[j],clusterCenter[1])
        distFromc2=distance.euclidean(dictA[j],clusterCenter[newCenter])
        if(distFromc1 > distFromc2):
            clusterLabel[j]=newCenter

    for point in clusterLabel:
        if(clusterLabel[point]==1):
            distC1=distance.euclidean(dictA[point],clusterCenter[1])
            distSquared=distC1*distC1
            SquaredDistancesList1.append(distSquared)

        elif (clusterLabel[point]==newCenter) :
            distC2=distance.euclidean(dictA[point],clusterCenter[newCenter])
            distSquared=distC2*distC2
            SquaredDistancesList2.append(distSquared)

        TotalDistance[1]=sum(SquaredDistancesList1)
        RandomNumber[1]=random.uniform(0,TotalDistance[1])

        TotalDistance[2]=sum(SquaredDistancesList2)
        RandomNumber[2]=random.uniform(0,TotalDistance[2])

    for point in clusterLabel:
        if(clusterLabel[point]==1):
            dist=distance.euclidean(dictA[point],clusterCenter[1])
            currentDistance=currentDistance+(dist*dist)
            if(currentDistance>RandomNumber[1]):
                MaxDistInC1=currentDistance
                MaxPointInC1=point
                break

    for point in clusterLabel:
        if(clusterLabel[point]==newCenter):
            dist=distance.euclidean(dictA[point],clusterCenter[newCenter])
            currentDistance=currentDistance+(dist*dist)
            if(currentDistance>RandomNumber[2]):
                MaxDistInC2=currentDistance
                MaxPointInC2=point
                break

    if(MaxDistInC1 > MaxDistInC2):
        clusterCenter[MaxPointInC1]=dictA[MaxPointInC1]
        cluster3=MaxPointInC1

    elif (MaxDistInC2 > MaxDistInC1):
        clusterCenter[MaxPointInC2] = dictA[MaxPointInC2]
        cluster3=MaxPointInC2

    for j in dictA:
        dist1=distance.euclidean(dictA[j],clusterCenter[1])
        dist2=distance.euclidean(dictA[j],clusterCenter[newCenter])
        dist3=distance.euclidean(dictA[j],clusterCenter[cluster3])
        minimum=min(dist1,dist2,dist3)
        if(minimum==dist1):
            clusterLabel[j]=1
        elif(minimum==dist2):
            clusterLabel[j]=newCenter
        elif(minimum==dist3):
            clusterLabel[j]=cluster3
            
    cost=0
    for j in dictA:
        if(clusterLabel[j]==1):
            #print clusterLabel[j]
            dista1=distance.euclidean(dictA[j],clusterCenter[1])
            cost=cost+math.pow(dista1,2)
            #print cost
    for j in dictA:
        if (clusterLabel[j]==newCenter):
            dista2=distance.euclidean(dictA[j],clusterCenter[newCenter])
            cost=cost+math.pow(dista2,2)
            #print clusterCenter[newCenter]
    for j in dictA:
        if(clusterLabel[j]==cluster3):
            dista3=distance.euclidean(dictA[j],clusterCenter[cluster3])
            cost=cost+math.pow(dista3,2)
            #print dista3
                

    print clusterCenter
    
    print cost
    return clusterCenter


def main():
    k=3
    file_object=open('C2.txt')
    lines=file_object.readlines()
    dictA=createHashMap(lines)
    clusterCenter=creatingClustersUsingKpp(dictA,k)
 


   
if __name__=="__main__":
    main()
