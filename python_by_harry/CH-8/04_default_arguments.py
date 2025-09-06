def greet(name, ending = "Thank you"): #default value given when defining function, if not given, it keeps this value, but if we give any value, it will change to that value
    print(f"Good Day {name}")
    print(ending)

greet("Rihan","Thanks")
greet("Harry")