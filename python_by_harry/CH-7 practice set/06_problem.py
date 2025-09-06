'''
6. Write a program to calculate the factorial of a given number using for loop. 
'''
f = 1
n = int(input("Enter a number : "))
i = 1
while(i<n+1):
    f = f*i
    i = i + 1
print(f"Factorial of {n} is = {f}")