###simple function example(for addition)
##def add(x,y):
##    print(x+y)
##a=int(input("enter one value:"))
##b=int(input("enter one value:"))
##add(a,b)



#simple function example(for addition)
##def add(x,y):
##    z=int(x)+int(y)
##    print(z)
##    
##a=(input("enter one value:"))
##b=(input("enter one value:"))
##add(a,b)
##
##
##passing arguments at the variables    
##def add(x=2,y=3):
##    print(x+y)
##add()

#giving another value for alreaady written value)
##def add(x=5,y=20):
##    print(x+y)
##add(30,40)



##    
##def add(x=None,y=3):
##    print(x+y)
##add(30)
##
##
##
####

#with three variables
##def add(x,y,z):
##    print(x+y+z)
##add(10,20)
##
##
##def add(x,y,z):
##    print(x+y+z)
##add(10,20)


#using return
##def add(x,y):
##    return(x+x)
##
##print(add(10,20))





#inner with an inner
##def func(a,b):
##    def innerfunc(x,y):
##        def innerfunc1(c,d):
##            return c*d
##        return innerfunc1(x,y)
##    return innerfunc(a,b)
##print(func(2,3))

#another example
##def total(a,b):
##    def add(y):
##        def mul(z):
##            return z+z
##        return mul(y)*mul(y)
##    return add(a)+add(b)
##print(total(2,3))



    ###cirlce area using math module
##from math import pi
##
##def area(pi,r):
##    return (pi*r*r)
##print(area(pi,10))
##
##
##
##
###or
##
##import math
##def area(pi,r):
##    return (pi*r*r)
##print(area(math.pi,10))
##


#inner function
##def func(a,b):
##    def innerfunc(x):
##        return x*x*x
##    return innerfunc(a)+innerfunc(b)
##print(func(2,3))



#circle

##def area(pi,r):
##    return pi*r*r
##print(area(3.14,5))
##
##



##def area(pi,r):
##    return pi*r*r
##print(area(r=5,pi=3.14))







def avg(a,b,c):
      int(len1)=len(avg)
      x=(a+b+c)/len1
print(avg(1,2,3))




























