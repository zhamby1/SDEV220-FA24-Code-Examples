#using compound operators
#compound operators allow you to check for multiple condition inline with your if statements. 
#There are three types of compound conditions
# and - both things must be true for the if statement to be evaluated to true
# or - only ONE must be true for the resulting if statement to be evaluated to tru
# not - flips the boolean value of the result to it's opposite (i.e true becomes false, false becomes true)

#Truth Table - comparing booleans to see if result is true of false
#And Truth Table -
#T/T = T
#T/F = F
#F/T = F
#F/F = F

#lets take the previous example of being able to vote.  So far, we said you had to be 18 and older to vote.  Let's also add that you must be registered to vote
#You can do this a few ways, but lets look at two
#Answer 1 - Nesting (bad)

age = 16
registered = "n"

#nested statements must be true all the way down as we go.
#in other words for line 19 to execute line 17 and 18 = true
# if(age >= 18):
#   if(registered == "y"):
#     print("you can vote")

#   else:
#     print("You can't vote due to not being registered")
# else:
#   print("You cant vote due to age")

#Answer 2 - using compound conditions.

if age >=18 and registered == "y":
    print("You can vote")

elif age>=18 and registered == "n":
    print("Your are old enough, but are not registerd to vote.  You cannot vote")

elif age <= 17 and registered == "y":
    print("Your are not old enough to vote. You are registered.  You cannot vote")

else:
    print("You cannot vote because you are not registered and you are too young")
