def greet(name, ending): #* name and ending is an argument/parameter which we can change everytime
    print("Good Day, " + name  )
    print(ending)
    return "Done"


greet("Harry", "Thank you") #* Harry goes into name, and thank you in ending
greet("Saiyam", "Thanks")
greet("Rohan", "Thank you")

a = greet("Divya", "Thank you")
print(a) #* None as function does not 'return' any value, using return, we return the final value of funtion, which we can store in other variablsa
