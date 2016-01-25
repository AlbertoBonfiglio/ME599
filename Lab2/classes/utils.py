#!/usr/bin/python3


def getIntInput(msg='', var=''):
    while True:
        try:
            retval = int(input(msg.format(var)))
            return retval
        except ValueError as ex:
            print(ex)