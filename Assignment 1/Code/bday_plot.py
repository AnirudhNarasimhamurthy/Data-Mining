
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

#m=300
#yvals=[0.02365,0.03525,0.036151,0.04636,0.065038,0.10533,0.140456,0.199561,0.332895,0.379241,0.428203,0.47349]

#m=1000
#yvals=[0.084951,0.098292,0.136454,0.14707,0.198177,0.313431,0.467365,0.679867,1.057523,1.283208,1.477823,1.580242]

#m=3000
yvals=[0.30869,0.316529,0.364814,0.45203,0.639772,1.150114,1.407348,1.950634,3.180289,3.705318,4.382941,4.600287]

#m=10000
#yvals=[0.83914,1.061329,1.28111,1.525068,2.021546,3.453782,4.811616,6.865197,10.521872,12.545527,14.811142,15.869707]



xvals=[3000,5000,7000,10000,20000,50000,100000,200000,500000,700000,900000,1000000]
plt.plot(xvals,yvals)
plt.xlabel("Domain size n",color='red')
plt.ylabel("Run time in seconds",color='red')
plt.title("Plot of run time and n for m=3,000")
#plt.autoscale(enable=True, axis=u'both', tight=False)
#plt.grid(False)
#plt.xlim(0,300)
#plt.ylim(0,1.0)
plt.draw()
plt.show()
