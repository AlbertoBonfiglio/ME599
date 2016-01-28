#!/usr/bin/python3

from math import sqrt, pi, e
import numbers
import sys

normal_termination = 0
command_line_syntax_error = 2


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


def percent_within_StdDev(data, stddev=0, multiplier=1):
    meanval = mean(data)
    leftboundary = meanval - (stddev*multiplier)
    rightboundary = meanval + (stddev*multiplier)

    counter = 0
    for n in data:
        if n > leftboundary and n < rightboundary:
            counter +=1

    return counter/len(data)


def get_floatparam(arg, default=0.0, minVal=0.0, maxVal=0.0):
    errorstring = '{0} is not a valid option value.'
    retval = default
    try:
        retval = float(arg)
        if retval < minVal and retval >maxVal:
            print(errorstring.format(arg))
            sys.exit(command_line_syntax_error)
    except ValueError:
        print(errorstring.format(arg))
        sys.exit(command_line_syntax_error)

    return retval

def get_intparam(arg, default=0, minVal=0, maxVal=0):
    errorstring = '{0} is not a valid option value.'
    retval = default
    try:
        retval = int(arg)
        if retval < minVal and retval >maxVal:
            print(errorstring.format(arg))
            sys.exit(command_line_syntax_error)
    except ValueError:
        print(errorstring.format(arg))
        sys.exit(command_line_syntax_error)

    return retval
