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
    def test_set1_invalid(self):
        self.assertEqual(classifyTriangle(-1, 2, 3),'InvalidInput', '-1, 2, 3 is invalid input')
        self.assertEqual(classifyTriangle(1000, 1000, 1000), 'InvalidInput', '1000, 1000, 1000 is invalid input')
        self.assertEqual(classifyTriangle(-3, -4, -5), 'InvalidInput', '-3, -4, -5 is invalid input')
        self.assertEqual(classifyTriangle(0.3, 0.4, 0.5), 'InvalidInput', '0.3, 0.4, 0.5 is invalid input')

    def test_set2_not_a_triangle(self):
        self.assertEqual(classifyTriangle(2, 2, 4),'NotATriangle', '2, 2, 4 is not a triangle')
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle', '1, 1, 2 is not a triangle')
        self.assertEqual(classifyTriangle(1, 2, 9), 'NotATriangle', '1, 2, 9 is not a triangle')

    def test_set3_equilateral(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1, 1, 1 is an Equilateral')
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral', '200, 200, 200 is an equilateral '
                                                             'triangle')
        self.assertEqual(classifyTriangle(83, 83, 83), 'Equilateral', '83, 83, 83 is an equilateral '
                                                                             'triangle')

    def test_set4_isosceles(self):
        self.assertEqual(classifyTriangle(3, 3, 2), 'Isosceles', '3, 3, 2 is an isosceles triangle')
        self.assertEqual(classifyTriangle(100, 100, 97), 'Isosceles', '100, 100, 97 is an isosceles triangle')
        self.assertEqual(classifyTriangle(77, 77, 53), 'Isosceles', '0.77, 0.77, 0.53 is an isosceles triangle')
        self.assertEqual(classifyTriangle(77, 88, 88), 'Isosceles', '77, 88, 88 is an isosceles triangle')

    def test_set5_right(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3, 4, 5 is a right triangle')
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5, 3, 4 is a right triangle')
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5, 12, 13 is a right triangle')

    def test_set6_scalene(self):
        self.assertEqual(classifyTriangle(3, 4, 6), 'Scalene', '3, 4, 6 is an scalene')
        self.assertEqual(classifyTriangle(5, 8, 7), 'Scalene', '5, 8, 7 is an scalene')
        self.assertEqual(classifyTriangle(9, 10, 12), 'Scalene', '9, 10, 12 is an scalene')

    def test_set7(self):
        self.assertEqual(classifyTriangle(1, 2, 100), 'NotATriangle', '1, 2, 100 should not be a triangle')
        self.assertEqual(classifyTriangle(100, 100, 100), 'Equilateral', '100, 100, 100 should be an equilateral '
                                                                          'triangle')
        self.assertEqual(classifyTriangle(76, 76, 37), 'Isosceles', '76, 76, 37 should be an isosceles triangle')
        self.assertEqual(classifyTriangle(20, 99, 101), 'Right', '20, 99, 101 should be a right triangle')
        self.assertEqual(classifyTriangle(20, 99, 100), 'Scalene', '76, 76, 37 should be a scalene triangle')

    def test_set8_equal(self):
        self.assertEqual(classifyTriangle(1, 2, 100), 'NotATriangle', '1, 2, 100 should not be a triangle')
        self.assertEqual(classifyTriangle(100, 100, 100), 'Equilateral', '100, 100, 100 should be an equilateral '
                                                                          'triangle')
        self.assertEqual(classifyTriangle(76, 76, 37), 'Isosceles', '76, 76, 37 should be an isosceles triangle')
        self.assertEqual(classifyTriangle(20, 99, 101), 'Right', '20, 99, 101 should be a right triangle')
        self.assertEqual(classifyTriangle(20, 99, 100), 'Scalene', '76, 76, 37 should be a scalene triangle')

    def test_set9_notequal(self):
        self.assertNotEqual(classifyTriangle(1, 2, 100), 'Right', '1, 2, 100 should not be a triangle')
        self.assertNotEqual(classifyTriangle(100, 100, 100), 'Right', '100, 100, 100 should be an equilateral '
                                                                          'triangle')
        self.assertNotEqual(classifyTriangle(76, 76, 37), 'Right', '76, 76, 37 should be an isosceles triangle')
        self.assertNotEqual(classifyTriangle(20, 99, 101), 'NotATriangle', '20, 99, 101 should be a right triangle')
        self.assertNotEqual(classifyTriangle(20, 99, 100), 'NotATriangle', '76, 76, 37 should be a scalene triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

