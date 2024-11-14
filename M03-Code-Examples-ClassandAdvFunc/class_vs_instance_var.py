#classes can represent real world objects with data and behavior that can be modified and changed

#if we want the attribute/data to be blank until we create a class we can use instance variables
#instance variable can be set or changed upon the creation of an object/instance
#class variables - do not change upon the creation/instantiation of an object BUT can be changed afterwards if needed

#create a class called Dog.  Dog will have a couple of attributes - name and animal.  Dog will always have the class variable of animal = "dog", but every dog can have a different name.  So use our instance variable (name) to set the name of the dog upon creation

class Dog:
    #class variable
    animal = "Dog"
    #anytime we create a new dog, it will always have animal = "dog".  If we need to change it later, we can

    #instance variables are used in arguments/parameters when creating an instance in order to set attributes upon creation
    #constructors - initialize the instance variables with some data that the user or other parts of the program provide upon creation.  It is null until we give it data.
    #constructors are special methods/functions
    #the self keyword is used when creating an instance variable
    #self = that individuals instance value or data (ie internal state)
    #__init__ = constructor keyword in python

    #make a method or function in a class we just use the same syntax we do with a function

    def __init__(self,name,age):
        #name is going to be whatever you put in the parenthesis
        self.name = name
        self.age = age

    #common behavior can be created with functions
    def bark(self):
        print("WOOF!!!!")



dog1 = Dog("Zach",8)
print(dog1.name)
print(dog1.age)
#method call or object function call
dog1.bark()

dog2 = Dog("Spot",7)
print(dog2.name)
print(dog2.age)
dog2.bark()

#class variables should be the same
print(dog1.animal)
print(dog2.animal)


#class variables can change after creating the object
dog2.animal = "Cat"
print(dog2.animal)


#use inputs to set internal state or instance variables.
dog_name = input("What is the dog's name? ")
dog_age = int(input("What is the dog's age? "))

dog3 = Dog(dog_name,dog_age)
print(dog3.name)
print(dog3.age)