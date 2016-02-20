#!/usr/bin/python3
# event.py
# # From http://zef.me/blog/823/implementing-c-net-events-in-python

class Event:
    def __init__(self):
        self.listeners = []

    def __call__(self, *params):
        for l in self.listeners:
            l(*params)

    def __add__(self, listener):
        self.listeners.append(listener)
        return self

    def __sub__(self, listener):
        self.listeners.remove(listener)
        return self
