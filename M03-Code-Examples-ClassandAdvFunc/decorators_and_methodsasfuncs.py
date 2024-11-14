#In Python, a decorator is a function that takes another function as input and extends or modifies its behavior without explicitly modifying the original function's code. Decorators are a powerful way to add functionality to existing functions or classes, promoting code reusability and separation of concerns.

#a decorator is a "wrapper" for a function that adds code to the function in order to make it do something extra

def my_decorator(func):
    def wrapper():
        print("Something added before the function")
        func()
        print("Something added after the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

#say we want a class.. but that class is just a group of functions
#ie the class is used to organize functions instead of holding data
#I want a class that contains a ton of math utilities to add, multiply, divide, etc.. numbers

class MyMathUtils:
    #a static method is one that DOES NOT require an object or data
    @staticmethod
    def add(x,y):
        return x + y
    
    @staticmethod
    def multiply(x,y):
        return x * y
    
print(MyMathUtils.add(9,10))
print(MyMathUtils.multiply(2,4))