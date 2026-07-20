# to print number fron 1 to 11 using list comphresion
l = [i for i in range(1,11)]
print(l)

# square of lists
lst = [1,2,3,4,54,55,77]
l = [i*i for i in  lst]
print(l)

# to print even number 
lst = [ 1,2,3,4,5,6,7,8,9,10]
l = [i for i in lst if i%2==0]
print(l)
 # 
l = [ i for i in range(1,11) if i%2==0]
print(l)

# print even or odd 
l = [' even 'if i%2==0 else'odd'for i in range(1,12)]
print(l)

# separate even and odd list by using list comphresion
l = [1,2,3,4,5,6,7,8,9,10]
even = [ i for i in l if i%2==0]
odd = [ i for i in l if i%2!=0]
print(even,end = " ")
print(odd)

# to print postive or negative
lst = [1,-2,3,-3,8,-9]
l = [ 'postive' if i>0 else'odd' for i in lst]
print(l)

# 
lst =[1,-2,3,-3,8,-9]
postive = [ i for i in lst if i>0]
negative = [ i for i in lst if i<0]
print(postive)
print(negative)

# normal
l =[i for i in range(1,11)]
print(l)
#square
l = [i*i for i in range(1,11)]
print(l)
#even 
lst = [1,2,3,4,5,6,7,8,9,10]
l = [i for i in lst if i%2==0]
print(l)
# even or odd
l=['even'if i%2==0 else 'odd'for i in range(1,11)]
print(l)
#upper
lst =['keerthi','siva']
l = [name.upper()for name in lst]
print(l)