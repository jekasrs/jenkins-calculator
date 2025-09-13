import unittest

import math
from math import calculate

class TestCalculator(unittest.TestCase):
    # def setUp(self):
    #     print("Before each test")
    
    # def tearDown(self):
    #     print("After each test")
    
    def test_additions(self):
        self.assertEqual(calculate(1,2,'+'), 3)
        self.assertEqual(calculate(-5,2,'+'), -3)
        self.assertEqual(calculate(0,0,'+'), 0)
        self.assertEqual(calculate(5,-5,'+'), 0)
    
    def test_substractions(self):
        self.assertEqual(calculate(5,2,'-'), 3)
        self.assertEqual(calculate(0,0,'-'), 0)
        self.assertEqual(calculate(-1,1,'-'), -2)
        self.assertEqual(calculate(1,-1,'-'), 2)
        
    def test_multiplies(self):
        self.assertEqual(calculate(3,7,'*'), 21)
        self.assertEqual(calculate(0,0,'*'), 0)
        self.assertEqual(calculate(-1,2,'*'), -2)
        self.assertEqual(calculate(1,-2,'*'), -2)
        self.assertEqual(calculate(-10,-10,'*'), 100)
        
    def test_divizions(self):
        self.assertEqual(calculate(10,2,'/'),5)
        self.assertEqual(calculate(0,2,'/'),0)
        self.assertEqual(calculate(-100,2,'/'),-50)
        self.assertEqual(calculate(-100,-2,'/'),50)

        with self.assertRaises(Exception):
            calculate(5,0,'/')
