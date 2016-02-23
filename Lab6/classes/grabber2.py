#!/usr/bin/python3

import io
import matplotlib.pyplot as plt
import numpy
import uuid
import cv2


from collections import Counter
from datetime import datetime
from PIL import Image, ImageDraw, ImageFilter, ImageChops, ImageOps, ImageMath
from urllib.request import urlopen # fix for Python3
from time import time, mktime, sleep, localtime

import Lab6.classes.event as event
from Lab6.classes.grabber import Webcam
from Lab6.classes.utils import get_closest_colour
from Lab6.classes.filter import FilterHelper

# Interface to the Oregon State University webcams.  This should work
# with any web-enabled AXIS camera system.
class Webcamera(Webcam):

    #TODO calculate the right threshold
    __daylightThreshold = 100

    def __init__(self):
        super(Webcamera, self).__init__()
        self.history = []

        self.filter = FilterHelper()
        self.OnCapture = event.Event()
        self.OnCaptureComplete = event.Event()


    def capture(self, duration=10, delay=0.01, persist=False):
        try:
            self.history = []

            _start = time()
            _running = True
            while _running:
                args = []
                _filename = str(uuid.uuid4()) + '.jpg'
                _image = self.save_image(_filename, persist)
                _intensity = self.image_average_intensity(_image)
                _daylight = self.daytime(_intensity)
                _mcc = self.image_most_common_colour(_image)
                _size = (_image.height * _image.width)

                _image_data = WebImage(_filename, _intensity, _daylight,  _mcc, _size, localtime(), delay)
                self.history.append(_image_data)

                _elapsed = (time() - _start)

                args.append(_elapsed)
                args.append(localtime())
                self.OnCapture(self, args)

                if _elapsed >= duration: _running = False

                #TODO add save and read back capability

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
            name = get_closest_colour(rgb)

            #TODO ZFind better way to do colours
            return (rgb, frequency, name, (frequency/len(pixels)))

        except Exception as ex:
            print(ex)


    def daytime(self, intensity=0):
        return intensity >= self.__daylightThreshold


    def plot_history_intensity(self):
        try:
            caption = 'average intensity over time'
            with plt.xkcd():
                fig, ax = plt.subplots(nrows=2, ncols=1, sharex=False, sharey=False,  tight_layout=True, figsize=(9, 4.5))
                fig.suptitle(caption,  fontsize=18, fontweight='bold')

                x = [datetime.fromtimestamp(mktime(wimage.time)) for wimage in self.history]

                y = [wimage.intensity for wimage in self.history]
                #ax.set_xticklabels(x, fontsize='small')
                ax[0].plot(x, y)

                y1 = self.filter.filterData(y, 5)
                ax[1].plot(x, y1)

                    #ax.set_xlabel('{0} #'.format(scaptions[col]), fontsize='small')
                    #ax.set_ylabel('Time (s)', fontsize='small')
                    #ax.set_xticks(position + (width/t_groups) *2)

                    #ax.legend(bars, tcaptions, fontsize='small', loc='upper left', shadow=True)
                    #ax.axis('tight')

                    #col +=1
            plt.show()
        except Exception as ex:
            print(ex)


    def __preprocess_image(self, image, ratio=0.75):
        #resize to make things faster, convert to grayscale,
        ## and apply some gaussian blur to reduce aliasing
        _image = image.resize((int(image.width*ratio), int(image.height*ratio)))
        #_image = ImageOps.grayscale(image)
        #_image = image.filter(ImageFilter.GaussianBlur)
        _image = cv2.cvtColor(numpy.array(_image), cv2.COLOR_RGB2BGR)
        _image = cv2.cvtColor(_image, cv2.COLOR_BGR2GRAY)
        _image = cv2.GaussianBlur(_image, (15, 15), 0)

        return _image



    #TODO finetune mincontour, remove imgshow, test in daylight
    # Gets two images and calculates the difference in pixels
    def detect_motion(self, interval=1):
        min_contour_area = 50
        retval = False
        threshold = 25
        try:
            #apply some gaussian blur to reduce aliasing (see wikipedia)
            _image_static = Image.open('nopeeps.jpg')
            _image_static = self.__preprocess_image(_image_static)
            cv2.imshow('Static', _image_static)

            sleep(interval) #defaults to one second
            _image_dynamic1 = Image.open('peeps.jpg') #self.save_image(persist=True)
            _image_dynamic1 = self.__preprocess_image(_image_dynamic1)
            cv2.imshow('Frame', _image_dynamic1)

            # ideas from http://docs.opencv.org/master/d4/d73/tutorial_py_contours_begin.html#gsc.tab=0
            _delta = cv2.absdiff(_image_dynamic1, _image_static)
            cv2.imshow('Delta', _delta)

            _threshold = cv2.threshold(_delta, 25, 255, cv2.THRESH_BINARY)[1]
            cv2.imshow('Tresh', _threshold)

            #TODO Evaluate if better
            th3 = cv2.adaptiveThreshold(_delta,25,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
            cv2.imshow('Tresh', th3)

            # dilate the thresholded image to fill in holes, then find contours
            # on thresholded image
            _threshold = cv2.dilate(_threshold, None, iterations=2)
            cv2.imshow('Tresh', _threshold)
            (img, contours, _) = cv2.findContours(_threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # loop over the contours
            text = 'None'
            for contour in contours:
                # if the contour is too small, ignore it
                if cv2.contourArea(contour) > min_contour_area:
                    continue # skip to the next



                # compute the bounding box for the contour, draw it on the frame,
                # and update the text
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(_image_dynamic1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = "Detected"


                # draw the text and timestamp on the frame
                cv2.putText(_image_dynamic1, "Motion: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                cv2.putText(_image_dynamic1, datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, _image_dynamic1.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

            cv2.imshow('Result', _image_dynamic1)
            cv2.imwrite('result.png', _image_dynamic1)

            return retval

        except Exception as ex:
            print(ex)



    #TODO detect Event
    def detect_event(self):
        retval = 0

        try:
             #resize to make things faster, convert to grayscale,
            ## and apply some gaussian blur to reduce aliasing (see wikipedia)
            _image_dynamic = self.save_image(persist=False).crop((190, 330, 545, 510))
            _image_dynamic = self.__preprocess_image(_image_dynamic)

            if self.daytime(self.image_average_intensity(_image_dynamic)) == True:
                _image_static = Image.open('day.png')
            else:
                _image_static = Image.open('night.png')

            _image_dynamic.save('dy.png')

            _pixel_static = numpy.array(_image_static.getdata())
            _pixel_dynamic = numpy.array(_image_dynamic.getdata())

            counter = 0
            for  p in range(len(_pixel_static)):
                if numpy.mean(_pixel_static[p]) != numpy.mean(_pixel_dynamic[p]):
                    counter += 1

            percentdiff = counter / len(_pixel_static)


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



