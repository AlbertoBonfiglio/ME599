#!/usr/bin/python3

from classes.robot import Robot
import matplotlib.pyplot as plt
import sys, getopt

normal_termination = 0
command_line_syntax_error = 2

helpstring = '''
mainfilter.py -e <option> -n <option>
    -h prints this help out
    -e number of epochs (default 1000)
    -n gaussian noise (default 0.25)
    '''

errorstring = '''{0} is not a valid option value. Type ./mainfilter.py -h for help'''

def selectGaussianNoise(argv):
    global _printPosition

    retNoise = 0.25
    retEpochs = 1000
    # if no argument then runs all the simulations and uses matplotlib
    if len(argv) < 1:
        return retNoise, retEpochs
    else: #parses the arguments
        try:
            opts, args = getopt.getopt(argv, "hn:e:", ["noise=", "epochs="])
        except getopt.GetoptError:
            print(helpstring)
            sys.exit(command_line_syntax_error)

        for opt, arg in opts:
            if opt == '-h':
                print(helpstring)
                sys.exit(normal_termination)

            elif opt in ("-n", "--noise"):
                try:
                    retNoise = float(arg)
                    if retNoise < 0.1:
                        print(errorstring.format(arg))
                        sys.exit(command_line_syntax_error)
                except ValueError:
                    print(errorstring.format(arg))
                    sys.exit(command_line_syntax_error)

            elif opt in ("-e", "--epoch"):
                try:
                    retEpochs = int(arg)
                    if retEpochs < 1:
                        print(errorstring.format(arg))
                        sys.exit(command_line_syntax_error)

                except ValueError:
                    print(errorstring.format(arg))
                    sys.exit(command_line_syntax_error)

    return retNoise,retEpochs


def main(args):
    filters = [1, 3, 9, 27]
    gnoise, epochs = selectGaussianNoise(args)
    sillyBot = Robot()

    data = sillyBot.getSensorReadings(epochs, gnoise)
    sillyBot.printSensorData(data, 'unfiltered')

    fig, axes = plt.subplots(nrows=4, ncols=5, sharex=True, sharey=True)

    fig.suptitle('Filter noise={0}'.format(gnoise), fontsize=20)
    axes[0, 0].plot(data)
    axes[0, 0].set_title('Unfiltered')

    idx=1
    for n in filters:
        meandata = sillyBot.filterData(data, n, usemedian=False, usenumpy=False)
        mediandata = sillyBot.filterData(data, n, usemedian=True, usenumpy=False)
        sillyBot.printSensorData(meandata, 'mean_{0}'.format(n))
        sillyBot.printSensorData(mediandata, 'median_{0}'.format(n))
        sillyBot.printStatistics(meandata, 'mean_{0}'.format(n))
        sillyBot.printStatistics(mediandata, 'median_{0}'.format(n))

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
    main(sys.argv[1:])
