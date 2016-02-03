#!/usr/bin/python3

from classes.smd import SpringMassDamper
import matplotlib.pyplot as plt
from matplotlib.pylab import figtext
import sys, getopt
from classes.utils import *
import random

helpstring = '''
gerryspringer.py
    -h prints this help out
    -m  or --mass=   mass in kilos (default between 1, 10.0)
    -k  or --spring= spring coeff  (default between 1, 3.0)
    -c  or --damp=   damp coeff    (default between 0.01, 1.0)
    -t  or --time=   sim time      (default between 25, 500)
    -dt or --delta=  time slice    (default between 0.001, 0.1)
    -x  or --pos=    initial pos   (default between 0, 10.0)
    -xd or --vel=    initial vel   (default between 0.1, 5.0)
    e.g. ./gerryspringer.py -m3 --vel=4 will simulate a system
        where the mass is 3 kg, the initial velocity is 5m/s
        all other parameters will be randomly generated
    '''

shortParams = 'hm:k:c:t:dt:x:xd:'
longParams = ['help','mass=', 'spring=', 'damp=', 'time=', 'delta=', 'pos=', 'vel=']


def get_parameters(argv, shortparams='h', longparams=[help]):
    mass = random.uniform(1, 10.0)
    spring = random.uniform(1, 3.0)
    damp = random.uniform(0.01, 0.5)
    t = random.randrange(25, 500)
    dt = random.uniform(0.1, 0.001)
    x = random.uniform(0, 10.0)
    x_dot = random.uniform(0.1, 5.0)

    # if no argument then runs all the simulations and uses matplotlib
    if len(argv) < 1:
        return mass, spring, damp, t, dt, x, x_dot

    else: #parses the arguments
        try:
            opts, args = getopt.getopt(argv, shortParams, longParams)
        except getopt.GetoptError:
            print(helpstring)
            sys.exit(command_line_syntax_error)

        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print(helpstring)
                sys.exit(normal_termination)

            elif opt in ("-m", "--mass"):
                mass = get_floatparam(arg, mass, 1, 10.0)

            elif opt in ("-k", "--spring"):
                spring = get_floatparam(arg, spring, 1, 3.0)

            elif opt in ("-c", "--damp"):
                damp = get_floatparam(arg, damp, 0.01, 1.0)

            elif opt in ("-t", "--time"):
                t = get_intparam(arg, t, 25, 500)

            elif opt in ("-dt", "--delta"):
                dt = get_floatparam(arg, dt, 0.001, 0.1)

            elif opt in ("-x", "--pos"):
                x = get_floatparam(arg, dt, 0, 10.0)

            elif opt in ("-xd", "--vel"):
                x_dot = get_floatparam(arg, dt, 0.1, 5.0)

    return mass, spring, damp, t, dt, x, x_dot


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


def main(argv):

    mass, spring, damp, t, dt, x, x_dot = get_parameters(argv, shortParams, longParams)

    try:
        caption = 'Initial conditions:\nM={0:.2f} Kg, K={1:.2f}, C={2:.2f}ns/m \n t={3}s, dt={4:.3f}s\n x={5:.3f}m, xdot={6:.3f}ms'.format(mass, spring, damp, t, dt, x, x_dot)

        gerry = SpringMassDamper(mass, spring, damp, t, dt)
        states, times = gerry.simulate(x, x_dot)
        draw_plot(states, times, caption)

    except Exception as ex:
        print(ex)





if __name__ == '__main__':
    main(sys.argv[1:])

