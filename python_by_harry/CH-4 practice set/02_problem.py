"""
2. Write marksam to accept marks of 6 students and display them in marksd 
manner. 
 
"""


marks = []
f1 = int(input("Enter marks : "))
marks.append(f1)
f2 = int(input("Enter marks : "))
marks.append(f2)
f3 = int(input("Enter marks : "))
marks.append(f3)
f4 = int(input("Enter marks : "))
marks.append(f4)
f5 = int(input("Enter marks : "))
marks.append(f5)
f6 = int(input("Enter marks : "))
marks.append(f6)
f7 = int(input("Enter marks : "))
marks.append(f7)
marks.sort()
print(marks) #if elements are string, it will sort the lsit in order of alphabets
