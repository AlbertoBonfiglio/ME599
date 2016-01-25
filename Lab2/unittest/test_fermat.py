from unittest import TestCase
from Lab2.classes.fermat import Fermat
from random import randint

class TestFermat(TestCase):
    def test_demo(self):
        self.fail()

    def test_getInput(self):
        f = Fermat()

        self.assertIsInstance(f.getInput(), int)


    def test_CheckFermatMoreThan2(self):
        f = Fermat()

        self.assertEqual(f.check_fermat(randint(), randint(), randint(), 3), f.CORRECT)

    def test_CheckFermatLessThan3(self):
        f = Fermat()

        self.assertEqual(f.check_fermat(randint(), randint(), randint(), 2), f.CORRECT)