from unittest import TestCase
from random import randint
from math import pi
from Lab5.classes.circle import Circle

class TestCircle(TestCase):

    def test_area(self):
        radius = randint(1,100)
        area = pi * (radius ** 2)

        obj = Circle(radius)

        self.assertEquals(obj.area(), area)


    def test_circumference(self):
        radius = randint(1,100)
        circumference = 2 * pi * radius

        obj = Circle(radius)

        self.assertEquals(obj.circumference(), circumference)

    def test_diameter(self):
        radius = randint(1,100)
        diameter = radius * 2

        obj = Circle(radius)

        self.assertEquals(obj.diameter(), diameter)
