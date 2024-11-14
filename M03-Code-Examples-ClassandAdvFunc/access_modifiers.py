#encapsulation - wrap data and give them the ability to be accessible or inaccessable
#we can set variables so that other classes and outside data canot interfere or change data unless specified or used with a method
#useful to limiting bugs
#we can limit access using functions so only certain groups/people/classes can manipulate data
#provide better security and robustness

class Pet:
    def __init__(self, name, animal_type, age):
        #to make fields/attr/variables "private" we use a double underscore aka a dunder (__)
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age
    

    #methods called getters/setters
    #getter retrieve data
    #setters change/modify data

    #getters
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
    
    #setters
    def set_name(self,name):
        self.__name = name
    def set_animal_type(self,animal_type):
        self.__animal_type = animal_type
    def set_age(self,age):
        self.__age = age


pet1 = Pet("Spot","dog", 5)
#run our getters
print(pet1.get_name())
print(pet1.get_animal_type())
print(pet1.get_age())

#change pets name, age and type
pet1.set_name("Jack")
pet1.set_animal_type("Cat")
pet1.set_age(2)

#Display new values
print(pet1.get_name())
print(pet1.get_animal_type())
print(pet1.get_age())


