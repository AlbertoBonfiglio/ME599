#!/usr/bin/python3

import sys
from classes.utils import *
from classes.grabber2 import Webcamera
import classes.event
import Lab6.hsv_gui as hg
from PIL import Image
import cv2
import time
import tkinter as tk


def capture_and_show():
    try:
        _webcam = Webcamera()
        _webcam.OnCapture += printevent
        _webcam.OnCaptureComplete += printcomplete
        _webcam.capture(40, 0.005, False)
        _webcam.plot_history_intensity()

        print(_webcam.history)

    except Exception as ex:
        print('Could not save image to file')
        print(ex)

def detect_motion():
    try:
        _webcam = Webcamera()

        winName = "Movement Indicator"
        cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
        while True:
            time.sleep(1)
            try:
                moveit, img = _webcam.detect_motion()
                cv2.imshow(winName, img)
                print('Movement detected {0}'.format(moveit))
            except:
                print('Error')

            key = cv2.waitKey(10)
            if key == 27:
                cv2.destroyWindow(winName)
                break
    except Exception as ex:
        print(ex)


def  detect_events():
    try:
        _webcam = Webcamera()

        print(_webcam.image_most_common_colour(Image.open('nopeeps_day.jpg'))    )
        winName = "Event Indicator"
        cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
        while True:
            time.sleep(1)
            try:
                moveit, num, img = _webcam.detect_event()
                cv2.imshow(winName, img)
                print('Event detected {0}, Events: {1}'.format(moveit, num))
            except:
                print('Error')

            key = cv2.waitKey(10)
            if key == 27:
                cv2.destroyWindow(winName)
                break
    except Exception as ex:
        print(ex)


def funkyfy():

    root = tk.Tk()
    app = hg.HsvGui(master=root)
    app.mainloop()

    try:
        _webcam = Webcamera()
        winName = "Event Indicator"
        cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
        while True:
            time.sleep(1)
            try:
                img = _webcam.funkyfy()
                cv2.imshow(winName, img)
            except:
                print('Error')

            key = cv2.waitKey(10)
            if key == 27:
                cv2.destroyWindow(winName)
                break
    except Exception as ex:
        print(ex)



def printevent(sender, args):
    print('captured at {0}'.format(args[0]))
    img = args[2]
    print('Is daytime {0}, average intensity: {1}, common colour: {2}'.format(img.daytime, img.intensity, img.most_common))

def printcomplete(sender, args):
    print('Captured finished')

if __name__ == '__main__':

    funkyfy()

    #capture_and_show()

    #detect_motion()

    #detect_events()
