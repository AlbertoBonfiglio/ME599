#!/usr/bin/python3

from math import pi, factorial, sqrt

class SillyMath(object):


    def gdc(self, a=0, b=0):
        if b == 0:
            raise ValueError('Cannot divide by 0')
        if a == 0:
            raise ValueError('Variable ''a'' cannot be zero')
        if a == b:
            return b
        else:
            return self.__iterateGDC(a, b)


    def __iterateGDC(self, a, b):
        while True:
            remainder = a%b
            if remainder == 0:
                return b
            else:
                a, b = b, remainder


    def gdc2(self, a=0, b=0):
        # Interestingly I found out this is the same implementation as
        # the gdc function in fractions.py ...
        while b:
            a, b = b, a%b

        return a


    def estimate_pi(self):
        SRConst = float((2 * sqrt(2)) / 9801)
        threshold = 1e-15

        k = 0
        retVal = 0
        tempVal = 1
        while not (abs(tempVal) < threshold):
            srn = self.__getSRNumerator(k)
            srd = self.__getSRDenominator(k)
            tempVal = SRConst * float(srn/srd)
            retVal += tempVal
            k += 1
        return float(1 / retVal)

    def compare_pi(self, x=0):
        if pi == x:
            return True
        return False


    def __getSRNumerator(self, k=0):
        return float(factorial(4*k) * (1103 + 26390 * k))

    def __getSRDenominator(self, k=0):
        return float((factorial(k)**4) * (396 ** (4 * k)))



