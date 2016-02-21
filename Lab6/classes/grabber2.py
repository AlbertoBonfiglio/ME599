#!/usr/bin/python3


import io
import matplotlib.pyplot as plt
import numpy
import uuid

from collections import Counter
from datetime import datetime
from PIL import Image, ImageDraw
from urllib.request import urlopen # fix for Python3
from time import time, mktime, sleep, localtime

import Lab6.classes.event as event
from Lab6.classes.grabber import Webcam
from Lab6.classes.utils import find_colour_name

# Interface to the Oregon State University webcams.  This should work
# with any web-enabled AXIS camera system.
class Webcamera(Webcam):

    #TODO calculate the right threshold
    __daylightThreshold = 100

    def __init__(self):
        super(Webcamera, self).__init__()
        self.history = []

        self.OnCapture = event.Event()
        self.OnCaptureComplete = event.Event()


    def capture(self, duration=10, delay=0.01):
        try:
            self.history = []

            _start = time()
            _running = True
            while _running:
                _filename = str(uuid.uuid4()) + '.jpg'
                _image = self.save_image(_filename, False)
                _intensity = self.image_average_intensity(_image)
                _daylight = self.daytime(_intensity)
                _mcc = self.image_most_common_colour(_image)
                _size = (_image.height * _image.width)

                _image_data = WebImage(_filename, _intensity, _daylight,  _mcc, _size, localtime(), delay)
                self.history.append(_image_data)

                self.OnCapture(self, localtime())

                _elapsed = (time() - _start) % 60.0
                if _elapsed >= duration: _running = False

                sleep(delay)

            self.OnCaptureComplete(self, None)
        except Exception as ex:
            print(ex)


    def save_image(self, filename=None, persist=True):
        try:
            if filename == None: filename = str(uuid.uuid4()) + '.jpg'

            _image = urlopen('{0}/axis-cgi/jpg/image.cgi'.format(self.url)).read()
            # convert directly to an Image instead of saving / reopening
            # thanks to SO: http://stackoverflow.com/a/12020860/377366
            _image_as_file = io.BytesIO(_image)
            _image_as_pil = Image.open(_image_as_file)
            if persist: _image_as_pil.save(filename)

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
            pixels = image.getdata()
            colours = Counter(pixels).most_common(1) #Handy Python function for counting occurences.

            rgb = colours[0][0]
            frequency = colours[0][1]
            name = find_colour_name(rgb)

            return (rgb, frequency, name, (frequency/len(pixels)))

        except Exception as ex:
            print(ex)


    def daytime(self, intensity=0):
        return intensity >= self.__daylightThreshold


    def plot_history_intensity(self):
        try:
            caption = 'average intensity over time'
            with plt.xkcd():
                fig, ax = plt.subplots(nrows=1, ncols=1, sharex=False, sharey=False,  tight_layout=True, figsize=(9, 4.5))
                fig.suptitle(caption,  fontsize=18, fontweight='bold')

                x = [datetime.fromtimestamp(mktime(wimage.time)) for wimage in self.history]

                y = [wimage.intensity for wimage in self.history]
                #ax.set_xticklabels(x, fontsize='small')
                ax.plot(x, y)

                    #ax.set_xlabel('{0} #'.format(scaptions[col]), fontsize='small')
                    #ax.set_ylabel('Time (s)', fontsize='small')
                    #ax.set_xticks(position + (width/t_groups) *2)

                    #ax.legend(bars, tcaptions, fontsize='small', loc='upper left', shadow=True)
                    #ax.axis('tight')

                    #col +=1
            plt.show()
        except Exception as ex:
            print(ex)



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
    def __init__(self, id, intensity, daytime, most_common, size, ctime, interval):
        self.id = id
        self.intensity = intensity
        self.daytime = daytime

        self.most_common = most_common
        self.size = size
        self.time = ctime
        self.interval = interval


    def most_common_rgb(self):
        return self.most_common[0]

    def most_common_frequency(self):
        return self.most_common[1]

    def most_common_name(self):
        return self.most_common[3]

    def most_common_percent(self):
        return self.most_common[4]



