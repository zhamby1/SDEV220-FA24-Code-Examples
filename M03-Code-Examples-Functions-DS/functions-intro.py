#all the descriptors and definitions of functions
# functions take data in, transforms it, and output a result
#functions are considered actions - verb
#SDEV definition - functions are blocks of code that can be repeated when it's name is called. It can have data passed to it, and *can* return data as a result.

#we have used functions already ie the print and input function
#if we want to make a "custom" or defined function, we need to define or create it
#in python we call our own custom function defined functions

#two step process to using functions - define then call or use
#defining a function is creating it to be used later on
#to define a funtion, use the keyword def followed by the function name and parentheses
#def function_name():

#functions can just be a summary of statements that do not return value.
#these are often called void functions
#example below: take two numbers and add them together. Code that belows to a function is indented

def my_function():
    x = 6
    y = 4
    sum = x + y
    print(sum)

#to call or use a function, just type the function name followed by parentheses
my_function()
my_function()
my_function()   

#pass data to a functiom - parameters
#parameters are the variables that are passed to the function
#paraemeter is just an argument that we have not used yet, or a defined argument
#the terms argument and parameter can be used interchangably
#parameters are defined in the parentheses of the function definition
#passing data - give the function some outside data, and them perform actions on that data
#we can pass data in any form of the types we have talked about before (int, float, string, list, tuple, dictionary)
#we can also pass functions as data to other function (functions as first class citizens)

def display_number(my_number):  # you can think of parameters as placeholders for data
    print(my_number)    

display_number(4)
numb = 549
display_number(numb)

#multiple parameters, separate by commas and the order matters

def add_two_numbers(num1,num2):
    sum = num1 + num2
    print(sum)

add_two_numbers(5,6)
add_two_numbers(6,5)

def divide_two_numbers(num1,num2):
    quotient = num1 / num2
    print(quotient)

divide_two_numbers(10,2)
divide_two_numbers(2,10)