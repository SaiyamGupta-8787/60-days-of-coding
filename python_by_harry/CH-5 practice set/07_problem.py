"""
7. If the names of 2 friends are same; what will happen to the program in problem 
6? 

"""
#!Entering different values in a same key, then lsat value will be taken by key

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