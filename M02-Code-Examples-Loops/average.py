#another use of loops is accumulation of numbers or keeping running totals
#this program will average numbers for a user
total_sum = 0
average = 0

how_many_numbers = int(input("How many numbers do you wish to average? "))

#count controlled because the user is giving us how many numbers they wish to enter
#use a for loop
for i in range(0,how_many_numbers,1):
    value = float(input("Please enter a value you wish to be averaged "))
    total_sum = total_sum + value

print("Your total sum is", total_sum)
average = total_sum / how_many_numbers
print("Your average is", average)