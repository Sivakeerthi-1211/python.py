# using recursion
# sum of n natural numbers
def sum(n):
    if n == 1:
        return 1
    else:
        return n +sum(n-1)
print(sum(100))

# factorial using recursion
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(10))

#fibbonaci using recursion 
def fibo(n):
    if n == 1:
        return 1
    elif n==0:
        return 0
    return fibo(n-1)+fibo(n-2)
n=5
for i in range(n):
    print(fibo(i),end =" ")
print(fibo(n))

# to find the nth fibonacci using recurssion
def fibo(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    return fibo(n-1)+fibo(n-2)
print(fibo(2))

# normal fibpnacci 
def fibo(n):
    a,b = 0,1
    for i in range(n):
        print (a,end=" ")
        a,b = b,a+b
n=5
print(fibo(5))