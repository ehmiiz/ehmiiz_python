# Functions
"""
functions:
you can import a function using the import keyword
however, how does the import keyword work locally?
1. you can import directly if the .py files (both function and the
import file) are placed in the same folder
2. from your new program (not the function) you can import sys and append 
the syspath of the function:
sys.path.append('/home/ehmiiz/git/pywsh/crash_course')
"""


# Classes
"""
Properties:
self.property = property

Method:
def im_a_method(self):
    self.property = 1


Parent & Child classes
- Parent and Child must be part of the same file
- Parent class must be first
- the child class calls the parents __init__ the function: super().__init__(whatever, it, needs)
- super() function is a special function that allows to call a method from the parent
- It calls the __init__ method from the car class, giving the child all attributes of that class.
- The name `super` calls from the parent class being a super class, and the child being a subclass.
- You can override parent class methods by giving the child class a method with the same name.

Composition
- If a class becomes to lengthy, you can use composition to create a class of a part of the class:
Car -> ElectricCar *To many attributes* -> Creates battery class before ElectricCar
Class Battery:
    X
in car: self.battery = Battery()
results in:
instance.electriccar.battery.describe()

The benifit of this is that we can no go bananas with describing the battery class
without "cluttering" the electriccar class.


"""