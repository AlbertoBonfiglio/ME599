#!/usr/bin/python3

import sys
from Lab6.classes.utils import *
from Lab6.classes.grabber2 import Webcamera
import Lab6.classes.event
from PIL import Image

def main(argv):
    try:
        _webcam = Webcamera()

        int1 = _webcam.image_average_intensity(Image.open('peeps_day.jpg'))
        int2 = _webcam.image_average_intensity(Image.open('night.jpg'))

      #  _webcam.detect_event()
        _webcam.detect_motion()

        _webcam.OnCapture += printevent
        _webcam.OnCaptureComplete += printcomplete
        _webcam.capture(20, 0.005, True)
        _webcam.plot_history_intensity()

        print(_webcam.history)

    except Exception as ex:
        print('Could not save image to file')
        print(ex)



def printevent(sender, args):
    print('captured at {0}'.format(args[0]))

def printcomplete(sender, args):
    print('Captured finished')

if __name__ == '__main__':
    main(sys.argv[1:])

