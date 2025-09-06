'''
Recursion is a function which calls itself.

It is used to directly use a mathematical formula as function.  

ek fxn apne app ko tab call karta hai, jab usse uska logic juda ho
'''

'''
factorial(0) = 1
factorial(1) = 1 
factorial(2) = 2 x 1 
factorial(3) = 3 x 2 x 1 
factorial(4) = 4 x 3 x 2 x 1 
factorial(5) = 5 x 4 x 3 x 2 x 1 
factorial(n) = n x (n-1) x (n-2) x ... x 3 x 2 x 1

factorial(n) = n x factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a number : "))
print(f"The factorial of this number is :{factorial(n)}")

############# The programmer needs to be extremely careful while working with recursion to ensure that the function doesn’t infinitely keep calling itself. Recursion is sometimes the most direct way to code an algorithm.