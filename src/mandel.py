"""Program to draw Mandelbrot fractals: the Mandelbrot algorithm.

Author: Lars van den Haak and Tom Verhoeff

Copyright (c) 2020 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.

* Contributor 1: ...
* TU/e ID number 1: ...
* Contributor 2: ...
* TU/e ID number 2: ...
* Date: ...
"""
from typing import List, Tuple, Sequence
import math

#: The type of 2D points.
Point = Tuple[float, float]


#: TODO: define this function
def mandel_seq(x: float, y: float, n: int = 100) -> Sequence[Point]:
    """Return the mandel sequence for the input point (x, y), using n as upper bound.

    Assumptions:

    * start the sequence at (u_0, v_0) = (0, 0)
    * The coordinate (x, y) will have mandel number n,
      when the sequence starts diverging at (u_n,  v_n)

    :param x: x-coordinate of the point for which the sequence is computed
    :param y: y-coordinate of the point for which the sequence is computed
    :param n: upper bound to detect divergence
    :return: the mandel sequence for the point (x, y)

    :examples:

    >>> mandel_seq(1, 0)
    [(0.0, 0.0), (1.0, 0.0), (2.0, 0.0), (5.0, 0.0)]
    >>> mandel_seq(0, 0, n = 1)
    [(0.0, 0.0), (0.0, 0.0)]
    """
    return []


#: TODO: define this function
def mandel_number(x: float, y: float, n: int = 100) -> int:
    """Return the mandel-number of point (x, y).

    This is the smallest index of the mandel sequence at which u_n^2 + v_n^2 > 4.

    Assumptions:

    * the sequence diverges when u_n^2 + v_n^2 > 4

    :param x: x-coordinate of the point for which the Mandel number is computed
    :param y: y-coordinate of the point for which the Mandel number is computed
    :param n: upper bound to detect divergence
    :return: the mandel-number of point (x, y).

    :examples:

    >>> mandel_number(1, 0)
    3
    >>> mandel_number(0, 0, n = 10)
    10
    """
    return 0


#: The type of colors
Color = Tuple[int, int, int]
#: The standard color
STDC: Color = (140, 0, 255)
#: Black
BLACK: Color = (0, 0, 0)
#: Grey
GREY: Color = (128, 128, 128)
#: White
WHITE: Color = (255, 255, 255)
#: Red
RED: Color = (255, 0, 0)
#: Green
GREEN: Color = (0, 255, 0)
#: Blue
BLUE: Color = (0, 0, 255)


#: TODO: define this function
#: TODO: document this
def convert_pixel(x: int, y: int) -> Point:
    return (0, 0)


#: TODO: define this function
#: TODO: document this
def generate_mandel_nums() -> List[List[int]]:
    return []


#: TODO: define this function
def color_mandel(px: int, py: int, n: int = 100, c1: Color = GREEN) -> Color:
    """Return the colour of the given pixel.

    Assumptions:
    * pixels that that diverge immediately -> BLACK
    * pixels that do not diverge after n iterations -> BLACK
    * colour scaled based on the squared root of the mandel number

    :param: px: pixel x-coordinate
    :param: py: pixel y-coordinate
    :param: n: maximum number of iterations, after which the pixel is coloured BLACK
    :return: Color(as a defined Tuple - lines 48) for the input pixel

    :examples:

    TODO: doctests
    """
    return (0, 0, 0)
