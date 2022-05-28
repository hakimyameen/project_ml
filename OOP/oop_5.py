'''
Setter and getter method:
'''
'''
These methods are associated with instance variables
We can set and get the values using these methods
------------------------------------------
Setter method:
used to set values to the instance variable
setter method os also known as Mutator method
-----------------
Syntax:
def set_method_name(self,var):
        self.var = var
----------------------------------------
getter method:
used to get the values from instance variable
gettter methods as   also known as Accessor method

syntax:
def get_method_name(self):
    return self.var     
-------------------------------------------------------------------
class Student:

    #setter method
    def details(self,roll_no):
        self.roll_no = roll_no

    #getter method
    def display(self):
        return self.roll_no

s = Student()
s.details(101)
print(s.display())

#Assignment: set Name,age, adress, place, pin and return also 
----------------------------------------------------------------------
Constructor allocates a memory to a class/ object
Immediately Destructor de-allocates a memory
--------------------------------------------------------
import time
class Student:
    def __init__(self):
        print('Constructor called')
        time.sleep(2)
    def __del__(self):
        print('Destructor gets called..')
        time.sleep(2)
# call the constructor
Student()
time.sleep(3)
Student()
time.sleep(3)
Student()
#
-----------------------------------------------------

class Student:
    def __init__(self,name,age):
        self.n= name
        self.a = age
        self.std = 1
        
    def m1(self,x1):
        self.x = x1
        self.y = 340
        self.name = 'Swaroopa'
        
s = Student('AB',23)
s.m1(45)
-----------------------------------------
class Student:
    def __init__(self):
        pass
s1 = Student()
s1.name = 'Alok'
s1.age = 34
s1.salary = 67000
print('S1:',s1)

s2 = Student()
print('S2:',s2)
s2.name= 'Rashmi'
del s2
print('S2:',s2)
--------------------------------------------------------
How to add and delete instances
---------------------------------
class Student:
    def __init__(self,nm,age):
        self.nm = nm
        self.ag = age
        #del self.ag
s = Student('A',12)
print(s.__dict__)
print('Lets add new instance place')
s.place = 'Pune'
print(s.__dict__)
print('Lets remove age')
del s.ag
print(s.__dict__)
# if we want to add instances inside a class then use self
# if we want to add instances from outside the class the use object
------------------------------------------------------------

class Student:
    x = 67 #class level/static
    def m1(self):
        # print(self.x)
        # print(Student.x)
        pass

s = Student()
s.m1()
print(s.x) #67
s.x = 67000
print(s.x)
print(Student.x)

s2 = Student()
print('S2:',s2.x)
------------------------------------------------
Nested class: class inside another class
'''
class Univeristy:
    def __init__(self):
        print('Init of University')
    def u1(self):
        pass
    def u2(self):
        pass
    class College:
        def __init__(self):
            print('Init of College')
        def c1(self):
            pass

#######################
u = Univeristy()
u.College()
print('##############################')
Univeristy().College()
print('##############################')
u = Univeristy()
u.u2()
c = u.College()
c.c1()

















































