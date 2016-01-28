#!/usr/bin/python3

import matplotlib.pyplot as plt
from matplotlib.pylab import figtext
import numpy as np
from Lab3.classes.utils import *
from time import clock, process_time, time, perf_counter


timers = [time, clock, process_time, perf_counter] #different timing functions
listlen = [1, 10, 100, 1000, 10000, 100000, 1000000]


def draw_plot(values, caption):
    try:
        t_groups = len(timers)
        n_groups = len(listlen)

        pivots = []
        for n in range(t_groups):
            pivots.append([value[n] for value in values])

        print(pivots)

        with plt.xkcd():
            #plt.style.use('fivethirtyeight')

            fig, axes = plt.subplots(nrows=2, ncols=4, sharex=True, sharey=True)
            fig.suptitle('Spring damping over time',  fontsize=18, fontweight='bold')

            for n in range(t_groups):
                axes[0,0].plot(listlen, pivots[n], color=np.random.rand(3,1))





            position = np.arange(n_groups)
            width=0
            for n in range(t_groups):
                axes[0,1].bar(np.arange(n_groups) + width, pivots[n], width=0.25, color=np.random.rand(3,1))
                width +=.25

            axes[0,1].set_xlabel('Time (s)')
            axes[0,0].set_ylabel('Displacement (m)')

            axes[0,1].set_xticks(position + (width/t_groups) *2)
            #xes[0,1].set_xticklabels(timers)

            axes[0,1].axis('tight')
            #figtext(.52, .15, caption)






            plt.show()

    except Exception as ex:
        print(ex)


def get_randomlists(listlenghts):
    retval = []
    for n in listlenghts:
        retval.append(np.random.uniform(-1.0, 1.0, size=n ))

    return retval


def time_list_sort(lists):
    retval=[]
    try:
        for n in lists:
            retval.append(timethis(sorted, n))

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
            func(list)
            tempval += (timer() - t1)

        tempval = tempval/epochs

        retval.append(tempval)

    return retval


def main(argv):
    try:

        times = time_list_sort(get_randomlists(listlen))

        draw_plot(times, 'blah')

    except Exception as ex:
        print(ex)





if __name__ == '__main__':
    main(sys.argv[1:])

