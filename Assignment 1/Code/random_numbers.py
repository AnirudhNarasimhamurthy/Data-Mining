import random
import time
from time import clock


def rand_bit():
    return random.randint(0,1)


def random_numbers():

    x=[]
    y=[]
    number2=""
    for i in range(1,5):
        x.insert(i,rand_bit())

    print x 
    number=""
    number=str(x[0])+str(x[1])+str(x[2])+str(x[3])
    print 'Number is :', number
    integer_value=int(number,2)
    print integer_value

    if integer_value <= 9:
        for i in range(1,6):
            y.insert(i,rand_bit())
        print y
        number2=str(y[0])+str(y[1])+str(y[2])+str(y[3])+str(y[4])
        print 'Number 2 is ',number2
        final_no=number+number2
        print 'Final no in binary',final_no
        int_value=int(final_no,2)
        print int_value

random_numbers()
