#for loop repeats code a certain number of times.  The big use of this is with data structures (lists, dicts, sets). We will look at this next module

#python is a little weird when it comes to for loops.  There are several ways you can do it, but the 'traditional' for loop uses a range function to help

#for loops look like this in other languages
# for(int i = 0, i < 10, i = i + 1)
# python does it the following way
# for iterable_value_name in range(starting_value,ending_value, increment)

number = 5
for i in range(0,number,1):
    print(i)


#separate both outputs/visual break for each loop
print("********************")
#we can also have decrements as well as increments
countdown = 0



#countdown loop
for i in range(10,countdown,-1):
    print(i)