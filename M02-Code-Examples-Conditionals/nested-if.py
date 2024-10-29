#nested ifs work by have a series of if statements that must be true and drilled down to in order to run
#compound conditions work similarly, but not in the same way
#we try to avoid nested-ifs when possible, because it can be hard to read and takes up memory processing

#lets make a quick program that says you get a discounted movie ticket if you are 12 and younger or if you are 65 and older and the rating is G

ticket_price = 10.00
discount = 0.10

age = int(input("How old are you? "))
rating = "G"
#when comparing strings, capitlization DOES matter
if(rating == "G"):
    if(age <= 12):
        ticket_price = ticket_price - (ticket_price * discount)
        print("Child discount. Your ticket price is", ticket_price)
    else:
        print("Ticket price is", ticket_price)
    
    if(age >= 65):
        ticket_price = ticket_price - (ticket_price * discount)
        print("Senior Citizen discount.  Your ticket price is", ticket_price)
    else:
        print("Ticket price is", ticket_price)
else:
    print("Rating is not G, discount not allowed. Ticket price is", ticket_price)


