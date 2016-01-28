import random
import time
from time import clock
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

#start_time = time.time()
start_time=clock()
def couponcollectors_simulation(m,n):

    numberslist={}
    trialslist=[]
    count=0
    numcount=0
    expected_sum=0
    expected_value=0

    for i in range(1,m+1):

        while 1:
            x=random.randint(1,n)
           # print "Random number is ", x
            if x not in numberslist:
                #print "Number",x, "added to the list"
                numberslist[x]=1;
                count=count+1
                numcount=numcount+1
                if numcount==n:
                 
                 #print "***************************************"
                 #print "All elements  occurs after", count, "trials"
                 #print "****************************************"
                 trialslist.append(count);
                 
                 #print "Numbers list is :", sorted(numberslist)
                 count=0;
                 numcount=0;
                 numberslist={};
                 
                 
                 break;

            else:
                count=count+1;
                
            
    """ print "Trials list is ",trialslist
   

    ## Empirical estimate of 'k' value
    expected_sum=sum(trialslist)
    print "The sum of all the trial values is",expected_sum
    expected_value=expected_sum/m

    print "Estimated number of k random trials in order to have a collision is",expected_value


 ## Finding the cdf  

    xval = np.sort(trialslist)
    check=np.arange(len(xval))
    xaxis=np.arange(0,len(xval),30)
    #print "Checking value of check is",check
    yval=np.arange(len(xval))/float(len(xval))
    plt.plot(xval,yval)
    plt.xlabel("Number of trials #k",color='red')
    plt.ylabel("Pr[All random nos in domain [n] occurs in k or fewer trials]",color='red')
    plt.title("Cumulative density plot")
    #plt.autoscale(enable=True, axis=u'both', tight=False)
    plt.draw()
    plt.show()"""


  

    ## Running time measure
    running_time=clock() - start_time
    print 'Time taken in seconds is :',running_time 
couponcollectors_simulation(2500,20000)
