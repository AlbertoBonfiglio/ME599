#!/usr/bin/python3

from math import pi, factorial, sqrt

class SillyMath(object):


    def gdc(self, a=0, b=0):
        retVal = 0
        modulus = a%b


        return retVal



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



