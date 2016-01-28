#!/usr/bin/python3

from classes.smd import SpringMassDamper
import matplotlib.pyplot as plt
from  matplotlib.pylab import figtext
import numpy as np


def main():
    mass = np.random.randint(1, 10)
    spring = np.random.randint(1, 10)
    damp = np.random.random()
    t = 200.0
    dt = 0.001
    x, x_dot = 10.0, 0.0

    try:
        gerry = SpringMassDamper(mass, spring, damp, t, dt)
        states, times = gerry.simulate(x, x_dot)

        print (plt.style.available)
        plt.style.use(['dark_background']) #, 'fivethirtyeight'])
        fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True, sharey=True)
        fig.suptitle('Spring damping over time',  fontsize=16, fontweight='bold')

        displacement = [n[0] for n in states]
        ax.plot(times, displacement)

        ax.set_xlabel('Time (s)')
        ax.set_ylabel('Displacement (m)')
        ax.axis('tight')
        figtext(.52, .15, 'M={0:.1f}, K={1:.1f}, C={2:.2f} \n t={3}, dt={4}\n x={5}, xdot={6}'.format(mass, spring, damp, t, dt, x, x_dot))
        plt.show()

    except Exception as ex:
        print(ex)





if __name__ == '__main__':
    main()