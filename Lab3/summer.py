#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
from classes.utils import *
from time import clock, process_time, time, perf_counter


timers = [time, clock, process_time, perf_counter]  #different timing functions
tcaptions = ['time', 'clock', 'ptime', 'pcounter']
listlen = [1, 10, 100, 1000, 10000,  100000, 1000000]


def get_randomlists(listlenghts):
    retval = []
    for n in listlenghts:
        retval.append(np.random.uniform(-1.0, 1.0, size=n ))

    return retval


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

            fig, axes = plt.subplots(nrows=1, ncols=2, sharex=False, sharey=False,  tight_layout=True, figsize=(9, 4.5))
            fig.suptitle(caption,  fontsize=18, fontweight='bold')
            #plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
            #Scatter plot
            legends = []
            for n in range(t_groups):
                legends.append(axes[0].plot(listlen, pivots[n], color=np.random.rand(3, 1), label=tcaptions[n]))

            axes[0].legend(shadow=True, loc='upper left', fontsize='small')
            axes[0].set_xlabel('Sample Size', fontsize='small')
            axes[0].set_ylabel('Time (s)',fontsize='small')
            axes[0].set_xticklabels(listlen, fontsize='small')
            #axes[0, 0].set_yticks(MaxNLocator(), fontsize='small')

            #Histogram
            position = np.arange(n_groups)
            width = 0
            bars = []
            for n in range(t_groups):
                bars.append(axes[1].bar(np.arange(n_groups) + width, pivots[n], width=0.25, color=np.random.rand(3,1)))
                width +=.25

            axes[1].set_xlabel('Sample Size', fontsize='small')
            axes[1].set_ylabel('Time (s)', fontsize='small')
            axes[1].set_xticks(position + (width/t_groups) *2)
            axes[1].set_xticklabels(listlen, fontsize='small')
            axes[1].legend(bars, tcaptions, fontsize='small', loc='upper left', shadow=True)
            axes[1].axis('tight')


    except Exception as ex:
        print(ex)


def main(argv):
    try:

        times = time_list_sort(get_randomlists(listlen), sorted)

        sums = time_list_sort(get_randomlists(listlen), sum)

        draw_plot(times, 'Sort comparison')

        draw_plot(sums, 'Sum comparison')
        plt.show()

    except Exception as ex:
        print(ex)





if __name__ == '__main__':
    main(sys.argv[1:])

