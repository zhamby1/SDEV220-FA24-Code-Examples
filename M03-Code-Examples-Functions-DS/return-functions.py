#functions can also return value
#return value - the value that is returned from the function
#we use the keyword return to do so
#we can retrun into a value or another function

#adding items we bought for a total

def add_items(item1, item2, item3):
    total = item1 + item2 + item3
    return total

#a return function must return value into something else
#in this case it is a variable
my_total = add_items(8.00,5.50,3.50)
print(my_total)

#chaining returned functions
#This functions takes in an amount and returns the amount with tax
def add_tax(total):
    tax = total * 0.10
    total_with_tax = total + tax
    print("Your total with tax is" , total_with_tax)

#without chaining
my_total2 = add_items(10,20,22)
add_tax(my_total2)

#chain to make easier.  chaining works because the return value is a number
add_tax(add_items(10,20,22))