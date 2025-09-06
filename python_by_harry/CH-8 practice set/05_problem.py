'''
5. Write a python function to print first n lines of the following pattern: 
*** 
**               
* - for n = 3 

'''
'''
BY LOOPS
n = int(input('Enter a number : '))
for i in range(n,0,-1):
    print("*"*i)
'''

def pattern(n):
    if(n==0):
        return #Function ends after returning
    print("*"*n)
    pattern(n-1)

n = int(input("Enter no. of line : "))
pattern(n)