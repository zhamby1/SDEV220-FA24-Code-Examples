#string formatting - formatting text in a certain way declared by the programmer.  I.e. I can change normal text to look like money, I can round or drop certain values after a decimal, put values in scientific notation, etc..

#https://www.w3schools.com/python/ref_string_format.asp
#the way python does string formatting is by using f and braces inside of a print function to create placeholders and formatting rules

number = 4
amount = 4.5644655

#traditional way of printing in python
print("I bought", number, "burritos, and it cost me $", amount)

#string formatting
print(f'I bought {number} burritos, and it cost me ${amount:.2f}')

#I want to use commas in between large numbers ie 4,000

print(f'The universe is {5000000000000:,} years old')