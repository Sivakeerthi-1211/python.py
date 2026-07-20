# squares of numbers in list using dict comphresion
l =[1,2,3,4,5,6,7,8,9,10]
d = { x :x *x for x in l}
print(d)

# even sqaure 
l = [1,2,3,4,5,6,7,8,9,10]
d = { x : x*x for x in l if x%2 ==0}
print(d)

# to print even and odd
l =  [1,2,3,4,5,6,7,8,9,10]
d ={x:"even"if x%2 ==0 else"odd" for x in l}
print(d)

# 
