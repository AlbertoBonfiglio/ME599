#!/usr/bin/python3

from classes.utils import *
from classes.complex import Complex
from classes.circle import Circle
from random import randint
def main(argv):
    try:
        radius = randint(1,100)
        cir = Circle(radius)
        print('Circle Radius {0}, Diameter = {1}, Area = {2}, Circumference = {3}'.format(cir.radius, cir.diameter(), cir.area(), cir.circumference()))


        a = Complex()
        b = Complex(2)
        c = Complex(1.0, 2.3)
        d = Complex(-2.0, 2.3)
        e = Complex(3.2, -2.3)

        print('sum --> {0}, {1} = {2}'.format(c, d, c + d))
        print('sum --> {0}, {1} = {2}'.format(c, 3, c + 3))
        print('sum --> {0}, {1} = {2}'.format(3, c, 3 + c))

        print('sub --> {0}, {1} = {2}'.format(c, d, c - d))
        print('sub --> {0}, {1} = {2}'.format(c, 3, c - 3))
        print('sub --> {0}, {1} = {2}'.format(3, c, 3 - c))

        print('mult --> {0}, {1} = {2}'.format(c, d, c * d))
        print('mult --> {0}, {1} = {2}'.format(c, 3, c * 3))
        print('mult --> {0}, {1} = {2}'.format(3, c, 3 * c))


        print('div --> {0}, {1} = {2}'.format(c, d, c / d))
        print('div --> {0}, {1} = {2}'.format(c, 3, c / 3))
        print('div --> {0}, {1} = {2}'.format(3, c, 3 / c))
        print('div --> {0}, {1} = {2}'.format(3, complex(1.0, 2.3), 3 / complex(1.0, 2.3)))

        print('conjugate --> {0}'.format(c))

        print('Root '.format())


    except Exception as ex:
        print(ex)





if __name__ == '__main__':
    main(sys.argv[1:])

