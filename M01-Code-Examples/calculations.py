#calculations in python consist of your typical math calcs (- + / *)
#addition
a = 7
b = 10
answer = a + b
print(answer)

#multiplication
c = 7
d = 4
product = c * d
print(product)

#subtraction
e = 10
f = 5
answer2 = e - f
print(answer2)

#division
g = 20
h = 5
answer3 = g / h
print(answer3)

#integer division - drops a decimal in a division calc
dec_numb = 20.5
dec_numb2 = 10.4
int_division_answer = dec_numb // dec_numb2
print(int_division_answer)

#modulo or modulus operator.  divide two numbers and the resulting remainder of the answer is the answer - use the % to use modulo operator

mod1 = 5
mod2 = 2
moduloanswer = mod1 % mod2
print(moduloanswer)

#exponents - **
answer = 2 ** 8
print(answer)

#inputs work different with calculations
#strings cannot be calculated except for combining them (concatonation)
name1 = "Zach"
name2 = "Hamby"
name3 = name1 + name2
print(name3)

#all inputs come in as strings
#that means that they cannot be calculated if we want to use numbers
#so we have to convert those strings into another type - int or float
#this is called parsing
#There are built in functions in python to help us do this 

#int() - converts data to a integer
#float() - converts data into a float

#one of the cool things about python is you can chain functions.  So it is easiest to chain a input function with a parsing function like int() or float()
number1 = float(input("Give me your first number "))
number2 = float(input("Give me your second number "))
myanswer = number1 * number2
print(myanswer)

numbint = int(input("Give me number "))
numbint2 = int(input("Give me second number "))
total2 = numbint + numbint2
print(total2)