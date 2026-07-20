def message():
    print("hello keerthi")
message()
#
print("start")
def message():
    print("heelo")
print("middle")
message()
print("end")

 # calling function  with arg and return
def add(a,b):
    return a+b
print(add(10,20))
# calling function with return with out arg
def message():
    return("congrats welcome to accenture")
k = message()
print(k)
# with arg with out return 
def add(a,b):
    c = a +b 
    print(c)
add(10,20)
#with out arg and with out return
def sum():
    a = 10
    b =30
    c = a+b
    print(c)
sum()

#
def mail():
    print(" congrats welcome to accenture")
mail()

# without parameters
def geet ():
    return ('welcome to new beging')
print(geet())

# function to find the square of number
def square(n):
    return n*n
print(square(4))

# function to check even or odd
def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(even_odd(9))
print(even_odd(10))

# function for the factorial
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
print(fact(5))

# function with default parameter
def geet(name='guest'):
    return('hello' , name)
print(geet())
print(geet("keerthi"))

# To write function  for even and odd in list
def even_odd(n):
    even = []
    odd  = []
    for i in n:
        if i %2==0:
            even.append(i)
        else:
            odd.append(i)
    return [even,odd]
lst=[2,5,6,10,44,556,78]
print(even_odd(lst))

# default parameters
def message (country= 'india' ):
    print(f'my country name is',country )
message()
message("usa")


def message():
    return 'hello world'
print("helo codegnan")
message()
#
def message():
    print('hello codegnan')
    print('hello 58')
    return 'hello world'
print(message())

#
def message():
    print('hello codegnan')
    print('hello 58')
    return 'hello world'
print(message())
print()
print(message())

# types of arguments
 #postional arguments
def message(name,age,salary):
    print("my name is :",name)
    print("my age is:",age)
    print('me salary:',salary)
message('keerthi',21,60000)

# kw arguments
def message (name,age,salary):
    print("my name is :",name)
    print("my age is:",age)
    print('me salary:',salary)
message(salary=60000,name='keerthi',age=21)

# variable length positions arguments(*kargs)
#def add(*b):
    #return sum(b)
#print(add(10,20))

# **Kwargs
def message(**b):
    print(b)
message(name="keerthi",age=25)

#mix postional and variable 
#case -1
def message(a,b,*i):
    print(a,b,i)
message(1,99)
#case - 2
def message(a,b,c,*i):
    print(a,b,c,i)
message(1,3,344,5556,6666,777)

# case -3
def message(a,b,c,*i):
    print(a,b,c,i)
message('eerla',"siva","keerthi","refferal")

# first non repeating character in a string
# i/p : aaabbc
# o/p : c
def non_repeating_character(s):
    for ch in s:
        if s.count(ch)==1:
            return ch
    return "no non_repeating_character"
s = "aaabbc"
print(non_repeating_character(s))



