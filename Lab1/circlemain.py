#!/usr/bin/python3

import numpy as np
from classes.circle import Circle

def main():
    _circle = Circle()
    _radii = np.arange(0, 10.5, 0.5)

    for r in _radii:
       print('{0} --> {1}'.format(r, _circle.circle_area(r)))

if __name__ == "__main__":
    main()