#!/usr/bin/python3

import matplotlib.pyplot as plt
from Lab4.classes.utils import *

listlen = [1, 10, 100, 1000, 2000]#,  100000, 1000000]
tcaptions = ['time', 'clock', 'ptime', 'pcounter']
algorithms = [sorted, bubble_sort, insertion_sort, merge_sort, quick_sort]

def draw_plot(values, caption, timers=[process_time]):
    try:
        t_groups = len(timers)
        n_groups = len(listlen)

        with plt.xkcd():
            #plt.style.use('fivethirtyeight')

            fig, axes = plt.subplots(nrows=1, ncols=len(algorithms), sharex=False, sharey=False,  tight_layout=True, figsize=(9, 4.5))
            fig.suptitle(caption,  fontsize=18, fontweight='bold')

            #Histogram

            row = 0
            col = 0

            for algorithm in values:
                position = np.arange(n_groups)
                width = 0
                bars = []

                ax = axes[col]

                bars.append(ax.bar(np.arange(n_groups) + width, algorithm, width=0.25, color=np.random.rand(3,1)))
                width +=.25

                ax.set_xlabel('Sample Size', fontsize='small')
                ax.set_ylabel('Time (s)', fontsize='small')
                ax.set_xticks(position + (width/t_groups) *2)
                ax.set_xticklabels(listlen, fontsize='small')
                ax.legend(bars, tcaptions, fontsize='small', loc='upper left', shadow=True)
                ax.axis('tight')

                col +=1



            #for n in range(t_groups):
            #    bars.append(axes[1].bar(np.arange(n_groups) + width, pivots[n], width=0.25, color=np.random.rand(3,1)))
            #    width +=.25

            #axes[1].set_xlabel('Sample Size', fontsize='small')
            #axes[1].set_ylabel('Time (s)', fontsize='small')
            #axes[1].set_xticks(position + (width/t_groups) *2)
            #axes[1].set_xticklabels(listlen, fontsize='small')
            #axes[1].legend(bars, tcaptions, fontsize='small', loc='upper left', shadow=True)
            #axes[1].axis('tight')

        plt.show()
    except Exception as ex:
        print(ex)


def main(argv):
    try:
        lists = get_randomlists(listlen)
        times = time_algorithms(algorithms, lists, timers=[process_time])



        #times should be a matrix of
        # algorithm 1 - list 1 timer 1-n ; list 2 timer 1-n ....
        # algorithm 2 - list 1 timer 1-n ; list 2 timer 1-n ....

        #what we want is

        draw_plot(times, "Algorithm Performance Comparison", timers=[process_time])


    except Exception as ex:
        print(ex)





if __name__ == '__main__':
    main(sys.argv[1:])

