#loops are also control structures. They repeat code until a condition is met.  They use the same logic and relational operators that conditionals use

#loops main goal is to repeat code until you do not want the code to be repeated
#two types of loops - for and while

#while loop - is a loop that repeats code based on a specific condition and is broken due to the condition no longer being met

#for loop - does similar things, but is controlled by a counter.  Repeats code a certian number of times or repeats code until it processes a certain amount of data

#in many cases while loops use flags/sentinel values to break the loop once the flag is no longer true

#program that will record and calculate commission based on a salary
#while loops are very useful for making menu based programs

#flag
keep_going = "y"

print("Enter the following to calculate your sales and commission. When you are done, press n and enter to exit.  If you would like to enter another sale, press y and enter")

while keep_going == "y":
    sales = float(input("What is your sales for the day? "))
    com_rate = float(input("What is your commission rate in the form of a decimal? "))
    total_earned = sales * com_rate
    print("You have earned", total_earned, "today.")
    keep_going = input("Do you wish to run the program again? Press y and enter for yes or n and enter for no ")

print("Thanks for using our program")