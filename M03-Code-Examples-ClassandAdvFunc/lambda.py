#anonymous or anon functions - functions without a name..used as a tiny function usually inside of another function
#Why?

#main reason is two fold
#1. you can create variable that are expressions
#2. very useful in event based programming when an event happens and you can just write a function inside of the () instead of call a new def function outside

#example of traditional function to double a number
#def double_number(number):
#  double = number * 2
#  return double
# doubled_number = double_number(5)
# print(doubled_number)

#lambda function - we can use an expression (=) to define a function with an anon function.  This derive from lambda calc
#anon functions are ALWAYS return functions
# example of an expression is x = 6
#syntax:
#variable name = lambda parameter: parameter body or function body
double = lambda number: number * 2
#python treats functions as first class citizens aka functions can take in other functions as params/arguments..function chaining
print(double(34))

multiply = lambda first_num,second_num: first_num * second_num
print(multiply(5,6))

#you could run lambda without a name making it a true anon function
word = "HelloWorld"
(lambda text: print(text))(word)