#variables store data.  They are noun of the programming world aka the data.
#python is a weakly typed language - variables have types, but you do not declare the type before the initialization of the variable.

#data type - the type of data stored in a variable
#integer or int - whole number (no decimal)
#float - decimal number
#string - text
#boolean = true or false (one one or the other)

x = 6 #int
y = 5.6 #float
my_name = "Zach" #string
my_bool = True #boolean

#functions - perform actions, take input, process the input, and produce an output
#functions are the verb of the programming world - they are actions
#built-in functions in python perform an action that we will use.  You can the difference between a function and a variable in that functions are ended with a ().  ie print() or input()

#input function - takes an input and returns it into a variable.  The code inside the () is called an argument.  The argument is data that is taken into the variable to be processed or used in some way.  
#in this case, the argument is used to display a prompt to the user.
name = input("What is your name? ")

#print function displays things on screen.  The argument of this function is used to display whatever is inside the ().  It takes that and converts to a string and displays it.
#you can join variables with text by using a comma ,
print("Your name is", name)


#the cool thing about variables is that they can change. you can also take the current value of a variable and manipulate its current value into something else.
#increment - increasing value
#decrement - decreasing value

z = 6
z = 10
print(z)
z = z + 2

print(z)

