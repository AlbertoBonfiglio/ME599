from unittest import TestCase
from Lab2.classes.sillymath import SillyMath
import numpy
import fractions

class TestSillyMath(TestCase):

    def test_gdc(self):

        obj = SillyMath()
        a = numpy.random.randint(-23450, 23540)
        b = numpy.random.randint(-23450, 23540)

        x = fractions.gcd(a, b)
        y = obj.gdc(a, b)

        print(a,b,x,y)
        assert x==y


    def test_gdc2(self):

        obj = SillyMath()
        a = numpy.random.randint(-23450, 23540)
        b = numpy.random.randint(-23450, 23540)

        x = fractions.gcd(a, b)
        y = obj.gdc2(a, b)

        print(a,b,x,y)
        assert x==y


    def test_gdcWithAEqualToZero(self):

        obj = SillyMath()
        a = 0
        b = numpy.random.randint(-23450, 23540)

        self.assertRaises(ValueError, obj.gdc, a, b)


    def test_gdcWithBEqualToZero(self):

        obj = SillyMath()
        a = numpy.random.randint(-23450, 23540)
        b = 0

        self.assertRaises(ValueError, obj.gdc, a, b)
