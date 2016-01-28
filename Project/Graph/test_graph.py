import networkx as nx
import numpy
import pylab as plt
a=numpy.reshape(numpy.random.random_integers(0,1,size=625),(25,25))
print 'a is :', a
a=numpy.reshape(a,(25,25))
print 'a is :', a
G=nx.DiGraph()
G.add_edges_from([ (1,4) , (1,5) , (1,6) ])
nx.draw(G)
plt.show()