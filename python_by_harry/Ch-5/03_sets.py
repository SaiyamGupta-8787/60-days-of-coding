d = {} #empty dict, also dict() can be used
s = {1,2,3,3,3,"Saiyam"} #SET
empty_set = set() #dont use s = {} as it makes empty dictionary

print(s,type(s)) #doesnt print repeated values, and prints unordered

s.add(566)
print(s,type(s))

#! sets are unordered, unindexed, items cannot be changed, no duplicate values

#! Opertions on sets
s.remove(1)
print(s,type(s))
print(len(s))

s.pop() #removes any element
s.clear() #empties set


#! More on sets

'''
🔥 Python Sets – Complete Guide
1. What is a Set?

A set is an unordered collection of unique elements.

Sets are like mathematical sets: no duplicates, no order.

Example:

nums = {1, 2, 3, 3, 2}
print(nums)   # {1, 2, 3} (duplicates removed)

2. Properties of Sets

Unordered → elements have no fixed order.

Mutable → you can add/remove items.

No duplicates → {1,2,2} becomes {1,2}.

Only immutable elements allowed → you can’t add lists or dicts, but you can add tuples.

s = {1, "hello", (2,3)}
print(s)   # {1, 'hello', (2,3)}

3. Creating Sets
# Curly braces
s1 = {1, 2, 3}

# Constructor
s2 = set([1, 2, 3, 3])   # {1,2,3}

# Empty set (⚠️ {} is a dict!)
empty = set()

4. Adding & Removing Elements
s = {1, 2}
s.add(3)             # {1,2,3}
s.update([4, 5])     # add multiple elements

s.remove(2)          # remove specific element (error if missing)
s.discard(10)        # safe remove (no error if missing)

x = s.pop()          # removes & returns a random element
s.clear()            # empty set

5. Set Operations (Mathematical)

Sets are powerful because of set operations.

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # Union → {1,2,3,4,5,6}
print(a & b)   # Intersection → {3,4}
print(a - b)   # Difference → {1,2}
print(b - a)   # Difference → {5,6}
print(a ^ b)   # Symmetric difference → {1,2,5,6}

6. Membership & Subsets
a = {1, 2, 3}
b = {1, 2, 3, 4}

print(2 in a)          # True
print(a.issubset(b))   # True
print(b.issuperset(a)) # True
print(a.isdisjoint({4,5})) # True

7. Frozensets (Immutable Sets)

A frozenset is like a set, but immutable (can’t add/remove).

Useful as dictionary keys or when you need a fixed set.

fs = frozenset([1,2,3])
print(fs)  # frozenset({1,2,3})

8. Real-World Applications

Removing duplicates:

names = ["a", "b", "a", "c"]
unique = set(names)    # {'a','b','c'}


Membership testing (faster than lists):

words = {"apple", "banana", "cherry"}
print("banana" in words)   # O(1) lookup


Data science (set operations on tags, IDs, categories)

users_A = {"alice", "bob", "carol"}
users_B = {"bob", "dave"}
print(users_A & users_B)  # {'bob'} (common users)


Web scraping / logs: Store unique URLs visited.

Automation: Detect duplicates in files, filter unique entries.

9. Common Mistakes & Tricks

❌ Mistake: Using {} for empty set.

s = {}          # this is a dict, not a set!


✅ Correct:

s = set()


❌ Mistake: Expecting order.
Sets don’t maintain order (before Python 3.7+ dicts did, sets never do).

⚡ Trick: Convert list → set → list to remove duplicates.

nums = [1,2,2,3,1]
unique = list(set(nums))


⚡ Trick: Find common elements between two lists.

l1 = [1,2,3,4]
l2 = [3,4,5,6]
common = list(set(l1) & set(l2))  # [3,4]
'''