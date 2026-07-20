l = [ i  for i in range (1,11)]
print(l)


# square of list elements
l = [4,3,8,1,2]
lst = [ i**2 for i in l ]
print(lst)


# print even numbers form 1 to 10
lst = [ i for i in range (1,11) if i%2==0]
print(lst)


# list comprehension using if- else
l = ["even" if i % 2 == 0 else "odd" for i in range(1,11)]
print(l)


# separate even and odd by list comphresion
l = [1,2,3,4,5,6,7,8,9,10]
even = [ i for i in  l if i%2==0 ]
odd = [ i for i in   l if i %2!=0]
print(even)
print(odd)