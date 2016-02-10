#!/usr/bin/python3
from math import pi

#TODO test code
class circle(object):

    def __init__(self, radius=1):
        pass

    def area(self):
        return pi * (self.radius**2)


    def circumference(self):
        return 2 * pi * self.radius


    def diameter(self):
        return 2 * self.radius