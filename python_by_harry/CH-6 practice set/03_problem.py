"""
3. A spam comment is defined as a text containing following keywords: 
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams. 

"""

s1 = 'Make a lot of money'
s2 = 'buy now'
s3 = 'subscribe this'
s4 = 'click this'

S = input("Enter a string : ")

if (s1 in S) or (s2 in S) or (s3 in S) or (s4 in S):
    print("SCAM DETECTED !!!")
else:
    print("NO SCAM DETECTED !!!")
