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
    
