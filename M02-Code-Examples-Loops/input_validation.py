#ask for someones age, if they are less than 0 (they accidently give you a negative), ask again

#you can also break loops by using booleans and the break statement

while True:
    age = int(input("Give me your age "))
    if age < 0:
        print("You have given me an age that is less than 0. Please try again")
    else:
        break

print("You age is", age)

#doing same thing with try/except aka try/catch

# while True:
#     try:
#         age = int(input("Give me your age "))
#         if age < 0:
#             raise ValueError
#         break
#     except ValueError:
#         print("Input invalid.  Please enter positive integer")