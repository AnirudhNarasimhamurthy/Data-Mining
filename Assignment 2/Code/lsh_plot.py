
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

xvals=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
yvals=[0.00019,0.0063,0.0474,0.1860,0.4700,0.8019,0.9747,0.9964,0.9999]

plt.plot(xvals,yvals)
plt.xlabel("JS(D1,D2)",color='red')
plt.ylabel("Probability of checking d(D1,D2)",color='red')
#plt.title("Probability that the distance d(D1,D2) is checked in LSh scheme with r=20 and b=5")
plt.draw()
plt.show()