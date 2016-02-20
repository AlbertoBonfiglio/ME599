#!/usr/bin/python3

from urllib.request import urlopen # fix for Python3
from PIL import Image, ImageDraw
from Lab6.classes.grabber import Webcam
import time
import io
import uuid
import Lab6.classes.event as event


# Interface to the Oregon State University webcams.  This should work
# with any web-enabled AXIS camera system.
class Webcamera(Webcam):

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

                _image_data = WebImage(_filename, False, 0, (255, 255, 255), time.time(), delay)
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


    def daytime(self):
        retval = False
        try:
            raise NotImplementedError
            return retval

        except Exception as ex:
            print(ex)


    def image_intensity(self, image):
        retval = 0
        try:
            raise NotImplementedError
            return retval

        except Exception as ex:
            print(ex)


    def image_average_intensity(self, image):
        retval = 0
        try:
            raise NotImplementedError
            return retval

        except Exception as ex:
            print(ex)


    def image_most_common_colour(self):
        retval = 0
        try:
            raise NotImplementedError
            return retval

        except Exception as ex:
            print(ex)


    def detect_motion(self, interval=10):
        retval = 0
        try:
            raise NotImplementedError
            return retval

        except Exception as ex:
            print(ex)


    def detect_event(self):
        retval = 0
        try:
            raise NotImplementedError
            return retval

        except Exception as ex:
            print(ex)


class WebImage(object):
    def __init__(self, id, daytime, intensity, mcc, ctime, interval):
        self.id = id
        self.daytime = daytime
        self.intensity = intensity
        self.mcc = mcc
        self.time = ctime
        self.interval = interval




