import math
	
t=100
tow=0.4
b=-math.log(100,tow)	
b=round(b)
print 'Choice of b is:',b

r=t/b
r=round(r)
print 'Choice of r is:',r


r=20
b=5	

s=0.6957
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (r,b) (100, 1 )value of f(',s, ') is :', f

	
s=0.4631
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (r,b) (100, 1 )value of f(',s, ') is :', f

	
s=0.3984
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (r,b) (100, 1 )value of f(',s, ') is :', f

s=0.3864
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (r,b) (100, 1 )value of f(',s, ') is :', f


s=0.3529
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (r,b) (100, 1 )value of f(',s, ') is :', f

s=0.3522
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (r,b) (100, 1 )value of f(',s, ') is :', f




	
"""r=50
b=2	
s=0.4
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (50,2) value of f(',s, ') is :', f


	
r=25
b=4	
s=0.4
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (25,4) value of f(',s, ') is :', f	

	
r=20
b=5	
s=0.4
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (20,5) value of f(',s, ') is :', f	

	
r=10
b=10	
s=0.4
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (10,10) value of f(',s, ') is :', f	


r=5
b=20	
s=0.4
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (5,20) value of f(',s, ') is :', f	




r=4
b=25	
s=0.4
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (4,25) value of f(',s, ') is :', f	


r=2
b=50	
s=0.4
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (2,50) value of f(',s, ') is :', f	


r=1
b=100	
s=0.4
f= 1-math.pow((1-math.pow(s,b)),r)
print 'The (1,100) value of f(',s, ') is :', f	"""
