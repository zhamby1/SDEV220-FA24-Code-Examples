#an or compound or logical statment is true if either condition is true
#ie only on condition must be true for the whole if statement to be evaluated to be true
#Or Truth Table - 
#T/T = T
#T/F = T
#F/T = T
#F/F = F

#lets use the movie example from earlier, and clean it up a bit
#lets ignore the G rating.  Remember 12 and younger get a discount as well as 65 and older


ticket_price = 10.00
discount = 0.10
age = int(input("How old are your? "))

#or condition

if age <= 12 or age >= 65:
    ticket_price = ticket_price - (ticket_price * discount)
    print("Your ticket price is", ticket_price)
else:
    print("Your ticket price is", ticket_price)
