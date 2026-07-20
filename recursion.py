
# factorail
def fact(n):
    if n ==0:
        return 1
    return n*fact(n-1)
print(fact(5))

# sum of first 10 digits
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
print(sum(10))
# fibbonacci using recursion
# sum of two preceeding numbers - fibonnaci
def fib(n):
    if n ==0 :
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
n= 6
for i in range(n):
        print(fib(i),end =' ')
print(fib(6))
# fibbonaci of nth 
def fib(n):
    if n ==0 :
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(6))

# normal fibbonacci
def fibo(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b = b,a+b
print(fibo(6))

# by using recursion to print 1 to n numbers
def fun(n):
    if n == 1:
         return 1
    return fun (n-1)
print(fun(9))
