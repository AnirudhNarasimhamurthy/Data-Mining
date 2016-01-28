import JS


#Reading the input file D1
with open('D1.txt', 'r') as inputFile:
	data1 = inputFile.readlines()
	
#Reading the input file D2
with open('D2.txt', 'r') as inputFile:
	data2 = inputFile.readlines()
			
#Reading the input file D3
with open('D3.txt', 'r') as inputFile:
	data3 = inputFile.readlines()

	
#Reading the input file D4
with open('D4.txt', 'r') as inputFile:
	data4 = inputFile.readlines()
	
doc1_kgc,doc2_kgc,doc3_kgc,doc4_kgc="","","",""
doc1_kgw,doc2_kgw,doc3_kgw,doc4_kgw="","","",""

doc1_kgc2grams,doc2_kgc2grams,doc3_kgc2grams,doc4_kgc2grams=set(),set(),set(),set()

doc1_kgc3grams,doc2_kgc3grams,doc3_kgc3grams,doc4_kgc3grams=set(),set(),set(),set()
doc1_kgw3grams,doc3_kgw3grams,doc3_kgw3grams,doc4_kgw3grams=set(),set(),set(),set()

#k3grams=set()


# Storing the words in a format which can be used for finding k-grams based on characters

doc1_kgc=JS.storewords_kgrams_characters(data1)
doc2_kgc=JS.storewords_kgrams_characters(data2)
doc3_kgc=JS.storewords_kgrams_characters(data3)
doc4_kgc=JS.storewords_kgrams_characters(data4)


doc1_kgw=JS.storewords_kgrams_words(data1)
doc2_kgw=JS.storewords_kgrams_words(data2)
doc3_kgw=JS.storewords_kgrams_words(data3)
doc4_kgw=JS.storewords_kgrams_words(data4)


# k-Grams --2-grams based on characters
doc1_kgc2grams=JS.k2_grams(doc1_kgc)
doc2_kgc2grams=JS.k2_grams(doc2_kgc)
doc3_kgc2grams=JS.k2_grams(doc3_kgc)
doc4_kgc2grams=JS.k2_grams(doc4_kgc)


# k-Grams --3-grams based on characters

doc1_kgc3grams=JS.k3_grams(doc1_kgc)
doc2_kgc3grams=JS.k3_grams(doc2_kgc)
doc3_kgc3grams=JS.k3_grams(doc3_kgc)
doc4_kgc3grams=JS.k3_grams(doc4_kgc)


# k-Grams --3-grams based on words
doc1_kgw3grams=JS.k3_grams(doc1_kgw)
doc2_kgw3grams=JS.k3_grams(doc2_kgw)
doc3_kgw3grams=JS.k3_grams(doc3_kgw)
doc4_kgw3grams=JS.k3_grams(doc4_kgw)

print' \n Results of k-Grams on different documents:'

print '------------------------------------------------'
print '	k-Grams	    |Doc1  |Doc2  |Doc3 | Doc4 |'
print '------------------------------------------------'
print ' Cardinality(chars)','|',len(doc1_kgc),'|',len(doc2_kgc),'|',len(doc3_kgc),'|',len(doc4_kgc),'|'
print ' 2-grams characters','|',len(doc1_kgc2grams),' |',len(doc2_kgc2grams),' |',len(doc3_kgc2grams),'|',len(doc4_kgc2grams),' |'
print ' 3-grams characters','|',len(doc1_kgc3grams),'|',len(doc2_kgc3grams),'|',len(doc3_kgc3grams),'|',len(doc4_kgc3grams),'|'
print '------------------------------------------------'
print ' Cardinality(words)','|',len(doc1_kgw),'|',len(doc2_kgw),'|',len(doc3_kgw),'|',len(doc4_kgw),'|'
print ' 3-grams words     ','|',len(doc1_kgw3grams),'|',len(doc2_kgw3grams),'|',len(doc3_kgw3grams),'|',len(doc4_kgw3grams),' |'
print '------------------------------------------------'


#Jaccard Similarity between different documents for 2-grams based on characters

