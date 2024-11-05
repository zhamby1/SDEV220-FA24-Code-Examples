#data structures defin how data is stored and organized outside of normal (primitive) data types.  Usually they contain more than one piece of data
#lists are a type of data structure that can hold multiple pieces of data
#Similar to arrays in other langauges, excepts lists can hold multiple data types and are dynamic in size
#lists are defined by square brackets []
#lists are mutable, meaning they can be changed after they are created, and can be modifyied to add, delete, or change elements

#creating a list
#nameoflist = []

# #list of test scores for a class test
test_scores = [100, 90, 80, 70, 60]
# #if we need to access or change a single item/element in a list, we use the index of the element to grab it.  Lists start at the 0 index position (index means where the elements are located in the list by it's order)

print(test_scores[0]) #100
print(test_scores[1]) #90

test_scores[0] = 95
print(test_scores[0]) #95

#we want to use lists to group things together, as well as be able to iterate over them to change or access the elements in the list (iterate ie use a loop to go through each element in the list)

#if we need to display or modify items in a list, we use a for loop
#in python there are a few types of for loops

#for in loop - for items in this list do the following thing
#we are going to use a for in loop to display all the test scores in the list. To do so we create a variable placeholder to represent each INDIVIDUAL score in the test_scores list

# for single item in list
for score in test_scores:
    print(score)

#instead of printing the score, we can add 5 to each score (modify the score)
for score in test_scores:
    score = score + 5
    print(score)

#adding to a data to a list - we can add data to a list by using the append() method

new_score = 50
test_scores.append(new_score)
print(test_scores)

#now lets go through all the list functions or methods that we can use with lists
#extend() - combines data from list to another
test_scores2 = [10,20,90]
test_scores.extend(test_scores2)
print(test_scores)

#removing from a list you can use the remove function/method
test_scores.remove(10) #removes the first instance of the number 10 in the list
print(test_scores)

#finding something in a list - this will give you a true or false value.  Then you can use if statements to remove/modify values
looking_for = 80
#the in keyword is used to check if a value is in a list
found = looking_for in test_scores

if found == True:
    print("Found the value")
    test_scores.remove(looking_for)
    print(test_scores)
else:  
    print("Value not found")

#count() - counts the number of times a value appears in a list
print(test_scores.count(90))

numbers = [10,3,7,5,9,100]
#sort() - sorts the list in ascending order smallest to larges
numbers.sort()
print(numbers)

#sort in descending order - largest to smallest
numbers.sort(reverse=True)
print(numbers)

#find the length of a list by using len() function
print(len(numbers))

#this is an alternative to a for in loop, in is similar to what you would see with a traditional for loop in other languages
for i in range(len(test_scores)):
    print(i, "-", test_scores[i])