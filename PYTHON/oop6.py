#!/usr/bin/python3

class P:
    def __init__(self, x):
        self.__x = x
    
    def get_x(self):
        return self.__x
    
    def set_x(self, x):
        self.__x = x
P1 = P(42)
P2 = P(4711)
a = P1.get_x()
print(a)
P1.set_x(47)
P1.set_x(P1.get_x()+P2.get_x())
b = P1.get_x()
print(b)
