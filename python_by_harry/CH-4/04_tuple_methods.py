t = (1,45,33,32342,False,"Rohan","Shivam")
print(t)
print(t.count(45))

i = t.index(45)
print(i)
print(len(t))


#! MORE ON TUPLES
# Tuple for testing
friends = ('Apple', 'Orange', 5, 34.341, False, 'AAKASH', 'rohan')

print("ORIGINAL TUPLE:", friends)
print("-" * 50)

# --- Basic Checks ---
print("len(friends):", len(friends))
print("'Apple' in friends:", 'Apple' in friends)
print("friends[0]:", friends[0])
print("friends[-1]:", friends[-1])
print("friends[1:4]:", friends[1:4])  # slicing

print("-" * 50)

# --- Counting & Index ---
print("friends.count('Apple'):", friends.count('Apple'))
print("friends.index('Orange'):", friends.index('Orange'))

print("-" * 50)

# --- Concatenation & Repetition ---
new_tuple = friends + ("Mango", "Banana")
print("friends + ('Mango', 'Banana'):", new_tuple)

repeat_tuple = ("Hi",) * 3
print("('Hi',) * 3:", repeat_tuple)

print("-" * 50)

# --- Conversion ---
friends_list = list(friends)
print("Convert tuple to list:", friends_list)

back_to_tuple = tuple(friends_list)
print("Convert list back to tuple:", back_to_tuple)

print("-" * 50)

# --- Nesting ---
nested = (1, 2, (3, 4, 5), ("a", "b"))
print("nested tuple:", nested)
print("nested[2]:", nested[2])
print("nested[2][1]:", nested[2][1])

print("-" * 50)

# --- Unpacking ---
a, b, *rest = friends
print("a:", a, "| b:", b, "| rest:", rest)
