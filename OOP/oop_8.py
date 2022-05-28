'''
Encapsulation in Python:
# class acts as a container in which we can hid Members
# members  means: Properties + behaviour
# Variables + Methods are hidden to outside world(direct access is not possible)

# Encapsulation == Data Hiding/Hiding of Members
-------------------------------------------------------
Example: class in python

class Sample:
    x = 60
    def m1(self):
        pass


# We cant access x and m1() directly outside the class
print(x)
m1()
_-----------------------------------
In other programming lang. we have specific access modifiers
public

private
protected

unfortunately we dont have these modifiers

Python does not contain Public private and protected terms

But we can implement then using _(underscore) convention
Variable/method without underscore is public in that scope
Variable/method with _ underscore is protected in that scope
Variable/method with __  underscore is private in that scope
--------------------------------------------
class Sample:
    public = 100
    _protected = 200
    __private = 300

    print(__private)
    print(_protected)

s = Sample()
print(s.public)
print(s._protected)
# private variable is completely hidden from outside world
#print(s.__private)
###########################################################
# If private member i want to access then we can access
# Using Name mangling technique
print(dir(s))
print(s._Sample__private)
s._Sample__private = 400
print(s._Sample__private)
---------------------------------------------------------
Hide the methods

---------------------------------------------------------
class Sample:
    def m1(self):
        print('Public m1 ')

    def _m2(self):
        print('Protected m2')

    def __m3(self):
        print('Private m3')

class Test(Sample):
    def m4(self):
        #self.m1()
        #Sample.m1()
        super().m1()
        super()._m2()
        super()._Sample__m3()

t = Test()
t.m4()
------------------------------------------
s = Sample()
s.m1() #directly available
s._m2() # indirectly its available

s._Sample__m3() # completely hidden
'''
'''

Abstraction:
Information Hiding
It is implemented using Abstract class


In python we have normal class.
If we want to make a normal as an abstract class then we have to first import
ABC(Abstract Base Class) class,Then this ABC class we have to inherit in normal class
This is just a partial abstraction
In order to make complete abstract class 
we have to add at least one abstract method

What is abstract method???
a normal/instance method if we want to make it abstract then 
use @abstractmethod decorator
To use above decorator we have to import it from abc module
-------------------------------------------------------
from abc import ABC,abstractmethod
class Sample(ABC):

    @abstractmethod
    def m1(self):
        pass

# We cant instantiate abstract class
# means we cant create an object of an abstract class
class Sampel2(Sample):
    pass
s2 = Sampel2()
----------------------------------------------

from abc import ABC,abstractmethod
class Sample(ABC):

    @abstractmethod
    def m1(self):
        pass
     # in abstract class we can also add non abstract methods
    #@abstractmethod
    def my_method(self):
        print('This is instance method')

# This is not allowed at all
# we cant instantiate ABC
#s =  Sample()
#s.m1()

#class Child(Sample):
    #pass
#c =  Child()
#c.m1()
#------------------------------------------------
# In above case we are just creating an object of child class
# and trying to access m1() from Sample class
# which is again not allowed
# why???????
# Rule is: As Sample class is not normal class, n its an abstract class
# so implementation of abstract method(m1()) in child class is Mandatory
class Child(Sample):
    def m1(self):
        print('Implementation of Abstract method m1')
    
c =  Child()
c.m1()
c.my_method()
--------------------------------------------------------
'''
from abc import ABC
class Shape(ABC): #abstract classdef calculate_area(self): #abstract methodpassclass Rectangle(Shape):
  length = 5
  breadth = 3
  def calculate_area(self):
      return self.length * self.breadth

class Circle(Shape):
  radius = 4
  def calculate_area(self):
      return 3.14 * self.radius * self.radius

#rec = Rectangle() #object created for the class 'Rectangle'
cir = Circle() #object created for the class 'Circle'
#print("Area of a rectangle:", rec.calculate_area()) #call to 'calculate_area' method defined inside the class 'Rectangle'
print("Area of a circle:", cir.calculate_area()) #call to 'calculate_area' method defined inside the class 'Circle'.


























