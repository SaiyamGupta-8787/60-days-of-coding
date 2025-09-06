friends = ['Apple','Orange',5,34.341,False,'AAKASH', 'rohan']

print(friends)
friends.append("heyya") #'heyya' appended/ added to the last of the original frie=nds list
print(friends)


l1 = [1,23,312,11,6]
l1.sort() #arranges original l1 in ascending order
print(l1) 
 

l1.reverse()
print(l1)

l1.insert(3, 333) #Insert 333 so that its index is 3 in the list
print(l1)

value = l1.pop(3) #remove and return element at 3rd index
l1.pop() #removes and returns last element by default
print(l1)
print(value)

l1.remove(23) #removes first occurence of given word
print(l1) 

#! More on list methods
# List for testing
friends = ['Apple', 'Orange', 5, 34.341, False, 'AAKASH', 'rohan']

print("ORIGINAL LIST:", friends)
print("-" * 50)

# --- Basic Checks ---
print("len(friends):", len(friends))
print("'Apple' in friends:", 'Apple' in friends)
print("friends[0]:", friends[0])
print("friends[-1]:", friends[-1])
print("friends[1:4]:", friends[1:4])  # slicing

print("-" * 50)

# --- Adding Elements ---
friends.append("Mango")
print("After append('Mango'):", friends)

friends.insert(2, "Banana")
print("After insert(2, 'Banana'):", friends)

more_friends = ["Grapes", "Pineapple"]
friends.extend(more_friends)
print("After extend([...]):", friends)

print("-" * 50)

# --- Removing Elements ---
friends.remove("Apple")  # removes first occurrence
print("After remove('Apple'):", friends)

popped = friends.pop()   # removes last item
print("After pop():", friends, " (popped:", popped, ")")

popped_at_1 = friends.pop(1)  # removes item at index 1
print("After pop(1):", friends, " (popped:", popped_at_1, ")")

del friends[0]  # delete by index
print("After del friends[0]:", friends)

print("-" * 50)

# --- Modification ---
friends[0] = "Kiwi"
print("After friends[0] = 'Kiwi':", friends)

print("-" * 50)

# --- Sorting & Reversing ---
nums = [4, 1, 7, 3, 9, 2]
print("nums:", nums)
nums.sort()
print("After sort():", nums)
nums.sort(reverse=True)
print("After sort(reverse=True):", nums)
nums.reverse()
print("After reverse():", nums)

print("-" * 50)

# --- Useful Functions ---
nums = [4, 1, 7, 3, 9, 2]
print("nums:", nums)
print("min(nums):", min(nums))
print("max(nums):", max(nums))
print("sum(nums):", sum(nums))
print("nums.count(3):", nums.count(3))

print("-" * 50)

# --- Copying & Clearing ---
copy_list = nums.copy()
print("copy_list:", copy_list)

nums.clear()
print("After clear():", nums)

print("-" * 50)

# --- Nested Lists ---
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("matrix:", matrix)
print("matrix[0]:", matrix[0])
print("matrix[1][2]:", matrix[1][2])


