'''
OOP characteristics:
1. Inheritance
2. Abstraction
3. Encapsulation
4. Polymorphism
'''
'''
1. Inheritance:
Its a relationship
we inherit something from someone
Parent--- child relationship

Creating(deriving) a new class(child class) from parent class(base class) is nothing but 
an Inheritance

Example:
class Universty: #parent
        pass
class Institutes(Universty):
        pass
-------------------------------------------------------
class Parent:
    print('This is parent class')
    def m1(self):
        print('Parent m1')
class Child(Parent):
    pass

c = Child()
c.m1()
--------------------------------------------  
# Overriding in Python:
When we have same method with same name in both parent asn child class
then
Method in parent will be overridden in child    
and method in child overrides method in parent
---------------------------------------------------------
class Parent:
    print('This is parent class')
    def m1(self):
        print('Parent m1')

class Child(Parent):
    def m1(self):
        print('Child m1')

c = Child()
c.m1()
-------------------------------------------------------

class Parent:
    print('This is parent class')
    def money(self):
        print('Parent money')
    def Car(self):
        pass
# now if child has very less amount
# then he/she must have to take help of Parent
class Child(Parent):
    def money(self):
        print('Child money')
        super().money()
    def budget(self):
        #super().money()
        #super(Child, self).money()
        super(Child, self).money()
        super(Child, self).Car()

c = Child()
c.money()
c.budget()
-----------------------------------------------------
class Parent:
    def __init__(self,place):
        self.plac =place
        print('Init of parent')
        #print(self.plac)

class Child(Parent):
    def __init__(self,nm,age):
        self.nm = nm
        self.age = age
        super().__init__('Pune')
        print('Init of Child')
        print(self.nm,self.age,self.plac)

c =  Child('Nilam',22)
------------------------------------------------
Types of Inheritance:
1. Single inheritance= One parent and One child
2. Multilevel inheritance = Super_Parent--Parent--child

'''
class GrandFather:
    def money(self):
        print('Money from Grand father')

class Father(GrandFather):
    def money(self):
        #super().money()
        print('Money from father')

class Child(Father):
    def money(self):
        super().money()

c = Child()
c.money()






