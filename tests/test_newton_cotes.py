import unittest

from goph420_lab01.integration import (integrate_newton)
class test_trap_even(unittest.TestCase):
    def setUp(self):
        self.x_trap= [0,2]
        self.f_trap= [2,0]
    def test_value_trap(self):
        expected = 2
        self.assertEqual(integrate_newton(self.x_trap,self.f_trap,'trap'),expected)
    def test_type(self):
        self.assertIsInstance(integrate_newton(self.x_trap,self.f_trap,'trap'),float)

class test_trap_odd(unittest.TestCase):
    def setUp(self):
        self.x_trap= [0,1,2]
        self.f_trap= [2,1,0]
    def test_value_trap(self):
        expected = 2
        self.assertEqual(integrate_newton(self.x_trap,self.f_trap,'trap'),expected)
    def test_type(self):
        self.assertIsInstance(integrate_newton(self.x_trap,self.f_trap,'trap'),float)

class test_simp_even(unittest.TestCase):
    def setUp(self):
        self.x_simp_even = [0,1,2,3,4,5]
        self.f_simp_even = [0,3,12,27,48,75]
    def test_value_simp_even(self):
        expected = 125
        self.assertEqual(integrate_newton(self.x_simp_even,self.f_simp_even,'simp'),expected)

class test_simp_odd(unittest.TestCase):
    def setUp(self):
        self.x_simp_odd = [0,1,2,3,4]
        self.f_simp_odd = [0,3,12,27,48]

    def test_value_simp_odd(self):
        expected = 64
        self.assertAlmostEqual(integrate_newton(self.x_simp_odd,self.f_simp_odd,'simp'),expected,delta=1e-15)

class TestGaussInvalidInitializers(unittest.TestCase):
    def setUp(self):
        self.x= [0,1,2]
        self.xs= [1,2]
        self.xm= [[1,2],[0,3]]
        self.f= [2,1,0]
    
    def test_string_method(self):
        with self.assertRaises(ValueError):
            integrate_newton(integrate_newton(self.x,self.f,'hi'))

    def test_dims(self):
        with self.assertRaises(ValueError):
            integrate_newton(integrate_newton(self.xm,self.f,'trap'))

    def test_length(self):
        with self.assertRaises(ValueError):
            integrate_newton(integrate_newton(self.xs,self.f,'trap'))
if __name__ == "__main__":
    unittest.main()
