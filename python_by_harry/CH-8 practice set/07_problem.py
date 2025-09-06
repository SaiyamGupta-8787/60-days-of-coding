'''
7. Write a python function to remove a given word from a list ad strip it at the same 
time. 
'''

def rem(lst, word):
    n = []
    for item in lst:
        if item != word:             # remove exact match
            n.append(item.strip())   # just strip whitespace
    return n

l = ['Harry', 'Rohan', 'Shivam', 'an']
print(rem(l, "an"))
