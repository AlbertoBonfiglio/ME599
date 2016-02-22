#!/usr/bin/python3
import numpy
from Lab6.classes.utils import mean, median

class FilterHelper(object):

    def null_filter(self, data, width=0):
        filtered = []
        for datum in data:
            filtered.append(datum)

        return filtered


    def filterData(self, data, window=1, usemedian=False, usenumpy=True):
        if (window < 1): window = 1

        func = self.__getfilterFunction(usemedian, usenumpy)
        filtered = []
        width = int((window-1) /2)
        lenData = len(data)-1

        for n in range(lenData+1):
            if n <= (width):  #
                l = data[0:n+1]
                r = data[n+1:(n+width)+1]
                dataslice = l+r

            elif n >= (lenData - width):
                dataslice = data[n-width-1:lenData+1:]

            else:
                dataslice = data[n-width-1:n+width]

            datum = func(dataslice)
            filtered.append(datum)

        return filtered


    def __getfilterFunction(self, usemedian=False, usenumpy=True):
        if usenumpy == True:
            if usemedian == True:
                func = numpy.median
            else:
                func = numpy.mean
        else:
            if usemedian == True:
                func = median
            else:
                func = mean

        return func