# #video for this code: https://www.youtube.com/watch?v=oROcVrgz91Y&t=1s&ab_channel=thenewboston
# class Parent():
#   def print_last_name(self):
#     print('Roberts')

# class Child(Parent):
#   def print_first_name(self):
#     print("Bucky")
#    #can override using this method 
#   #def print_last_name(self):
#    # print("Hamby")


# bucky = Child()
# bucky.print_first_name()
# bucky.print_last_name()

#non-inheritance polymorphism
#polymorphism - functions have the same name but do different things
#group by behavior

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("VRRROOOOOM")

# class Boat:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("SAIL")

# class Plane:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#     def move(self):
#         print("FLY")


#inhertiance based polymorphism - Inherit a class and override methods or functions

#super or parent class
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    #default behavior
    def move(self):
        print("MOVE!")

#inhertiance and override the move method/function
class Car(Vehicle):
    def move(self):
        print("Vroom")

class Plane(Vehicle):
    def move(self):
        print("Fly")

class Boat(Vehicle):
    def move(self):
        print("Sail")



car1 = Car("Ford","Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

car1.move()
boat1.move()
plane1.move()