import matplotlib.pyplot as plt
import numpy as np

values_list=[]
val=0
yval=0
yaxis=[]
#means_cost=[268675.77180662, 264550.32610798, 1435825.16288564, 253203.324142836, 267827.195930236, 279985.753142216, 276264.547268808, 276639.89175316, 271506.564288316, 252027.42824261202, 296320.35585668, 252387.2573467, 232652.568113808, 226372.104691184, 276924.18027173996, 1329499.7063390398, 1276966.4526978, 276132.087716508, 267962.380268256, 239701.515078852]
"""means_cost=[14841.26977,
15540.30292,
15677.90027,
15867.9557,
17516.48181,
17520.39731,
17860.97041,
17893.40364,
18506.98248,
18962.65606,
19676.89383,
19799.03598,
21525.91906,
21567.6214,
21701.93811,
22772.39481,
24903.48959,
28344.15254,
37232.69863,
39909.03296]"""


means_cost=[37091.5060753,26398.4904671,14113.3432975,15824.8555782,12791.9402576,
26838.0387961,25241.1330368,24148.9990569,19129.0791407,17838.1775023,
21185.4054447,17901.8177766,15111.7177013,18027.5552369,15079.2777279,
21181.1072984,15400.637285,16409.5612512,27201.5971605,14164.5803716]



xval = np.sort(means_cost)
for i in range(0, len(means_cost)):
	yval += 1/ float(len(xval))
	yaxis.append(yval)
	
plt.plot(xval,yaxis)
plt.axis([10000, 40000, 0, 1])
plt.xlabel("3-means cost",color='red')
plt.ylabel("Percentage of our data less than or equal to the corresponding 3-means cost",color='red')
plt.title("CDF plot of k-Means ++ 3-means cost ")
#plt.autoscale(enable=True, axis=u'both', tight=False)
plt.draw()
plt.show()




"""total_sum=sum(means_cost)

for i in range(0, len(means_cost)):
	val+=means_cost[i] / float(total_sum)
	values_list.append(val)
	  

xaxis=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
plt.plot(xaxis,values_list)
plt.xlabel("Trial numbers",color='red')
plt.ylabel("3-means cost",color='red')
plt.title("Cumulative density plot")
plt.axis([0,20,0,1])
#plt.autoscale(enable=True, axis=u'both', tight=False)
plt.draw()
plt.show()"""


"""import numpy as np
import matplotlib.pyplot as plt

data=[267.605350405,263.496340745,1430.10474391,252.194545959,266.760155309,
278.870272054,275.163891702,275.53774079,270.424864829,251.023334903,
295.13979667,251.381730425,231.725665452,225.470223796,275.820896685,
1324.20289476,1271.87893695,275.031959877,266.894801064,238.746528963]


sorted_data = np.sort(data)

yvals=np.arange(len(sorted_data))/float(len(sorted_data))

plt.plot(sorted_data,yvals)



plt.xlabel("Trial numbers",color='red')
plt.ylabel("3-means cost",color='red')
plt.show()"""