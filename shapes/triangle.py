#!/usr/bin/env python

"""
Author: Lena Lysenko
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape.
"""

import math
from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains three side lenght values
    and number of decimal places to use when computing values.
    """

    decimal_places = 2

    def __init__(self, side1, side2, side3):
        """
        Create the triangle by storing the sides.
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        """
        Compute the area using the formula √p(p − a)(p − b)(p − c) where p = perimeter / 2
        """
        p = self.perimeter() * 0.5
        return round(math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3)), self.decimal_places)

    def perimeter(self):
        """
        Compute the perimeter using the formula side1 + side2 + side3
        """
        return self.side1 + self.side2 + self.side3
