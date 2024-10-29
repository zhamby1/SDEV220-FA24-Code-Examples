#create a program that determines if you can get a loan based on salary and years worked.  If you have worked 2 years or more and your salary is greater than 30,000 a year..then you qualify for a loan.

#salary
salary = float(input("Give me your salary for the year "))
years_on_the_job = int(input("How many years have you worked at your place of employment? "))

if salary >= 30000 and years_on_the_job >= 2:
    print("You qualify for a loan")

#lets deal with the alternative of not qualifying
#We want the user to know why they don't qualify
#years on the job -doesnt meet....salary does meet
elif salary >= 30000 and years_on_the_job < 2:
    print("You have not worked long enough to get a loan.  Salary is acceptable")

#worked long enough, but not enough salary
elif salary < 30000 and years_on_the_job >= 2:
    print("Your salary is not high enough to qualify.  You have worked long enough at your workplace")

else:
    print("You dont have a high enough salary to qualify, and you have not worked long enough at your job")