JS12_2grams= JS.JaccardSimilarity(doc1_kgc2grams,doc2_kgc2grams)
JS13_2grams= JS.JaccardSimilarity(doc1_kgc2grams,doc3_kgc2grams)
JS14_2grams= JS.JaccardSimilarity(doc1_kgc2grams,doc4_kgc2grams)
JS23_2grams= JS.JaccardSimilarity(doc2_kgc2grams,doc3_kgc2grams)
JS24_2grams= JS.JaccardSimilarity(doc2_kgc2grams,doc4_kgc2grams)
JS34_2grams= JS.JaccardSimilarity(doc3_kgc2grams,doc4_kgc2grams)


#Jaccard Similarity between different documents for 3-grams based on characters

JS12_3grams= JS.JaccardSimilarity(doc1_kgc3grams,doc2_kgc3grams)
JS13_3grams= JS.JaccardSimilarity(doc1_kgc3grams,doc3_kgc3grams)
JS14_3grams= JS.JaccardSimilarity(doc1_kgc3grams,doc4_kgc3grams)
JS23_3grams= JS.JaccardSimilarity(doc2_kgc3grams,doc3_kgc3grams)
JS24_3grams= JS.JaccardSimilarity(doc2_kgc3grams,doc4_kgc3grams)
JS34_3grams= JS.JaccardSimilarity(doc3_kgc3grams,doc4_kgc3grams)

#Jaccard Similarity between different documents for 3-grams based on words
		
JS12_3wgrams= JS.JaccardSimilarity(doc1_kgw3grams,doc2_kgw3grams)
JS13_3wgrams= JS.JaccardSimilarity(doc1_kgw3grams,doc3_kgw3grams)
JS14_3wgrams= JS.JaccardSimilarity(doc1_kgw3grams,doc4_kgw3grams)
JS23_3wgrams= JS.JaccardSimilarity(doc2_kgw3grams,doc3_kgw3grams)
JS24_3wgrams= JS.JaccardSimilarity(doc2_kgw3grams,doc4_kgw3grams)
JS34_3wgrams= JS.JaccardSimilarity(doc3_kgw3grams,doc4_kgw3grams)

print' \n Results of Jaccard Similarity for 2-grams based on characters:'

print '------------------------------------------------'
print 'Jaccard Similarity | Doc1 | Doc2 | Doc3 | Doc4 |'
print '------------------------------------------------'
print ' Document 1	  ','|','   ',' |',JS12_2grams,'|',JS13_2grams,'|',JS14_2grams,'|'
print ' Document 2	  ','|','   ',' |','   ',' |',JS23_2grams,'|',JS24_2grams,'|'
print ' Document 3	  ','|','   ',' |','   ',' |','   ',' |',JS34_2grams,'|'
print '------------------------------------------------'

print' \n Results of Jaccard Similarity for 3-grams based on characters:'

print '------------------------------------------------'
print 'Jaccard Similarity | Doc1 | Doc2 | Doc3 | Doc4 |'
print '------------------------------------------------'
print ' Document 1	  ','|','   ',' |',JS12_3grams,'|',JS13_3grams,'|',JS14_3grams,'|'
print ' Document 2	  ','|','   ',' |','   ',' |',JS23_3grams,'|',JS24_3grams,'|'
print ' Document 3	  ','|','   ',' |','   ',' |','   ',' |',JS34_3grams,'|'
print '------------------------------------------------'


print' \n Results of Jaccard Similarity for 3-grams based on words:'

#print '3 grams for words:',doc1_kgw3grams

print '------------------------------------------------'
print 'Jaccard Similarity | Doc1 | Doc2 | Doc3 | Doc4 |'
print '------------------------------------------------'
print ' Document 1	  ','|','   ',' |',JS12_3wgrams,' |',JS13_3wgrams,' |',JS14_3wgrams,' |'
print ' Document 2	  ','|','   ',' |','   ',' |',JS23_3wgrams,'|',JS24_3wgrams,' |'
print ' Document 3	  ','|','   ',' |','   ',' |','   ',' |',JS34_3wgrams,' |'
print '------------------------------------------------'


		