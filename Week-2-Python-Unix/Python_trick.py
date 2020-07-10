'''
is & == ?
'''
x = 3
y = 3.0
#false, only variabels point to the same object return true
print(x is y)
#true, since they have the same value
print(x == y) 

'''
String
these two method return only copy but not change the original!!
since string is immutable
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



'''
Loops
'''
# range(start, stop, [,step]]): start is inclusive, end is exclusive
for i in range(0, 10, 2):
    print(i)


'''
Conditions
'''
# if, elif, else
def return_what():
    pass
x = return_what()
print(x)

'''
Scope
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

















