"""
2. Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user. 

"""
sub_1 = int(input("Enter marks of a subject out of 100 : "))
sub_2 = int(input("Enter marks of a subject out of 100 : "))
sub_3 = int(input("Enter marks of a subject out of 100 : "))

total_percentage = ((sub_1 + sub_2 + sub_3)/300)*100

if (sub_1<0 or sub_1>100 or sub_2<0 or sub_2>100 or sub_3<0 or sub_3>100):
     print("INVALID MARKS")

elif(total_percentage>=40 and (sub_1>=33 and sub_2>=33 and sub_3>=33)):
    print("YOU ARE PASSED!!!")

else:
     print("YOU ARE FAILED!!!")

