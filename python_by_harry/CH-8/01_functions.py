# a = 1
# b = 2
# c = 3
# average = (a+b+c)/3
# print(average) 

# n1 = int(input("Enter a number : "))
# n2 = int(input("Enter a number : "))
# n3 = int(input("Enter a number : "))

# av = (n1+n2+n3)/3
# print(av)
#! if we need to repeat this process, we have to use functions, we need to put this piece of code a name

#* We always 'define' a function before our 'main' code, wehn we define a function, it is 'user defined', fucntions like print()or input() are in-built fxns
def avg():
    n1 = int(input("Enter a number : "))
    n2 = int(input("Enter a number : "))
    n3 = int(input("Enter a number : "))

    av = (n1+n2+n3)/3
    print(av)

#*_main_code

avg() #! Calling fucntion for using it
avg() #we can call it any number of times we want
avg() 
avg() 
avg() 
avg() 
