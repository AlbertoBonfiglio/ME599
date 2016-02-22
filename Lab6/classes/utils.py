#!/usr/bin/python3

from math import sqrt, pi, e
import numbers
import sys
from time import clock, process_time, time, perf_counter
import numpy as np
from copy import copy, deepcopy
from webcolors import rgb_to_name


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


def root(self, a=0, b=0, c=0):
    raise NotImplementedError()


def euclidean_distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

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


def getAnyInput(msg='', var=''):
    while True:
        retval = input(msg.format(var))
        return retval

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

def get_randomlists(listlenghts, numpyarray=False):
    retval = []
    for n in listlenghts:
        value = np.random.uniform(-1.0, 1.0, size=n)
        if numpyarray:
            retval.append(value)
        else:
            retval.append(value.tolist())

    return retval

#endregion


#region Sorting Helpers
def bubble_sort(data):
    #if list is empty or only one element just return it
    if len(data) <= 1: return data

    templist = copy(data) #shallow copy

    count = len(templist)
    if count >= 2:
        while count > 0:
            index = 0 # keeps track of how the position of the last swap
            for n in range(count - 1):
                if templist[n] > templist[n+1]:
                    templist[n], templist[n+1] = templist[n+1], templist[n]
                    index = n+1
            count = index

    return templist


def quick_sort(data, randPivot=True, useLambda=False):
    #if list is empty or only one element just return it
    if len(data) <= 1: return data

    if randPivot:
        #gets a random pivot point
        pivot = np.random.choice(data, 1)
    else:
        #gets a pivot point about half way
        pivot = data[len(data)/2]

    # separates the array into less, equal or more than the pivot
    # then recursively calls quicksort for each the subarrays
    if not useLambda:
        # This is pretty much what was shown in class but without lambdas
        return (quick_sort([x for x in data if x < pivot], randPivot, useLambda) +
                [x for x in data if x == pivot] +
                quick_sort([x for x in data if x > pivot], randPivot, useLambda))
    else:
        # This is what was shown in class with lambdas
        #TODO change list comprehension to lambdas using filter(lambda x: blah blah)
        return (quick_sort([x for x in data if x < pivot], randPivot, useLambda) +
                [x for x in data if x == pivot] +
                quick_sort([x for x in data if x > pivot], randPivot, useLambda))


def insertion_sort(data):
    #if list is empty or only one element just return it
    if len(data) <= 1: return data

    templist = copy(data)
    insertionlist = []
    count = len(templist)

    if count >= 2:
        idx = np.random.randint(0, count)
        value = templist[idx]
        insertionlist.append(value)
        templist.pop(idx)

        while len(templist) > 0:
            value = templist[0]
            templist.pop(0)

            for n in range(len(insertionlist)):
                inserted = False
                if value <= insertionlist[n]:
                    insertionlist.insert(n, value)
                    inserted = True
                    break

            if not inserted: insertionlist.append(value)

        return insertionlist

    else:
        return templist


def merge_sort(data, chunks=1):
    #if list is empty or only one element just return it
    if len(data) <= 1: return data

    #breaks down the array into individual lists of [chunks] size
    lists = []
    for n in range(0, len(data), chunks):
        lists.append(data[n:n+chunks])

    #if the number of items is not even merges the last two and removes the last
    #also ordters the last two items
    count = len(lists)
    if not isEven(count):
        if (lists[count-2] > lists[count-1]):
            tempval = lists[count-1] + lists[count-2]
        else:
            tempval = lists[count-2] + lists[count-1]
        lists[count-2] = tempval
        lists.pop(count-1)

    #now loops in reverse merging and sorting two lists at a time until
    #there is ony one left (the highlander algorithm!!)
    while len(lists) > 1:
        templist = []
        for n in reversed(range(1, len(lists), 2)):
            arrayA = lists[n]
            arrayB = lists[n-1]
            #TODO change merge_arrays to a lambda for readability and encapsulation
            templist.append(merge_arrays(arrayA, arrayB))

        lists = templist

    return templist


def merge_arrays(a, b):
    merged = []
    temp = a + b
    # takes the smallest item in the temporary array, and appends it to the
    # return array until the temp array is empty
    while len(temp) > 0:
        value = min(temp)
        merged.append(value)
        idx = temp.index(value)
        del temp[idx]

    return merged


def isSorted(data):
    for n in range(len(data)-1):
        if data[n] > data[n+1]:
            return False
    return True


def isReallySorted(data):
    temp = copy(data)
    temp.sort()
    for n in range(len(data)-1):
        if data[n] != temp[n]:
            return False
    return True


#endregion


#region Timers
timers = [time, clock, process_time, perf_counter]  #different timing functions

def time_list_sort(lists, func=sorted, epochs=10, timers=[time, clock, process_time, perf_counter]):
    retval=[]
    try:
        for n in lists:
            retval.append(__timethis(func, n, epochs, timers))

        return retval

    except Exception as ex:
        print(ex)


def time_algorithms(algorithms, data, epochs=10, timers=[time, clock, process_time, perf_counter]):
    retval=[]

    try:
        for func in algorithms:
            tempval = []
            for item in data:
                value = __timethis(func, item, epochs, timers)
                if len(value) >1:
                    tempval.append(value)
                else:
                    tempval.append(value[0])

            retval.append(tempval)

        return retval

    except Exception as ex:
        print(ex)


def __timethis(func, data, epochs, timers):
    tempdata = copy(data)
    retval = []
    for timer in timers:
        print('Processing {0} {1} {2}'.format(len(data), func, timer))
        tempval = 0
        for n in range(epochs):
            t1 = timer()
            x = func(tempdata)
            tempval += (timer() - t1)

        tempval = tempval/epochs

        retval.append(tempval)

    return retval

#endregion


#region Helpers

#Convert a 3-tuple of integers, suitable for use in an rgb() color triplet,
#to its corresponding normalized color name,
#if any such name exists; valid values are html4, css2, css21 and css3, and the default is css3.

def get_colour_name(rgb, palette='css3'):
    try:
        colorname = rgb_to_name(rgb, spec=palette)
        return colorname
    except:
        return 'Undefined'

def find_colour_name(rgb):
    palettes = ['css3', 'html4', 'css2', 'css21']
    for palette in palettes:
        colour = get_colour_name(rgb, palette)
        if colour != 'Undefined': return colour

    return 'Undefined'


#endregion

#region Filters

#endregion
