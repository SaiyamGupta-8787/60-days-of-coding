#Negative slicing 0 is -length, last index is -1

n = 'harry'
print(n[0:3])
print(n[-4:-1]) # convert -ve into corresponding +ve indexes -4 is 1, -1 is 4
print(n[1:4])

print(n[:4]) # 0:4
print(n[1:]) #1:length

#Slicing with skipping/stepping values

num = '0123456789'
print(num[1:9:2]) #take normal slice of 1:9, then only keep initial and every 2nd character after it

word = 'amazing'
word = word[:7] #word[0:7] = 'amazing'
word = word[0:] #wrodp[0:7] = 'amazing'
print(word)