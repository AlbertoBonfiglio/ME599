#!/usr/bin/python3

from numbers import Number

class Complex(object):

    def __init__(self, real=0, imaginary=0):
        if not isinstance(real, (Number)):
            raise ValueError('{0} is not a valid real number'.format(real))

        if not isinstance(imaginary, (Number)):
            raise ValueError('{0} is not a valid imaginary number'.format(imaginary))

        self.real = real
        self.imaginary = imaginary


    def __str__(self):
        rSign = ''
        iSign = '+'
        if self.real < 0: rSign = '-'
        if self.imaginary < 0: iSign = '-'

        retval = '({0}{1}{2}{3}i)'.format(rSign, abs(self.real), iSign, abs(self.imaginary))
        #retval = '({0}{1}{2}{3}i)'.format(rSign, self.real, iSign, abself.imaginary)

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
            other = Complex(other, 0)
            _real = _real * other.real
            _imaginary = _imaginary * other.imaginary

        else:
            raise ValueError('{0} is not a valid value'.format(other))

        return Complex(self.real*other.real - self.imaginary*other.imaginary,
                       self.imaginary*other.real + self.real*other.imaginary)


    def __rmul__(self, other):
        return self.__mul__(other)


    def __invert__(self):
        return Complex(self.real, -self.imaginary)


    def __truediv__(self, other):
        if isinstance(other, Number):
            other = Complex(other, 0)

        conj = ~other

        f,o,i,l = self.foil(self, conj)
        f1, o1, i1, l1 = self.foil(other, conj)

        numr = f + l
        numi = o + i

        denr = f1 + l1
        deni = o1 + i1

        return Complex(numr/denr, numi/denr)


    def __rtruediv__(self, other):
        if isinstance(other, Number):
            other = Complex(other, 0)

        conj = ~self

        f,o,i,l = self.foil(other, conj)
        f1, o1, i1, l1 = self.foil(self, conj)

        numr = f + l
        numi = o + i

        denr = f1 + l1
        deni = o1 + i1

        return Complex(numr/denr, numi/denr)


    def foil(self, c1, c2):
        f = c1.real * c2.real
        o = c1.real * c2.imaginary
        i = c1.imaginary * c2.real
        l = -(c1.imaginary * c2.imaginary)

        return f,o,i,l


