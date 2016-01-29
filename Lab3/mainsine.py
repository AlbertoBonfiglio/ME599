#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np


def getSample(size=10):
    retval = 0
    for n in range(size):
        retval += np.random.uniform(0.0, 1.0)

    return retval


def getSamples(size=10000):
    valueArray = []
    for n in range(size):
        valueArray.append(getSample())

    return valueArray


def sinePlot():
    start, stop = 0, 4 * np.pi
    x = np.linspace(start, stop)

    fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
    fig.suptitle('Sine function {0}-{1:.2f}'.format(start, stop), fontsize=20)

    ax.plot(x, np.sin(x))
    ax.set_xlabel('Angle [rad]')
    ax.set_ylabel('sin(x)')
    ax.axis('tight')

    plt.show()


def sampleHistoPlot():
    samples = [10, 100, 1000, 10000, 100000, 1000000]

    fig, axes = plt.subplots(nrows=2, ncols=3, sharex=False, sharey=False)
    fig.suptitle('CLT', fontsize=20)

    x, y = 0, 0
    for n in range(len(samples)):
        if (n+1) % 4 == 0:
            x, y = 0, y+1

        ax = axes[y, x]

        bins = samples[n]
        if bins > 100:
            bins = 250

        ax.hist(getSamples(samples[n]), bins, normed=1, facecolor='g', alpha=0.75)
        ax.set_xlabel('bins')
        ax.set_ylabel('samples')
        ax.axis('tight')

        x += 1

    plt.show()


def main():
    sinePlot()
    sampleHistoPlot()








if __name__ == '__main__':
    main()