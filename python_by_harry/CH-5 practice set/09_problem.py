"""
9. Can you change the values inside a list which is contained in set S? 
s = {8, 7, 12, "Harry", [1,2]}

"""
s = {8, 7, 12, "Harry", [1,2]} #!List cannot be inside a set, as only immutable datatypes can be put inside a set

s[4][0] = 9 #! WRONG
