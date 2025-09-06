
"""

str = 'harry' 

#! 1. len() function – This function returns the length of the strings. 

str = "harry" 
print(len(str))  # Output: 5

#! 2. String.endswith("rry") – This function_ tells whether the variable string ends with  the string "rry" or not. If string is "harry", it returns true for "rry" since Harry ends with rry.

name = "harry" 
print(name.endswith("rry"))  # Output: True
print(name.startswith("hao"))

#! 3. string.count("c") – counts the total number of occurrences of any character. 

str = "harry" 
count = str.count("r") 
print(count)  # Output: 2

#! 4. the first character of a given string.

str = "harry" 
capitalized_string = str.capitalize() 
print(capitalized_string)  # Output: "Harry" 


#!5. string.find(word) – This function finds a word and returns the index of first occurrence of that word in the string.

str = "harry" 
14 
index = str.find("rr") 
print(index)  # Output: 2

#! 6. string.replace (old word, new word ) – This function replace the old word with  new word in the entire string.

str = "harry" 
replaced_string = str.replace("r", "l") 
print(replaced_string)  # Output: "hally" 

"""
#testing

s = "  Hello World 123!!  "
print("original string : ", repr(s))
print("-"*50)
print()

# --- Basic Checks ---
print("len(s):", len(s))
print("s.isalpha():", s.isalpha())
print('"123".isdigit():', "123".isdigit())
print('"Hello123".isalnum():', "Hello123".isalnum())
print('"   ".isspace():', "   ".isspace())
print('"hello".islower():', "hello".islower())
print('"HELLO".isupper():', "HELLO".isupper())
print('s.startswith("   He"):', s.startswith("   He"))
print('s.endswith("!!!   "):', s.endswith("!!!   "))

print("-" * 50)

# --- Searching ---
print('s.find("World"):', s.find("World"))
print('s.rfind("l"):', s.rfind("l"))
print('s.index("Hello"):', s.index("Hello"))
print('s.count("l"):', s.count("l"))

print("-" * 50)

# --- Modification ---
print("s.lower():", s.lower())
print("s.upper():", s.upper())
print("s.title():", s.title())
print("s.capitalize():", s.capitalize())
print("s.swapcase():", s.swapcase())
print("s.strip():", repr(s.strip()))
print("s.lstrip():", repr(s.lstrip()))
print("s.rstrip():", repr(s.rstrip()))
print('s.replace("World", "Python"):', s.replace("World", "Python"))
print('"42".zfill(5):', "42".zfill(5))

print("-" * 50)

# --- Splitting & Joining ---
print("s.split():", s.split())
print('s.split("o"):', s.split("o"))
print('"o".join(["Hell", "W", "rld"]):', "o".join(["Hell", "W", "rld"]))
print('s.partition("World"):', s.partition("World"))
print('s.rpartition("l"):', s.rpartition("l"))

print("-" * 50)

# --- Formatting ---
print('"Hello".center(10, "-"):', "Hello".center(10, "-"))
print('"Hello".ljust(10, "."):', "Hello".ljust(10, "."))
print('"Hello".rjust(10, "."):', "Hello".rjust(10, "."))
print('"{} {}!".format("Hello", "Python"):', "{} {}!".format("Hello", "Python"))
name = "Saiyam"
print(f"f-string: Hello {name}, welcome!")

print("-" * 50)

# --- Useful Extras ---
print('"Hello".encode():', "Hello".encode())
print('"Hello\\tWorld".expandtabs(4):', "Hello\tWorld".expandtabs(4))
print('"Straße".casefold():', "Straße".casefold())

