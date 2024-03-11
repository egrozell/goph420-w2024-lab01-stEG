import unittest

from goph420_lab01.integration import (integrate_gauss)
class TestGauss_npts_1(unittest.TestCase):
    def setUp(self):
        self.lims = [0,2]
        self.f = lambda x: x-2
    def test_value_ntps1(self):
        expected = -2
        self.assertAlmostEqual(integrate_gauss(self.f,self.lims,1),expected,delta=1e-15)
    def test_type(self):
        self.assertIsInstance(integrate_gauss(self.f,self.lims,1), float)

class TestGauss_npts_2(unittest.TestCase):
    def setUp(self):
        self.lims = [0,2]
        self.f = lambda x: 3*x**2 
    def test_value_ntps1(self):
        expected = 8
        self.assertAlmostEqual(integrate_gauss(self.f,self.lims,2),expected,delta=1e-15)
    def test_type(self):
        self.assertIsInstance(integrate_gauss(self.f,self.lims,2), float)

class TestGauss_npts_3(unittest.TestCase):
    def setUp(self):
        self.lims = [0,2]
        self.f = lambda x: 4*x**3
    def test_value_ntps1(self):
        expected = 16
        self.assertAlmostEqual(integrate_gauss(self.f,self.lims,3),expected,delta=1e-15)
    def test_type(self):
        self.assertIsInstance(integrate_gauss(self.f,self.lims,3), float)

class TestGauss_npts_4(unittest.TestCase):
    def setUp(self):
        self.lims = [0,2]
        self.f = lambda x: 5*x**4
    def test_value_ntps1(self):
        expected = 32
        self.assertAlmostEqual(integrate_gauss(self.f,self.lims,4),expected,delta=1e-13)
    def test_type(self):
        self.assertIsInstance(integrate_gauss(self.f,self.lims,4), float)

class TestGauss_npts_5(unittest.TestCase):
    def setUp(self):
        self.lims = [0,2]
        self.f = lambda x: 6*x**5
    def test_value_ntps1(self):
        expected = 64
        self.assertAlmostEqual(integrate_gauss(self.f,self.lims,5),expected,delta=1e-13)
    def test_type(self):
        self.assertIsInstance(integrate_gauss(self.f,self.lims,5), float)

class TestGaussInvalidInitializers(unittest.TestCase):
    
    def test_callable_function(self):
        with self.assertRaises(TypeError):
            integrate_gauss(f:=8.0, lims = [1,2])

    def test_lims_dim(self):
        with self.assertRaises(ValueError):
            integrate_gauss(f = lambda x: 2-x, lims = [1])

    def test_lims_type_lims(self):
        with self.assertRaises(ValueError):
            integrate_gauss(f = lambda x: 2-x, lims = ['one','four'])

    def test_npts(self):
        with self.assertRaises(ValueError):
            integrate_gauss(f = lambda x: 2-x, lims = [1,4],npts = 0)
if __name__ == "__main__":
    unittest.main()
