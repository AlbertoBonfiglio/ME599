#!/usr/bin/python3

import matplotlib.pyplot as plt
from Lab4.classes.utils import *

listlen = [1, 10, 100, 1000, 10000,  100000, 1000000]
tcaptions = ['time', 'clock', 'ptime', 'pcounter']

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
                legends.append(axes[0].plot(listlen, pivots[n], color=np.random.rand(3, 1), label= tcaptions[n]))

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
        lists = get_randomlists([101])

      #  bubblelist = bubble_sort(lists[0])
      #  insertlist = insertion_sort(lists[0])
        mergelist = merge_sort(lists[0])

        print(isSorted(mergelist))

    except Exception as ex:
        print(ex)





if __name__ == '__main__':
    main(sys.argv[1:])

