marks = {
    "Harry" : 100, #! Key:Value
    "Shubham" : 56,
    "Rohan" : 23
}
print(marks, type(marks))
#! print(marks[0]) #) is not a ke : ERROR
print(marks["Harry"]) #!prints corresponding value of the key "Harry"

#! Dictionaries are unordered(prins in random order) , mutable(values of keys can be changed), indexed(Keys are used as indexes), and keys are unique and immutable