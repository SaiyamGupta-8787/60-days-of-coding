"""
1. Write a program to find the greatest of four numbers entered by the user. 

"""
n1 = int(input("Enter a number : "))
n2 = int(input("Enter a number : "))
n3 = int(input("Enter a number : "))
n4 = int(input("Enter a number : "))

if(n1>n2 and n1>n3 and n1>n4):
    print(n1,"is the largest number")
elif(n2>n1 and n2>n3 and n2>n4):
    print(n2,"is the largest number")
elif(n3>n1 and n3>n2 and n3>n4):
    print(n3,"is the largest number")
else:
    print(n4, "is the largest number")