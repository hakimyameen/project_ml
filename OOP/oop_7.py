'''
Multiple Inheritance:
We can have more than one Parent
and multiple child

-------------------------------------
class Father:
    def money(self):
        print('Father\'s money')
class Mother:
    pass
    def money(self):
        print('Mother\'s money')
# when we want to inherit multiple parents
# then we must have to think abt priority
class Child(Father,Mother):
    def money(self):
        super().money()
c = Child()
c.money()
--------------------------------------

class A:
    def m1(self):
        print('m1')
class B:
    pass
class C:
    def m1(self):
        print('m1')
class D(B,A,C):
    def m1(self):
        print('m1')
        super().m1()

d = D()

# MRO: Method resolution order
# It tell us how the methods are accessed from the class according to hierarchy/priority
# It gives a sequence of method access/how methods are accessed
# in order to check MRO we need a class(Child/Derived) name

print(D.mro())
'''
class X:
    pass
class Y:
    pass
class Z():
    pass
class P(X,Z):
    pass
class Q(Y,X):
    pass
class Child(X,Q,Z):
    pass
print(Child.mro())


























