"""
8. If languages of two friends are same; what will happen to the program in problem 
6? 

"""

#! There can be same value for two different keys

d = {}

name = input("Enter friends name : ")
L = input("Enter language  : ")
d.update({name : L})

name = input("Enter friends name : ")
L = input("Enter language  : ")
d.update({name : L})

name = input("Enter friends name : ")
L = input("Enter language  : ")
d.update({name : L})

name = input("Enter friends name : ")
L = input("Enter language  : ")
d.update({name : L})
print(d)