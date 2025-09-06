'''

7. Write a program to print the following star pattern. 
* 
*** 
***** for n = 3 

'''
'''
for n = 3
  *
 ***
*****
'''
n = int(input("Enter number of lines:"))
#!Simmple

# print("*")
# print("**")
# print("***")

# for i in range(1,n+1):
#     print("*"*i,)
# #! 1,3,5,7,...
# for i in range(1, n+1):
#     print("*"*(2*i - 1))

#! Pyramid
for i in range (1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i - 1))