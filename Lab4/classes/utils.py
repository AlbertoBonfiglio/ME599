#!/usr/bin/python3

from math import sqrt, pi, e
import numbers
import sys
from time import clock, process_time, time, perf_counter
import numpy as np
from copy import copy

#region Various Math functions

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

#endregion


#region Input Helpers
normal_termination = 0
command_line_syntax_error = 2

def getIntInput(msg='', var=''):
    while True:
        try:
            retval = int(input(msg.format(var)))
            return retval
        except ValueError as ex:
            print(ex)


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

#endregion


#region Various Quick helpers

def get_randomlists(listlenghts):
    retval = []
    for n in listlenghts:
        retval.append(np.random.uniform(-1.0, 1.0, size=n))

    return retval

#endregion


#region Sorting Helpers
def bubble_sort(list):
    templist = copy(list) #shallow copy

    count = len(templist)

    while count > 0:
        index = 0 # keeps track of how the position of the last swap
        for n in range(count - 1):
            if templist[n] > templist[n+1]:
                templist[n], templist[n+1] = templist[n+1], templist[n]
                index = n+1
        count = index

    return templist

def quick_sort(list):
    templist = copy(list) #shallow copy

    return templist

def insertion_sort(list):
    templist = copy(list) #shallow copy

    return templist

def merge_sort(list):
    templist = copy(list) #shallow copy

    return templist


def isSorted(list):
    for n in range(len(list)-1):
        if list[n] > list[n+1]:
            return False
    return True
#endregion


#region Timers
timers = [time, clock, process_time, perf_counter]  #different timing functions

def time_list_sort(lists, func=sorted):
    retval=[]
    try:
        for n in lists:
            retval.append(timethis(func, n))

        return retval
    except Exception as ex:
        print(ex)


def timethis(func, list, epochs=10):
    retval = []
    for timer in timers:
        print('Processing function {0}'.format(timer))
        tempval = 0
        for n in range(epochs):
            t1 = timer()
            x = func(list)
            tempval += (timer() - t1)

        tempval = tempval/epochs

        retval.append(tempval)

    return retval

#endregion
