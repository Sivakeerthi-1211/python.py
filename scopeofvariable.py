# local variable
def display():
    x=10
    print('value of x:',x)
display()

#gobal variable
x=20
def display():
    x= 10
    print("value of second x:",x)
display()
print("value of 1st value ",x)

#both local gobal 
x=20
def display():
    x= 10
    print("value of second x:",x)
print('value of x',x)
display()
print("value of 1st value ",x)

# both local gobal
print('start')
x=20
def display():
    x=30
    print("inside function",x)
print('before function',x)
display()
print('outside function',x)
print('end')

#
x=20
def display():
    global  x
    x=30
    print("inside function: ", x)
print('before function:', x)
display()
print('outside function',x)
print('end')

