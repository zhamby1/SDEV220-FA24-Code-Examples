#tuples are immutable (does not change) lists of data...list of constants
#tuples are faster than lists
#constant is a variable that does not change.  declared and used
#tuples are used for fixed data
#tuples have to be replaced to be changed

#here is an example of something that is immutable (does not change) - Strings
#when changing a string value, it is actually creating a new string
#String are technically arrays of list of characters that represent an individual character or symbol

name = "Zach"
print(name)

# name[0] = "T" #this will not work because strings are immutable
name = "Tach" #this will work because it is creating a new string
print(name)

#tuples are created using parentheses - tuplename = (data1, data2, data3)
#Tuples, in general, can be accessed the same way a list can be
states = ("IL","KY","IN","OH")
#print tuples just like lists
for state in states:
    print(state)

#There is one type of "modifying" you can do, you can combine tuples because it makes or overwrites a new tuple
states2 = ("FL","GA","AL")
states = states + states2
print(states)