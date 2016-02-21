#!/usr/bin/python3

import time
import io
import uuid
import Lab6.classes.event as event
import numpy

from urllib.request import urlopen # fix for Python3
from PIL import Image, ImageDraw
from Lab6.classes.grabber import Webcam
from collections import Counter


# Interface to the Oregon State University webcams.  This should work
# with any web-enabled AXIS camera system.
class Webcamera(Webcam):

    #TODO calculate the right threshold
    __daylightThreshold = 45

    def __init__(self):
        super(Webcamera, self).__init__()
        self.history = []

        self.OnCapture = event.Event()
        self.OnCaptureComplete = event.Event()


    def capture(self, duration=10, delay=0.01):
        try:
            self.history = []

            _start = time.time()
            _running = True
            while _running:
                _filename = str(uuid.uuid4()) + '.jpg'
                _image = self.save_image(_filename)
                _intensity = self.image_average_intensity(_image)
                _daylight = self.daytime(_intensity)
                _mcc = self.image_most_common_colour(_image)

                _image_data = WebImage(_filename, _intensity, _daylight,  (255, 255, 255), time.time(), delay)
                self.history.append(_image_data)

                self.OnCapture(self, None)

                _elapsed = (time.time() - _start) % 60.0
                if _elapsed >= duration: _running = False

                time.sleep(delay)

            self.OnCaptureComplete(self, None)
        except Exception as ex:
            print(ex)


    def save_image(self, filename=None):
        try:
            if filename == None: filename = str(uuid.uuid4()) + '.jpg'

            _image = urlopen('{0}/axis-cgi/jpg/image.cgi'.format(self.url)).read()
            # convert directly to an Image instead of saving / reopening
            # thanks to SO: http://stackoverflow.com/a/12020860/377366
            _image_as_file = io.BytesIO(_image)
            _image_as_pil = Image.open(_image_as_file)
            _image_as_pil.save(filename)

            return _image_as_pil

        except Exception as ex:
            print(ex)


    def image_average_intensity(self, image):
        try:
            pixels = numpy.array(image.getdata())
            return numpy.mean(pixels)

        except Exception as ex:
            print(ex)


    def image_most_common_colour(self, image):
        try:
            #pixels,count = numpy.unique(image.getdata(), return_counts=True)
            pixels = image.getdata()
            colours = Counter(pixels).most_common(1)
            return colours

        except Exception as ex:
            print(ex)


    def daytime(self, intensity=0):
        return intensity <= self.__daylightThreshold



    #TODO detect motion
    def detect_motion(self, interval=10):
        retval = 0
        try:
            raise NotImplementedError
            return retval

        except Exception as ex:
            print(ex)

    #TODO detect Event
    def detect_event(self):
        retval = 0
        try:
            raise NotImplementedError
            return retval

        except Exception as ex:
            print(ex)


class WebImage(object):
    def __init__(self, id, intensity, daytime, mcc, ctime, interval):
        self.id = id
        self.intensity = intensity
        self.daytime = daytime

        self.mcc = mcc
        self.time = ctime
        self.interval = interval




