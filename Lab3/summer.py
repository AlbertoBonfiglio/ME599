#!/usr/bin/python3

import matplotlib.pyplot as plt
from matplotlib.pylab import figtext
import numpy as np
from Lab3.classes.utils import *




def draw_plot(states, times, caption):
    try:
        with plt.xkcd():
            #plt.style.use('fivethirtyeight')
            fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
            fig.suptitle('Spring damping over time',  fontsize=18, fontweight='bold')

            displacement = [n[0] for n in states]
            ax.plot(times, displacement)

            ax.set_xlabel('Time (s)')
            ax.set_ylabel('Displacement (m)')
            ax.axis('tight')
            figtext(.52, .15, caption)
            plt.show()

    except Exception as ex:
        print(ex)


def get_lists(listlenghts):
    retval = []
    for n in listlenghts:
        retval.append(np.random.uniform(-1.0, 1.0, size=n ))

    return retval


def main(argv):
    listlen = [1, 10, 100, 1000, 10000, 100000, 1000000]
    try:
        lists = get_lists(listlen)

    except Exception as ex:
        print(ex)





if __name__ == '__main__':
    main(sys.argv[1:])

