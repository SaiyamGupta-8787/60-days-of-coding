
#! type() fxn used to find data type of a value 

a = 31  

ta = type(a) # class <int> 
print(ta)

b = "31" 
tb = type (b) # class <str>
print(tb)

c = 3.14

tc = type(c) #class <float>
print(tc)

d = True
td = type(d) # class <bool>
print(td)

e = [1,2,3]
te = type(e) # class <list>
print(te)

f = (1,2,3)
tf = type (f) # class <tuple>
print(tf)

g = {1,2,3}
tg = type(g) # class <set>
print(tg)

h = {a:'hello, a is a key, am its value'}
th = type(h) #class <dict>
print(th)

#! Typecasting
x = "23.12"
y = float (a) # x but type should be float

print(type(x))
print(type(y))

