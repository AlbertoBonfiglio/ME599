#!/usr/bin/python3

import tkinter
import Lab6.classes.event as event


class HsvGui(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.pack()
        self.createwidgets()


    def createWidgets(self):

        top = tkinter.Tk()
# Code to add widgets will go here...
top.mainloop()
