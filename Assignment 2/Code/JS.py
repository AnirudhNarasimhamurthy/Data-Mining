
def JaccardSimilarity(a,b):


	"""
	intersection_set=set()
	
	for items in a:
		for values in b:
			if values==items:
				intersection_set.add(values)
				break

	#intersection_count=len(intersection_set)
	
	union_set=set()
	
	for items in a:
		for values in b:
			if values not in union_set:
				union_set.add(values)
			if items not in union_set:
				union_set.add(items)	
			
	union_count=len(union_set)"""
	
	int_set=set(a).intersection(b)
	intersection_count=len(int_set)
	union_set=set(a).union(b)
	union_count=len(union_set)
	JaccardSimilarity= intersection_count / float(union_count)
	
	
	print 'No of common elements between the sets is :', intersection_count
	print 'No of unique elements in both the sets is :', union_count
	#print 'Jaccard Similarity is :', JaccardSimilarity
	
	return JaccardSimilarity
	
def storewords_kgrams_characters(data):

	words=[]
	doc=""
	#Splitting based on space and removing other special characters 
	for names in data:
		names=names.replace('-',' ')
		#names=names.replace('\r','')
		#names=names.replace('\n','')
		words=names.split(' ')
	#print words	
		
	#Forming a single long string without spaces of the entire document so that we can find different kgrams
	for items in words:
		doc+=items

	return names
	#return doc


def storewords_kgrams_words(data):

	words=[]
	doc=""
	#Splitting based on space and removing other special characters 
	for names in data:
		names=names.replace('-',' ')
		#names=names.replace('\r','')
		#names=names.replace('\n','')
		words=names.split(' ')
	return words


def k2_grams(doc):

	grams=""
	k2grams=set()
	for i in range(0,len(doc)-1):
		grams=doc[i]+ doc[i+1]
		k2grams.add(grams)
		
		#print 'The 2-gram is :',grams,' Was it added to the set ?',added			
	return k2grams	



def k3_grams(doc):

	grams=""
	k3grams=set()
	for i in range(0,len(doc)-2):
		grams=doc[i]+ doc[i+1] + doc[i+2]
		k3grams.add(grams)
		#print 'The 3-gram is :',grams,' Was it added to the set ?',added		
	return k3grams	


def k3_grams_words(doc):

	grams=""
	k3grams=set()
	for i in range(0,len(doc)-2):
		grams=doc[i]+" "+doc[i+1] + " "+ doc[i+2]
		k3grams.add(grams)
		#print 'The 3-gram is :',grams,' Was it added to the set ?',added		
	return k3grams	
	