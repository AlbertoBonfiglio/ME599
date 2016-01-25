#!/usr/bin/python3

from Lab2.classes.robot import Robot
import matplotlib.pyplot as plt


def main():
    filters = [1, 3, 9, 27]
    sillyBot = Robot()

    data = sillyBot.getSensorReadings(5000, 0.05)
    sillyBot.printSensorData(data, 'unfiltered')

    fig, axes = plt.subplots(nrows=4, ncols=5, sharex=True, sharey=True)
    axes[0, 0].plot(data)
    axes[0, 0].set_title('Unfiltered')

    idx=1
    for n in filters:
        meandata = sillyBot.filterData(data, n, usemedian=False, usenumpy=False)
        mediandata = sillyBot.filterData(data, n, usemedian=True, usenumpy=False)
        sillyBot.printSensorData(meandata, 'mean_{0}'.format(n))
        sillyBot.printSensorData(mediandata, 'median_{0}'.format(n))

        axes[0, idx].plot(meandata)
        axes[0, idx].set_title('mean = {0}'.format(n))

        axes[1, idx].plot(mediandata)
        axes[1, idx].set_title('median = {0}'.format(n))


        meandata = sillyBot.filterData(data, n, usemedian=False, usenumpy=True)
        mediandata = sillyBot.filterData(data, n, usemedian=True, usenumpy=True)
        axes[2, idx].plot(meandata)
        axes[2, idx].set_title('NP mean = {0}'.format(n))

        axes[3, idx].plot(mediandata)
        axes[3, idx].set_title('NP median = {0}'.format(n))

        idx += 1

        sillyBot.printSensorData(meandata, 'mean_{0}'.format(n))
        sillyBot.printSensorData(mediandata, 'median_{0}'.format(n))

    plt.show()

if __name__ == "__main__":
    main()
