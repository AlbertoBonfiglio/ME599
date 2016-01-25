#!/usr/bin/python3

from Lab2.classes.sensor import generate_sensor_data, print_sensor_data
import numpy

class Robot(object):

    def __init__(self):
        self.data = None

    def getSensorReadings(self, n=1000, noise=0.05):
        self.data = generate_sensor_data(n, noise)
        return self.data


    def printSensorData(self, filename):
        print_sensor_data(self.data, filename)



    def null_filter(self, data, width=0):
        filtered = []
        for datum in data:
            filtered.append(datum)

        return filtered


    def filterData(self, data, width=1, usemedian=False):
        filtered = []

        if usemedian == True:
            func = numpy.median
        else:
            func = numpy.mean

        window = (width*2) + 1
        lenData = len(data)-1
        meandata = 0
        for n in range(lenData):
            slice = []
            if n <= (width):  #
                l = data[0:n+1]
                r = data[n+1:(n+width)+1]
                slice = l+r

            elif n >= (lenData - width):
                slice = data[n-width-1:lenData+1:]

            else:
                slice = data[n-width-1:n+width]


            datum = func(slice)
            filtered.append(datum)

        return filtered

