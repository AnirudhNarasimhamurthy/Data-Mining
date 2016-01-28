library(igraph) # This loads the igraph package
dat=read.table(file.choose(),header=FALSE) # choose an adjacency matrix from a .csv file
m=as.matrix(dat) # coerces the data set as a matrix
#g=graph.adjacency(m,mode="undirected",weighted=NULL) # this will create an 'igraph object'
g=get.adjacency(graph.edgelist(as.matrix(dat), directed=FALSE))
g 

