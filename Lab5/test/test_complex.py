from unittest import TestCase
from Lab5.classes.complex import Complex
from random import randint

class TestComplex(TestCase):

    def replace_j(self, object):
        s = str(object)
        #s[len(s)-2] = 'i'
        #return "".join(s)

        return s.replace('j', "i")

#region complete
    def test_create_complex(self):
        _real = randint(-100, 100)
        _imaginary = randint(-100, 100)

        obj = Complex(_real, _imaginary)
        obj2 = complex(_real, _imaginary)

        sComplex = str(obj)
        # need to change j into i
        scomplex = self.replace_j(obj2)

        self.assertEquals(scomplex, sComplex)

    def test_sum_complex(self):
        _real = randint(-100, 100)
        _imaginary = randint(-100, 100)
        _real2 = randint(-100, 100)
        _imaginary2 = randint(-100, 100)

        obj = Complex(_real, _imaginary)
        obj2 = Complex(_real2, _imaginary2)

        vobj = Complex(_real, _imaginary)
        vobj2 = Complex(_real2, _imaginary2)

        obj3 = obj + obj2
        vobj3 = vobj + vobj2

        self.assertEquals(str(obj3), self.replace_j(vobj3))

    def test_sum_to_complex(self):
        _real = randint(-100, 100)
        _imaginary = randint(-100, 100)
        _real2 = randint(-100, 100)

        obj = Complex(_real, _imaginary)
        vobj = Complex(_real, _imaginary)

        obj3 = obj + _real2
        vobj3 = vobj + _real2

        self.assertEquals(str(obj3), self.replace_j(vobj3))

    def test_sub_complex(self):
        _real = randint(-100, 100)
        _imaginary = randint(-100, 100)
        _real2 = randint(-100, 100)
        _imaginary2 = randint(-100, 100)

        obj = Complex(_real, _imaginary)
        obj2 = Complex(_real2, _imaginary2)

        vobj = Complex(_real, _imaginary)
        vobj2 = Complex(_real2, _imaginary2)

        obj3 = obj - obj2
        vobj3 = vobj - vobj2

        self.assertEquals(str(obj3), self.replace_j(vobj3))

    def test_sub_from_complex(self):
        _real = randint(-100, 100)
        _imaginary = randint(-100, 100)
        _real2 = randint(-100, 100)

        obj = Complex(_real, _imaginary)
        vobj = Complex(_real, _imaginary)

        obj3 = obj - _real2
        vobj3 = vobj - _real2

        self.assertEquals(str(obj3), self.replace_j(vobj3))

    def test_rsum_complex(self):
        _real = randint(-100, 100)
        _imaginary = randint(-100, 100)
        _real2 = randint(-100, 100)

        obj = Complex(_real, _imaginary)
        vobj = Complex(_real, _imaginary)

        obj3 = _real2 + obj
        vobj3 = _real2 + vobj

        self.assertEquals(str(obj3), self.replace_j(vobj3))

    def test_rsub_complex(self):
        _real = randint(-100, 100)
        _imaginary = randint(-100, 100)
        _real2 = randint(-100, 100)

        obj = Complex(_real, _imaginary)
        vobj = Complex(_real, _imaginary)

        obj3 = _real2 - obj
        vobj3 = _real2 - vobj

        self.assertEquals(str(obj3), self.replace_j(vobj3))

    def test_conjugate_complex(self):
        _real = randint(-100, 100)
        _imaginary = randint(-100, 100)

        obj = Complex(_real, _imaginary)
        vobj = Complex(_real, -_imaginary)


        self.assertEquals(str(~obj), str(vobj))

    def test_mult_complex(self):
        _real = randint(-100, 100)
        _imaginary = randint(-100, 100)
        _real2 = randint(-100, 100)
        _imaginary2 = randint(-100, 100)

        obj = Complex(_real, _imaginary)
        obj2 = Complex(_real2, _imaginary2)

        tobj = complex(_real, _imaginary)
        tobj2 = complex(_real2, _imaginary2)

        res1 = obj * obj2
        res2 = tobj * tobj2

        self.assertEquals(str(res1), self.replace_j(res2))


    def test_div_complex(self):
        _real = randint(-100, 100)
        _imaginary = randint(-100, 100)
        _real2 = randint(-100, 100)
        _imaginary2 = randint(-100, 100)

        obj = Complex(_real, _imaginary)
        obj2 = Complex(_real2, _imaginary2)

        tobj = complex(_real, _imaginary)
        tobj2 = complex(_real2, _imaginary2)

        res1 = obj / obj2
        res2 = tobj / tobj2

        self.assertEquals(str(res1), self.replace_j(res2))

#endregion








    def test_root_complex(self):
        _real = randint(-100, 100)
        _imaginary = randint(-100, 100)
        _real2 = randint(-100, 100)

        obj = Complex(_real, _imaginary)
        vobj = complex(_real, _imaginary)

