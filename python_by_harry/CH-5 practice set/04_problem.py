"""
4. What will be the length of following set s: 
s = set() 
s.add(20) 
s.add(20.0) 
s.add('20') # length of s after these operations? 

"""

s = set() 
s.add(20)  #! VERY IMPORTANT, when comparing int and float, python compares their 'values', not datatypes, it converts the in into a float(1.0), then compares it to any float in front of it, in this case, 20==20.0  is same as 20.0==20.0 = true
s.add(20.0) 
s.add('20')
print(s)
print(len(s))