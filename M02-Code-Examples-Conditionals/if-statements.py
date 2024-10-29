#if statements allow you to control the flow of a program.  If something is true, the code will run in the spaced or indentation below the if statement.  if not, the if statement is skipped.

#relational operators - determine whether a condition or relationship between two variables is true or false.  All if statements return a boolean value

# <,>,<=,>=, ==, ! .  These are used to compare values

#if statement..no else.  called a single alternative

a = 5

if a > 2:
    print("A is greater than 2")

#double equal sign (==) is used in an if statement to COMPARE if two things are equal.  The single (=) sign assigns value

x = 7
y = 7

if x == y:
    print("x and y are equal")

# != means to compare two values to see if they are not equal
# we will see the ! (not) operator later on, but basically it takes the boolean result and flips it

first_number = int(input("give me a whole number "))
second_number = int(input("give me a second number "))

if first_number != second_number:
    print("These numbers are not equal")

