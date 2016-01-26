#!/usr/bin/python3

class Fermat(object):
    CORRECT = 'No, that doesn’t work.'
    INCORRECT = 'Holy smokes, Fermat was wrong!'


    def getInput(self, var=''):
        while True:
            try:
                retval = int(input('Please enter an integer for variable {0} \n'.format(var)))
                return retval
            except ValueError as ex:
                print(ex)


    def check_fermat(self, a,b,c,n):
        value = (a**n) + (b**n)

        allPositive = (a > 0 and b > 0 and c > 0)

        fermatInvalid = (value == (c**n) and n > 2 and allPositive)

        if fermatInvalid:
            print('{0} = {1} for n = {2}'.format(value, c**n, n))
            return self.INCORRECT

        return self.CORRECT