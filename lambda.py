#square of number
result = lambda n  : n*n
print (result(67))

# sum of two numbers
result = lambda x ,y: x +y
print(result(2,4))

#mul 
result = lambda a,b : a*b
print(result(12,5))

# map () add 5 to list of elements
L = [10,20,30,40,50]
result= list(map(lambda x : x+5,L))
print(result)

# filter ()
# even number separation
l= [1,2,3,4,5,6,7,8]
result = list(filter(lambda n :n%2==0, l))
print(result)

# lambda using if- else
# find greatest number b/w two numbers
result = lambda a,b :a>b if a>b else b
print(result(5,6))

# reduce()
# to find the  sum of l = [10,20,30,40]
from functools import reduce
l = [10,20,30,40]
result =reduce(lambda a,b:a+b,l)
print(result)

# sorted
# based on values
t =(("b",3),("c",8),('d',9),('a',2))
result = sorted (t,key = lambda x:x[1])
print(result)

#based on keys
t =(("b",3),("c",8),('d',9),('a',2))
result = sorted (t,key = lambda x:x[0] )
print(result)
# using reverse = True
t =(("b",3),("c",8),('d',9),('a',2))
result = sorted (t,key = lambda x:x[0] ,reverse = True)
print(result)
# 
t = (("d",40),("a",10),('b',2),('c',50))
result = sorted (t,key = lambda x:x[0] )
print(result)
#
t = (("d",40),("a",10),('b',2),('c',50))
result = sorted (t,key = lambda x:x[1] )
print(result)
# to sort dictionary by values
d = {'a':20,'d':5,'b':60, "c": 25}
t = tuple(d.items())
result = sorted (t,key = lambda x:x[1] )
print(result)