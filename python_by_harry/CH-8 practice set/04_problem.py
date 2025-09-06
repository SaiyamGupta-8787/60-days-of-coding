'''
4. Write a recursive function to calculate the sum of first n natural numbers. 

'''

'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5
sum(n-1) = 1 + 2 + 3 + 4 + 5 + ... + n-1
sum(n) = 1 + 2 + 3 + 4 + 5 + ... + n-1 + n
'''

def SUM(n):
    if(n==1): #* Base condition to avoid infinite recursion(ulta na chala jaye) and stop at n=1
        return 1
    return SUM(n-1) + n
print(SUM(4))
