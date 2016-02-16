#!/usr/bin/python3

from numbers import Number

class Complex(object):

    def __init__(self, real=0, imaginary=0):
        if not isinstance(real, (Number)):
            raise ValueError('{0} is not a valid real number'.format(real))

        if not isinstance(imaginary, (Number)):
            raise ValueError('{0} is not a valid imaginary number'.format(imaginary))

        self.real = int(real)
        self.imaginary = imaginary


    def __str__(self):
        rSign = ''
        iSign = '+'
        if self.real < 0: rSign = '-'
        if self.imaginary < 0: iSign = '-'

        retval = '({0}{1}{2}{3}i)'.format(rSign, abs(self.real), iSign, abs(self.imaginary))
        return retval


    def __add__(self, other):
        _real = self.real
        _imaginary = self.imaginary
        if isinstance(other, Complex):
            _real += other.real
            _imaginary += other.imaginary

        elif isinstance(other, Number):
            _real += int(other)

        else:
            raise ValueError('{0} is not a valid value'.format(other))

        return Complex(_real, _imaginary)


    def __radd__(self, other):
        return Complex.__add__(self, other)


    def __sub__(self, other):
        _real = self.real
        _imaginary = self.imaginary
        if isinstance(other, Complex):
            _real -= other.real
            _imaginary -= other.imaginary

        elif isinstance(other, Number):
            _real -= int(other)

        else:
            raise ValueError('{0} is not a valid value'.format(other))

        return Complex(_real, _imaginary)


    def __rsub__(self, other):
        return Complex.__sub__(self, other)


    def __neg__(self):
        return Complex(-self.real, -self.imaginary)


    def __mul__(self, other):
        _real = self.real
        _imaginary = self.imaginary
        if isinstance(other, Complex):
            _real = _real * other.real
            _imaginary = _imaginary * other.imaginary

        elif isinstance(other, Number):
            _real = _real * int(other)

        else:
            raise ValueError('{0} is not a valid value'.format(other))

        return Complex(self.real*other.real - self.imaginary*other.imaginary,
                       self.imaginary*other.real + self.real*other.imaginary)


    def __invert__(self):
        return Complex(self.real, -self.imaginary)


    def __truediv__(self, other):
        raise NotImplemented
