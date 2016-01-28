import random
import time
from time import clock
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


#start_time = time.time()
start_time=clock()
def bdayparadoxsimulation(m,n):

    numberslist=[]
    trialslist=[]
    count=0
    expected_sum=0
    expected_value=0

    for i in range(1,m+1):

        while 1:
            x=random.randrange(1,n,1)
            #print "Random number is ", x
            if x not in numberslist:
                #print "Number",x, "added to the list"
                numberslist.append(x);
                count=count+1
            else:
                trialslist.append(count);
                #print "***************************************"
                #print "Collision occurs after", count, "trials"
                #print "****************************************"
                count=0;
                numberslist=[];
                break;
            
    #print "Trials list is ",trialslist
