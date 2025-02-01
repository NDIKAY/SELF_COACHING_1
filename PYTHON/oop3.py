#!/usr/bin/python3
from math import pi
class Circle:

    def __init__(self,r):
        self.r = r

    def calculateArea(self):
        area = pi * self.r *self.r
        print(area)
Circle1 = Circle(15)
Circle2 = Circle(20)
Circle1.calculateArea()
Circle2.calculateArea()
