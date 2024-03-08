import unittest

from goph420_lab01.integration import (integrate_gauss)
def function(x):
    return (2-x)
class TestGauss(unittest.TestCase):
    def setUp(self):
        self.lims = [0,2]
    def test_value_ntps1(self):
        expected = 2
        self.assertAlmostEqual(integrate_gauss(function(),self.lims,1),expected,delta=1e-15)
    def test_type(self):
        self.assertIsInstance(integrate_gauss(function(),self.lims,1), float)
