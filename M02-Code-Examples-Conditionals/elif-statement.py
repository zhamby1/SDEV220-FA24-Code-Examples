#multi-alternative - more than two conditions we are comparing and trying to solve
#usually deals with ranges or deals with looking for certain values out of a list of value or conditions
#we use elif for this (also known as else-if) in python

#below is an example of taking a numerical grade, and assigning a ltter grade based on the following
# A = 90-100, B = 80-89, C = 70-79, D = 60 - 69, F = < 60

number_grade  = 82
letter_grade = ""

if number_grade >= 90:
    letter_grade = "A"

#short circuiting - when an if or elif condition is met, it skips the rest of the statements below
elif number_grade >= 80:
    letter_grade = "B"

elif number_grade >= 70:
    letter_grade = "C"

elif number_grade >= 60:
    letter_grade = "D"

else:
    letter_grade = "F"

print("Your letter grade is", letter_grade)