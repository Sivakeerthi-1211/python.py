n= int(input("Enter number of rows: "))

# Upper Half
for i in range(1, n + 1):
    # Left Triangle
    for j in range(1, i + 1):
        print("*", end=" ")

    # Middle Spaces
    for j in range(2 * (n - i)):
        print(" ", end=" ")

    # Right Triangle
    for j in range(1, i + 1):
        print("*", end=" ")

    print()

# Lower Half
for i in range(n - 1, 0, -1):
    # Left Inverted Triangle
    for j in range(1, i + 1):
        print("*", end=" ")

    # Middle Spaces
    for j in range(2 * (n - i)):
        print(" ", end=" ")

    # Right Inverted Triangle
    for j in range(1, i + 1):
        print("*", end=" ")

    print()

    #  
n = int(input())
for i in range(n):
     for j in range(n):
        if j==n//2:
              print("",end = " ")
              else:
                print("_",end="")
    print()
        #
n = int(input("Enter an odd number: "))

# Top horizontal line
for i in range(n):
    print("*", end=" ")
print()

# Vertical line
mid = n // 2
 end=" "