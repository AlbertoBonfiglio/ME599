#!/usr/bin/python3

import sys
#from Lab6.classes.utils import *
from Lab6.classes.grabber2 import Webcamera
import Lab6.classes.event


def main(argv):
    try:
        _webcam = Webcamera()
        _webcam.OnCapture += printevent
        _webcam.OnCaptureComplete += printcomplete
        _webcam.capture(30, 0.05)

        print(_webcam.history)

    except Exception as ex:
        print('Could not save image to file')
        print(ex)



def printevent(sender, args):
    print('captured')

def printcomplete(sender, args):
    print('Captured finished')

if __name__ == '__main__':
    main(sys.argv[1:])

