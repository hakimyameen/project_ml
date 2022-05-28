'''
polymorphism means the same function name
(but different signatures) being used for different types.
--------------------------
def add(a, b, c=10):
    print(a + b + c)

add(1, 2)
add(2, 3, 4)
---------------------------------
def add(*args):
    print(sum(args))

add()
add(1,2)
add(2,3,5)
add(2,3,45,6,7)
------------------------------------------------------------------
Overloading Types:
Use same method but with different signature/no. of arguments
def m1()
def m1(a,b)
def m1(x,y,z)

1. Method Overloading
-------------------------------
class Sample:
    #lets implement different behaviour of m1()
    def m1(self):
        print('No arg')
    def m1(self,a):
        print('One arg')
    def m1(self,x,y):
        print('Two args')


s = Sample()
s.m1()
s.m1(10)
s.m1(10,70)
'''
'''
In python, method overloading is not possible,
bcz it will call last recent method always
so only
s.m1(10,70) will get executed
-----------------------------
If we still want to implement Method overloading then
use *args(variable length argument.

class Sample:
    def m1(self,*args):
        print('No arg')
    
s = Sample()
s.m1()
s.m1(10)
s.m1(10,70)
------------------------------------
Assignment: How to implement method overloading in Python??
--------------------------------------------------------------
2. Constructor overloading:
same name but different signature
def __init__()
def __init__(a)
def __init__(x,y,z)
----------------------------------------------
class Sample:
    def __init__(self):
        print('No arg')
    def __init__(self,x):
        print('One arg')
    def __init__(self,p,q):
        print('Two args')

#Sample() #this wont get executed
# constructor overloading is not possible
# bcz it wil also call last recent init method
# so u must have to pass 2 argumnts
s = Sample(2,3)
s.__init__(40,50)

# Assignment: Implement Constructor overloading using Python
--------------------------------------------------------------
Operator Overloading:
Different nature of operator on different inputs
----------------------------
class Library:
    def m1(self,books):
        self.books= books
        return self.books

l1 = Library()
print(l1.m1(500))

l2 = Library()
print(l2.m1(700))

print(l1.m1('500')+l2.m1('700'))
'''
class Library:
    def __init__(self,books):
        self.books = books
    # Magic method/dunder method
    def __add__(self, other):
        return self.books + other.books

    def __mul__(self, other):
        return self.books * other.books
l1 = Library(100)
l2 = Library(200)
# lets add two objects
print(l1+l2)
print(l2*l1)








