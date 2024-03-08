import unittest

from goph420_lab01.integration import (integrate_newton)
class TestGauss(unittest.TestCase):
    def setUp(self):
        self.x_trap= [0,1,2]
        self.f_trap= [2,1,0]
        self.x_simp_even = [0,1,2,3,4,5]
        self.x_simp_even = [0,3,12,27,48,75]
        self.x_simp_odd = [0,1,2,3,4]
        self.x_simp_odd = [0,3,12,27,48]
    def test_value_trap(self):
        expected = 2
        self.assertEqual(integrate_newton(self.x_trap,self.f_trap,'trap'),expected)
    def test_value_simp_even(self):
        expected = 125
        self.assertEqual(integrate_newton(self.x_simp_even,self.f_simp_even,'simp'),expected)
    def test_value_simp_odd(self):
        expected = 64
        self.assertAlmostEqual(integrate_newton(self.x_simp_odd,self.f_simp_odd,'simp'),expected,delta=1e-15)
    def test_type(self):
        self.assertIsInstance(integrate_newton(self.x_trap,self.f_trap,'trap'),float)
