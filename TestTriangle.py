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

    def testRightTriangle(self):
        self.assertEqual(classifyTriangle(3,4,5), 'Right', '3,4,5 should be Right')

    def testRightTriangle_permutations(self):
        self.assertEqual(classifyTriangle(5,3,4), 'Right', '5,3,4 should be Right')
        self.assertEqual(classifyTriangle(4,5,3), 'Right', '4,5,3 should be Right')

    def testRightTriangle_scaled(self):
        self.assertEqual(classifyTriangle(6,8,10), 'Right', '6,8,10 should be Right')

    def testEquilateral_small(self):
        self.assertEqual(classifyTriangle(1,1,1), 'Equilateral', '1,1,1 should be Equilateral')

    def testEquilateral_large(self):
        self.assertEqual(classifyTriangle(10,10,10), 'Equilateral', '10,10,10 should be Equilateral')

    def testIsosceles_aab(self):
        self.assertEqual(classifyTriangle(5,5,3), 'Isosceles', '5,5,3 should be Isosceles')

    def testIsosceles_aba(self):
        self.assertEqual(classifyTriangle(5,3,5), 'Isosceles', '5,3,5 should be Isosceles')

    def testIsosceles_baa(self):
        self.assertEqual(classifyTriangle(3,5,5), 'Isosceles', '3,5,5 should be Isosceles')

    def testIsosceles_large(self):
        self.assertEqual(classifyTriangle(10,10,15), 'Isosceles', '10,10,15 should be Isosceles')

    def testScalene_basic(self):
        self.assertEqual(classifyTriangle(4,5,6), 'Scalene', '4,5,6 should be Scalene')

    def testScalene_large(self):
        self.assertEqual(classifyTriangle(10,11,12), 'Scalene', '10,11,12 should be Scalene')

    # InvalidInput
    def testInvalid_zeroSide(self):
        self.assertEqual(classifyTriangle(0,1,1), 'InvalidInput', '0,1,1 should be InvalidInput')

    def testInvalid_negativeSide(self):
        self.assertEqual(classifyTriangle(-1,2,2), 'InvalidInput', '-1,2,2 should be InvalidInput')

    def testInvalid_tooLarge(self):
        self.assertEqual(classifyTriangle(300,400,500), 'InvalidInput', '300,400,500 should be InvalidInput')

    def testInvalid_nonInteger(self):
        self.assertEqual(classifyTriangle(3.5,4,5), 'InvalidInput', '3.5,4,5 should be InvalidInput')

    # NotATriangle
    def testNotATriangle_equalSum(self):
        self.assertEqual(classifyTriangle(1,2,3), 'NotATriangle', '1,2,3 is NotATriangle')

    def testNotATriangle_gap(self):
        self.assertEqual(classifyTriangle(2,2,5), 'NotATriangle', '2,2,5 is NotATriangle')

    def testNotATriangle_bigGap(self):
        self.assertEqual(classifyTriangle(1,10,12), 'NotATriangle', '1,10,12 is NotATriangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
