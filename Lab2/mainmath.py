#!/usr/bin/python3

from classes.sillymath import SillyMath
import classes.utils as utils


def main():
    silly = SillyMath()

    while True:
        isel = utils.getIntInput('Press 0 for GCD or 1 for Pi \n', 'choice')
        if (isel <0 or isel > 1):
            print('Seriously?? You chose {0}???'.format(isel))
        else:
            break

    if isel == 0:
        a = utils.getIntInput('Please enter an integer for variable {0} \n', 'a')
        b = utils.getIntInput('Please enter an integer for variable {0} \n', 'b')
        c = silly.gdc(a, b)
        print('Methinks the GDC of {0} and {1} is {2}'.format(a,b,c))

    else:
        print('My best guess is {0}'.format(silly.estimate_pi()))
        print('Is it equal to pi? {0}'.format(silly.compare_pi(silly.estimate_pi())))


if __name__ == "__main__":
    main()
