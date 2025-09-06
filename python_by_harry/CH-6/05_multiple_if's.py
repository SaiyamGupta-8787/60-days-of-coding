
#! if, elif, else ladder

a = int(input("Enter your age :"))


#* if, elif, else ladder

if(a%2==0):    #Seperate ladder, 1st if statemenet independent of others
    print("a is even")

#END OF 2st if statement
if(a>=18):       #2nd statement of if independent of others
    print("You are above the age of consent") #Indentation
    print("Good for you")

#END OF 2nd statement

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering zero, which is not a valid age")


else:
    print("You are below the age of consent")


print("End of program")