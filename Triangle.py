# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a, b, c):
    """
    Classify a triangle based on side lengths a, b, c.

    Returns:
        'InvalidInput'   if inputs are not valid integers in the allowed range (>0 and <=200)
        'NotATriangle'   if the sides do not satisfy triangle inequality
        'Equilateral'    if all three sides are equal
        'Right'          if it is a right triangle (Pythagorean triple)
        'Isosceles'      if exactly two sides are equal
        'Scalene'        if all sides are different
    """

    # --- Input validation ---
    # All sides must be integers
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # Each side must be > 0
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # Each side must be <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # --- Triangle inequality ---
    if (a + b) <= c or (a + c) <= b or (b + c) <= a:
        return 'NotATriangle'

    # --- Equilateral ---
    if a == b == c:
        return 'Equilateral'

    # --- Right triangle ---
    sides = sorted([a, b, c])
    x, y, z = sides[0], sides[1], sides[2]
    if x * x + y * y == z * z:
        return 'Right'

    # --- Isosceles ---
    if a == b or b == c or a == c:
        return 'Isosceles'

    # --- Scalene ---
    return 'Scalene'
