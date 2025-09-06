'''
4. Write a program to find whether a given number is prime or not. 

'''

n = int(input("Enter a number : "))
if(n<=1):
    print("Not prime")
else:
    let_prime = True
    for x in range(2,n):
        if(n%x==0):
            let_prime = False
            break
    
    if let_prime :
        print("Prime")
    else:
        ("Not prime")
