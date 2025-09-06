
#! if, elif, else ladder

a = int(input("Enter your age :"))


#* if, elif, else ladder

if(a>=18):       #!Block of code in if
    print("You are above the age of consent") #Indentation
    print("Good for you")

elif(a<0):
    print("You are entering an invalid age")

elif(a==0):
    print("You are entering zero, which is not a valid age")


else:
    print("You are below the age of consent")


print("End of program")