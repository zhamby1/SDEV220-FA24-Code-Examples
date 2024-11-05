#dictionaries create key-value pairs that associate a characteristic/property with a value.  Basically in python it is a hash table or an object.
#simlar to a class without methods ie an object literal
#dictionaries are mutable

#objects/dictionaries can be almost anything but in programming it usually refers to a wrapper that encapsulates related data together to describe some link the following:
# object called Person - name, age
# object called Car - make, model, year

#dictionaries can group soimething by a list of items and associated values (like an actual dictionary)
#Lets look at the example below where there is a list of bank customers, and their bank balance
#dictionary is created using curly braces - dictionaryname = {key1:value1, key2:value2, key3:value3}
bank_customers = {
    "Alice": 100,
    "Bob": 200,
    "Charlie": 300
}

#dictionaries can be accessed by the key, to display everything we can use a loop
for customer in bank_customers:
    #first iteration is Alice, 100.  customer is the key, bank_customers[customer] is the value where customer acts as an index
    print(customer, bank_customers[customer]) 

#use dictionary like an object
person_zach = {
    "Name": "Zach",
    "Age": 30,
    "City": "Chicago"
}

for details in person_zach:
    print(details, "-", person_zach[details])

#dictionaries can be modified by adding a new key-value pair
#referring to an item by a key name and assign a value..if there is not a key name that matches, new one will be added

#syntax - dictionaryname[key] = value
bank_customers["Zach"] = 400
print(bank_customers)
bank_customers["Alice"] = 150
print(bank_customers)

#grab single item from a list...call by key name
#use .get method to grab data from a dictionary
print(bank_customers.get("Alice"))

#delete item by key
#syntax - del dictionaryname[key]
del bank_customers["Alice"]
print(bank_customers)

#finding items in a dictionary
#syntax - key in dictionaryname

key = "Bob"
if key in bank_customers:
    print(key, "is in the bank_customers dictionary")

#matching name and values to find in a dictionary
find_name = "Zach"
value = 400

#for key value in dictionaryname.items():
for name, balance in bank_customers.items():
    if name == find_name and balance == value:
        print(find_name, "has a balance of", value)