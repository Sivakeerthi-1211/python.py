# add 
result = lambda a,b:a+b
print(result(2,5))

# mul
result=lambda a,b:a*b
print(result(3,4))

#square
result = lambda n : n*n
print(result(9))

#cube
result = lambda n :n*n*n
print(result(3))

# even or odd
result =lambda n : n%2==0
print(result(4))

#max and min
result = lambda a,b: a if a>b else b
print(result(2,5))

# min of three min
result = lambda a,b,c : min(a,b,c)
print(result(2,1,3))

# reverse string
result = lambda s:s[::-1]
print(result('python'))

# sort a string
l =[5,2,8,9]
l.sort(key = lambda x:x)
print(l)

# Sort List of Tuples by Second Element
students = [("Ram", 80), ("Sam", 65), ("Ravi", 90)]
result = sorted(students, key = lambda x :x[1])
print(result)
 #map 
l = [1,2,3,4,5,6]
result =list( map(lambda n : n*2,l))
print(result)
#
l= [1,2,3,4,5,6]
result =list(map(lambda n : n+5,l))
print(result)

#filter
l = [1,2,3,45,67,7,8]
result = list(filter(lambda n: n%2==0,l))
print(result)
# reduce
from functools import reduce
l = [23,54,66,77,88,99]
result = reduce(lambda x,y:x+y,l)
print(result)

# Find Length of a String
result = lambda s:len(s)
print(result("python"))


