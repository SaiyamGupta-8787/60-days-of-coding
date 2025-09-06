'''
10. Write a program to print multiplication table of n using for loops in reversed 
order.
'''

n = int(input("Enter a number : "))

for i in range(10,0,-1): #* Negative stepping, we go from top to bottom
    print(f"{n} x {i} = {n*i}")