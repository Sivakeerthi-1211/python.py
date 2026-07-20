# square of list in number
lst = [1,2,3,4,5,6,7,8,9,10]
d = {i:i*i for i in lst}
print(d)

# even number
d = {i:i**2 for i in range (1,11) if i%2==0}
print(d)

# to print even and odd
lst = [1,3,4,5,6,7,8,9]
d = {i:'even' if i%2==0 else 'odd'for i in lst}
print(d)

# postive and negative
lst =[1,-3,5,-6,7]
d ={i:'postive'if i>0 else "negative" for i in lst}
print(d)