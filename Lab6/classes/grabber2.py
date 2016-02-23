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
    __daylightThreshold = 75

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
                args.append(_image_data)

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
            if persist:
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


    def __preprocess_image(self, image, ratio=0.75, blur=21):
        #resize to make things a bit faster, convert to grayscale,
        # and apply some gaussian blur to reduce aliasing and pixel differences
        _image = image.resize((int(image.width*ratio), int(image.height*ratio)))
        _image = cv2.cvtColor(numpy.array(_image), cv2.COLOR_RGB2GRAY)
        _image = cv2.GaussianBlur(_image, (blur, blur), 0)

        return _image



    #TODO finetune mincontour,
    # Gets two images and calculates the difference in pixels
    def detect_motion(self, interval=1.5):
        min_contour_area = 40
        max_contour_area = 250
        retval = False
        threshold = 65
        try:
            #TODO write code to change static image if night
            _image_static = self.save_image(persist=False)
            _image_static = self.__preprocess_image(_image_static, .75, 7)

            sleep(interval) #defaults to one second

            _image_dynamic1 = self.save_image(persist=False)
            _image_dynamic1 = self.__preprocess_image(_image_dynamic1, .75, 7)


            # ideas from http://docs.opencv.org/master/d4/d73/tutorial_py_contours_begin.html#gsc.tab=0
            #_delta1 = cv2.absdiff(_image_dynamic2, _image_dynamic1)
            _delta = cv2.absdiff(_image_dynamic1, _image_static)
            #_delta = cv2.bitwise_and(_delta1, _delta2)

            _threshold = cv2.threshold(_delta, 25, 255, cv2.THRESH_BINARY)[1]


            # dilate the thresholded image to fill in holes, then find contour on thresholded image
            #_threshold = cv2.dilate(_threshold, None, iterations=2)

            (img, contours, _) = cv2.findContours(_threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # loop over the contours
            text = 'None'
            for contour in contours:
                # if the contour is too small, ignore it
                _area = cv2.contourArea(contour)
                if _area < min_contour_area or _area > max_contour_area:
                    continue # skip to the next

                # compute the bounding box for the contour, draw it on the frame,
                retval = True
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(_image_dynamic1, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = "Detected"

                # draw the text and timestamp on the frame
                #cv2.putText(_image_dynamic1, "Motion: {}".format(text), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                #cv2.putText(_image_dynamic1, datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"), (10, _image_dynamic1.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
            return retval, _image_dynamic1

        except Exception as ex:
            print(ex)



    #TODO detect Event
    def detect_event(self):
        crop_coord = (180, 320, 555, 490)
        min_contour_area = 1000
        max_contour_area = 3000
        event_count = 0
        threshold = 65

        try:
            #convert to grayscale,
            # and apply some gaussian blur to reduce aliasing (see wikipedia)
            _image_dynamic = Image.open('event_day.jpg').crop(crop_coord) #self.save_image(persist=False).crop(crop_coord)
            _image_dynamic = self.__preprocess_image(_image_dynamic, 1)

            _image_static = Image.open('nopeeps_day.jpg').crop(crop_coord)
            _image_static = self.__preprocess_image(_image_static, 1)

            # ideas from http://docs.opencv.org/master/d4/d73/tutorial_py_contours_begin.html#gsc.tab=0
            _delta = cv2.absdiff(_image_dynamic, _image_static)
            #cv2.imshow('delta', _delta)
            _threshold = cv2.threshold(_delta, 25, 255, cv2.THRESH_BINARY)[1]

            #cv2.imshow('thres', _threshold)

            # dilate the thresholded image to fill in holes, then find contour on thresholded image
            _threshold = cv2.dilate(_threshold, None, iterations=2)

            (img, contours, _) = cv2.findContours(_threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # loop over the contours
            text = 'None'
            for contour in contours:
                # if the contour is too small, ignore it
                _area = cv2.contourArea(contour)
                if _area < min_contour_area or _area > max_contour_area:
                    continue # skip to the next

                # compute the bounding box for the contour, draw it on the frame,
                event_count +=1
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(_image_dynamic, (x, y), (x + w, y + h), (0, 255, 0), 2)
                text = "Detected"

                # draw the text and timestamp on the frame
            return (event_count > 0), event_count, _image_dynamic

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



