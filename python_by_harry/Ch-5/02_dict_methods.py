marks = {
    "Harry" : 100,
    "Shubham" : 56,
    "Rohan" : 23,
    0 : "hey"
}

print(marks.items()) #shows hey:value pairs in form of tuples in a list

print(marks.keys()) #Prints key
print(marks.values()) #Prints values

marks.update({"Harry":99, "Renuka":100}) #! on passing dictionary in update(), existing key:values are changed, and new key:value pairs are added if not in marks


print(marks) 

print(marks.get("Harry"))
print(marks.get("Harry"))
print(marks.get("Shivika")) #key not in marks

#!DIfference b/w marks["Harry"] and marks.get("Harry")

print(marks.get("Harry1")) # prints None
#print(marks["Harry1"]) #returns an Error

#! MORE ON DICTIONARIES

#🔑 Python Dictionaries – Complete Guide
#1. What is a Dictionary?

#A dictionary (dict) is an unordered, mutable, and indexed collection of key:value pairs.

#Think of it as a real-life dictionary: the word is the key, the definition is the value.

#Example:

student = {
    "name": "Alice",
    "age": 20,
    "is_active": True
}
'''

Here:

"name", "age", "is_active" → keys

"Alice", 20, True → values
'''
'''
2. Dictionary Rules


Keys must be unique. If you reassign, it overwrites:
'''
d = {"a": 1, "a": 2}
print(d)   # {'a': 2}


'''
Keys must be immutable (string, number, tuple).
Lists, dicts, or sets cannot be keys.
'''
#d = { [1,2]: "bad" }   # ❌ TypeError
d = { (1,2): "good" }  # ✅ works


#Values can be anything: strings, lists, dicts, even functions.

'''
3. Creating Dictionaries
'''
# Method 1: Curly braces
person = {"name": "Bob", "age": 25}

# Method 2: dict() constructor
person = dict(name="Bob", age=25)

# Method 3: from list of tuples
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)   # {'a': 1, 'b': 2}

# Method 4: dictionary comprehension
squares = {x: x**2 for x in range(5)}
# {0:0, 1:1, 2:4, 3:9, 4:16}
'''
4. Accessing and Modifying
student = {"name": "Alice", "age": 20}
'''
print(student["name"])      # Alice
print(student.get("grade")) # None (safe way to avoid KeyError)

student["age"] = 21         # update
student["grade"] = "A"      # add new key:value
print(student)              # {'name':'Alice','age':21,'grade':'A'}

del student["grade"]        # delete key
'''
5. Useful Dictionary Methods
d = {"a": 1, "b": 2, "c": 3}
'''
print(d.keys())    # dict_keys(['a','b','c'])
print(d.values())  # dict_values([1,2,3])
print(d.items())   # dict_items([('a',1),('b',2),('c',3)])

# Safe retrieval with default
print(d.get("z", 0))   # 0

# Update / merge
d.update({"b": 20, "d": 40})
print(d)  # {'a':1, 'b':20, 'c':3, 'd':40}

# Remove
print(d.pop("a"))  # 1
print(d)           # {'b':20,'c':3,'d':40}

# Pop last inserted
print(d.popitem()) # ('d',40)

# Clear
d.clear()          # {}

'''
6. Iterating Over Dictionaries
person = {"name": "Alice", "age": 20}
'''
# By keys
for key in person:
    print(key, person[key])

# By values
for value in person.values():
    print(value)

# By key-value pairs
for k, v in person.items():
    print(f"{k} -> {v}")
'''
7. Dictionary Comprehensions

Super powerful way to generate dictionaries.
'''
# Mapping numbers to their squares
squares = {x: x**2 for x in range(6)}
print(squares)  # {0:0,1:1,2:4,3:9,4:16,5:25}

# Inverting a dictionary
d = {"a":1, "b":2}
inverse = {v: k for k, v in d.items()}
print(inverse)  # {1:'a', 2:'b'}

# Filtering
nums = {"a": 10, "b": 3, "c": 15}
big = {k: v for k,v in nums.items() if v > 5}
print(big)  # {'a':10, 'c':15}

'''
8. Nested Dictionaries

Dictionaries inside dictionaries.
'''
students = {
    "101": {"name": "Alice", "age": 20},
    "102": {"name": "Bob", "age": 22}
}

print(students["101"]["name"])  # Alice
