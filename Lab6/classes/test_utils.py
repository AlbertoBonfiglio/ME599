from unittest import TestCase
from Lab6.classes.utils import *


class Test_utils(TestCase):
    def test_euclidean_distance(self):
        a = (2, -1)
        b = (-2, 2)

        self.assertEqual(euclidean_distance(a,b), 5)

