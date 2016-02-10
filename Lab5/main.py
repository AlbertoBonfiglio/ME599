#!/usr/bin/python3

import matplotlib.pyplot as plt
from Lab4.classes.utils import *
from Lab5.classes.complex import Complex

def main(argv):
    try:
        a = Complex()
        b = Complex(2)
        c = Complex(1.0, 2.3)
        d = Complex(-2.0, 2.3)
        e = Complex(3.2, -2.3)

        f = b + d
        f1 = b + 1
        f2 = 1 + b
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(b, d, f)
        print(b, 1, f1)
        print(1, b, f2)

        print(d, e, d * e  )

        x = complex(2, 2.3)
        y = complex(3, -2.3)

        print(x, y, x*y)
    except Exception as ex:
        print(ex)





if __name__ == '__main__':
    main(sys.argv[1:])

