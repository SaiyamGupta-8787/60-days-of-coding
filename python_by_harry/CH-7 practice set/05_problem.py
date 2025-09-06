'''
5. Write a program to find the sum of first n natural numbers using while loop. 

'''
n = int(input("Enter a number : "))
# s = 0
# i = 0
# while(i<n+1):
#     s += i
#     i+=1

s = 0
for i in range(1,n+1):
    s = s+i



print(f"Sum of natural numbers upto {n} is = {s}")