def even_odd(n):
    even = []
    odd  =[]
    for i in n :
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return[even,odd]
lst = [11,12,13,14,15,16]
print(even_odd(lst))
    
# 
def non_repeating(s):
    for ch in s:
        if s.count(ch)==1:
            return ch
    return "no_non_repeative"
s="aabbc"
print(non_repeating(s))

#
#default parameter
def message(name='guest'):
    print("hello",name)
message()
message('keerthi')


#default parameter
def message(name="guest"):
    print("hello",name)
message()
message("keerthi")

# positional arguments
def add (a,b):
    c = a+b
    print(c)
add(10,30)

#keyword arguments
def information(name,age,salary):
    print("name",name)
    print('age',age)
    print('salary',salary)
information(name='keerthi',age=20,salary=60000)

# variable-length arguments(*args)
def add(*number):
    print(number)
add (10,20)
add (1,2,3,4,5,6,7,8,9)

