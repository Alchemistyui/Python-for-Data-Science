'''
--------------
is & == ?
--------------
'''
x = 3
y = 3.0
#false, only variabels point to the same object return true
print(x is y)
#true, since they have the same value
print(x == y) 

'''
--------------
String
these two method return only copy but not change the original!!
since string is immutable
--------------
'''
x = 'HEllo'
# print(capitalize(x)) --> false!!
# ways to use build-in method!
print(x.capitalize())
x.upper()
print(x)
print(x.lower())
# concat string
y = '1' + '2'
# repeat string
y = '1'*3 + '-'*2
print(y)
# strip(s, [, chars]), strip move the newline, spaces before and after the words
s = '  Alchemi st \n'
print(s.strip())
s = '----1 0----\n'
print(s.strip('-'))
# split(s [, sep, maxsplit])
s = 'a s d f g h'
print(s.split(' ', 3))
# slicing: left inclusive, right exclusive
s = 'hello' # pos idx:[0,1,2,3,4]; neg idx: [-5, -4, -3, -2, -1]
print(s[0:3])
print(s[4:7]) # not cause an error
print(s[-4:-1]) #negitive idx = positive idx - str length
# find(sub [, start, end]) -> lowest start idx or -1
print(s.find('el'))
# convert to numerical
s = '12'
int(s)
float(s)
# format
statement = 'we love {} {}'
print(statement.format('data', 'analysis')) 



'''
--------------
Loops
--------------
'''
# range(start, stop, [,step]]): start is inclusive, end is exclusive
for i in range(0, 10, 2):
    print(i)


'''
--------------
Conditions
--------------
'''
# if, elif, else
def return_what():
    pass
x = return_what()
print(x)

'''
--------------
Scope
--------------
'''
# beware, scope val and global val has same name is a bad practice
# notice, some companies like google don't recommend using global val
val = -2
def my_abs(val):
    if val < 0:
        return 0 - val
    else:
        return val
print(val)

'''
--------------
List: mutable
--------------
'''
li = [11, 22, 33]
for i in li:
    print(i)
for i in range(0, len(li)):
    print(li[i])
# list elem is changable
li[1] = 95
li.append(44)
li.pop(2) # remove the elem using idx and return that elem
li.remove(44) # remove the elem using its value
# merge 2 list
l1 = [1,2,3]
l2 = [4,5,6]
li.extend(l2)
# zip: crate a pairing of 2 lists
for i in zip(l1, l2):
    print(i)
#  Deep Copy and Shallow Copy
cp = l1 # shallow, change list will influence all the referance
cp = list(l1) # deep, 


'''
--------------
Tuple: immutable, used for connected info in some way
--------------
'''
# collect diff type of data in tuple
tup = ('Honda', 'Civic', 4, 2017)
tup[1]
len(tup)
for i in tup:
    print(i)
# immutability!!!->1.general & parallel computing, 2.use as key of dict


'''
--------------
Dictionaries: fast for lookups, key-value pair, unordered collection
--------------
'''
# key is immutable->tuple, value can be list
dict1 = {('Cars', 1984): ['bob', 'tom'], ('cars', 2020): ['mary', 'jean']}
len(dict1)
print(dict1[('Cars', 1984)])
# add elem, if the key exist, just reassign its value
dict1[('Cars', 3000)] = 7
print(dict1)
# safe way to get from dict: return none when key not in dict, but not error
dict1.get(('Cars', 3000))
('Cars', 3000) in dict1
# remove
dict1.pop(('Cars', 3000)) # return the value back
# loop: dict1.items() return tuples with key & value
for key, value in dict1.items():
    print(key, ":", value)






