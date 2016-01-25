#!/usr/bin/python3

from math import sqrt, pi, e
import numbers

def getIntInput(msg='', var=''):
    while True:
        try:
            retval = int(input(msg.format(var)))
            return retval
        except ValueError as ex:
            print(ex)


def isEven(n):
    if (n % 2 == 0):
        return True
    else:
        return False


def mean(data):
    tempVal = sum(data)
    return float(tempVal/len(data))


def median(data):
    temp = sorted(data)
    if not isEven(len(data)):
        index = int((len(data)-1)/2)
        retVal = temp[index]
    else:
        index = int((len(data)-1)/2)
        left = temp[index]
        right = temp[index+1]
        retVal = (left+right)/2
    return retVal


def factorialStirling(n):
    #using stirling's Approximation
    retval = sqrt(2*pi*n) * (n/e)**n

    return int(retval)

def factorial(n):
    if n == 0: return 1
    if n < 0: raise ValueError('N must be either 0 or a positive integer')
    if (n - round(n)) == 0:
        n = int(abs(n))
    if not isinstance(n, numbers.Integral): raise ValueError('Dammit Jim! N must be an integer')

    retval = n
    while n > 1:
        t = n-1
        retval, n = retval * t, t

    return int(retval)