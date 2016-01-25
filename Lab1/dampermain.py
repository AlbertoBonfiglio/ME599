#!/usr/bin/python3

# Help for command line argument use was taken from
# http://www.tutorialspoint.com/python/python_command_line_arguments.htm


from classes.damper import Damper
import sys, getopt
import numpy
import matplotlib.pyplot as plt

#Constants
normal_termination = 0
command_line_syntax_error = 2

helpstring = '''
dampermain.py -o <option> -p <option>
    -h prints this help out

    -o options:
        0 = all three simulations at once (default if omitted)
        1 = m = 1.0, k = 1.0, c = 0.0, x = 1.0, x_dot = 0.0
        2 = m = 1.0, k = 1.0, c = 1.0, x = 1.0, x_dot = 0.0
        3 = m = 1.0, k = 1.0, c = 1.0, x = 1.0, x_dot = 1.0

     -p options:
        0 = do not print individual positions to the console
        1 = print individual positions to the console

    Examples:
    To run the 2nd simulation WITH matplotlib and output enabled (can be viewed in Gnuplot)
      run ./dampermain.py -o2 -p1  > test

    To run the 2nd simulation WITHOUT matplotlib (can be viewed in Gnuplot)
      run ./dampermain.py -o2 -p0  > test

    To run all simulations at once with output ENABLED
      run ./dampermain.py -p1 > test (can be viewed in Gnuplot)

    To run all simulations at once with output DISABLED
      run ./dampermain.py -p0 > test (cannot be viewed in Gnuplot)
    '''

errorstring = '''{0} is not a valid option value. Type dampermain.py -h for help'''

m = 0
k = 1
c = 2
x = 3
x_dot = 4

_paramsSet = [(1.0, 1.0, 0.0, 1.0, 0.0),
              (1.0, 1.0, 1.0, 1.0, 0.0),
              (1.0, 1.0, 1.0, 1.0, 1.0)]

#Variables
_outputArray = []
_printPosition = False

def select(argv):
    global _printPosition

    retval = 0
    # if no argument then runs all the simulations and uses matplotlib
    if len(argv) < 1:
        return 0
    else: #parses the arguments
        try:
            opts, args = getopt.getopt(argv, "ho:p:", ["option=", "print="])
        except getopt.GetoptError:
            print(helpstring)
            sys.exit(command_line_syntax_error)

        for opt, arg in opts:
            if opt == '-h':
                print(helpstring)
                sys.exit(normal_termination)

            elif opt in ("-o", "--option"):
                try:
                    retval = int(arg)
                    if retval < 0 and retval >3:
                        print(errorstring.format(arg))
                        sys.exit(command_line_syntax_error)
                except ValueError:
                    print(errorstring.format(arg))
                    sys.exit(command_line_syntax_error)

            elif opt in ("-p", "--print"):
                try:
                    optval = int(arg)
                    if optval == 1:
                        _printPosition = True
                    else:
                        _printPosition = False
                except ValueError:
                    print(errorstring.format(arg))
                    sys.exit(command_line_syntax_error)

    return retval


def getDamperData(_tuple, _out=False):
    _damper = Damper(m=_tuple[m], k=_tuple[k], c=_tuple[c],)
    retval = _damper.dampOverTime(x=_tuple[x], x_dot=_tuple[x_dot], t=0.01, epoch=1000, out=_out)
    return retval


def getValues(selectedValue, _out=False):
    retval = []
    if selectedValue == 0:
        for n in range(len(_paramsSet)):
            _tuple = _paramsSet[n]
            retval.append(getDamperData(_tuple, _out))
    else:
        _tuple = _paramsSet[selectedValue - 1]
        retval.append(getDamperData(_tuple, _out))

    return retval

# Plots the various functions .
# From an example at http://matplotlib.org/examples/pylab_examples/subplots_demo.html
def showGraphs(data):
    x = numpy.arange(0, 1000, 1)
    f, (ax1, ax2, ax3) = plt.subplots(3, sharex=True, sharey=False)
    ax1.plot(x, data[0])
    ax1.set_title('Damping Simulations')
    ax2.plot(x, data[1])
    ax3.plot(x, data[2])
    f.subplots_adjust(hspace=0.2)
    plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
    plt.show()

def showGraph(data):
    x = numpy.arange(0, 1000, 1)
    f, (ax1) = plt.subplots(1, sharex=True, sharey=False)
    ax1.plot(x, data)
    ax1.set_title('Damping Simulations')
    f.subplots_adjust(hspace=0.2)
    plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
    plt.show()

def main(argv):
    #Gets the selected arguments
    selectedValue = select(argv)

    #retrieves the data according to the selected argument
    _outputArray = getValues(selectedValue, _printPosition)
    if selectedValue != 0:
        for n in range(len(_outputArray)):
            _array = _outputArray[n]
            if _printPosition != True:
                for x in range(len(_array)):
                    value = _array[x]
                    print('{0} {1}'.format(x, value))
            else:
                showGraph(_array)

    else:
        showGraphs(_outputArray)


if __name__ == "__main__":
    # Starts the script and passes any argument to the main function
    main(sys.argv[1:])