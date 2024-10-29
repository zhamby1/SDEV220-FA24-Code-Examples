#if-else statements are called dual-alternative.  If a statement is true, the path will flow into the if statement.  If the statement is falses, the path will flow into the else statement

#else literally means anything else

a = 7
b = 9

if a == b:
    print("A and B are equal")
else:
    print("A and B are NOT equal")

#can you vote program
#The code below will test to see if someone is old enough to vote
age = int(input("Please enter your age "))

if age >= 18:
    print("You are old enough to vote")
else:
    print("You are NOT old enough to vote")