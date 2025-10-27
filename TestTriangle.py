# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateral_large(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral', '10,10,10 should be Equilateral')

    def testIsoscelesA(self):
        self.assertEqual(classifyTriangle(5, 5, 3), 'Isosceles', '5,5,3 should be Isosceles')

    def testIsoscelesB(self):
        self.assertEqual(classifyTriangle(5, 3, 5), 'Isosceles', '5,3,5 should be Isosceles')

    def testIsosceles_large(self):
        self.assertEqual(classifyTriangle(10, 10, 15), 'Isosceles', '10,10,15 should be Isosceles')

    def testScalene(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4,5,6 should be Scalene')

    def testScalene_large(self):
        self.assertEqual(classifyTriangle(10, 11, 12), 'Scalene', '10,11,12 should be Scalene')

    def testInvalid_zeroSide(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', '0,1,1 should be invalid')

    def testInvalid_negativeSide(self):
        self.assertEqual(classifyTriangle(-1, 2, 2), 'InvalidInput', '-1,2,2 should be invalid')

    def testInvalid_triangleInequality(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is not a triangle')
        self.assertEqual(classifyTriangle(2, 2, 5), 'NotATriangle', '2,2,5 is not a triangle')
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle', '1,10,12 is not a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

