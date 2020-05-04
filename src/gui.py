"""Program to draw Mandelbrot fractals: the graphical user interface.

Author: Lars van den Haak and Tom Verhoeff

Copyright (c) 2020 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.

* Contributor 1: ...
* TU/e ID number 1: ...
* Contributor 2: ...
* TU/e ID number 2: ...
* Date: ...
"""
from PIL import Image, ImageTk  # type: ignore
import tkinter as tk
from mandel import *
from typing import Callable


def squares(px: int, py: int, c1: Color = GREEN, c2: Color = BLUE) -> Color:
    """Colors the screen in squares of 20 pixels

    :param: px: pixel x-coordinate
    :param: py: pixel y-coordinate
    :param: c1: Color of the first type of square
    :param: c2: Color of the second type of square
    :return: Color for the input pixel
    """
    if px // 20 % 2 == py // 20 % 2:
        c = c1
    else:
        c = c2
    return c


class GUI:
    """A class where we make our Graphical User Interface based on TkInter
    """
    def __init__(self) -> None:
        self.image = None
        self.window = tk.Tk()
        self.canvas = tk.Label(self.window, image=None)
        self.canvas.pack(side="bottom", fill="both", expand="yes")


def make_image(gui: GUI, colorize: Callable[[int, int], Color] = squares) -> None:
    """Puts an image on screen created by a function

    :param: gui: An instance from the GUI class
    :param: colorize: A function that gives a color to each pixel
    """
    img = Image.new('RGB', (600, 600))
    for x in range(0, 600):
        for y in range(0, 600):
            img.putpixel((x, y), colorize(x, y))

    tkimg = ImageTk.PhotoImage(img)
    # Save the image to the gui class, otherwise it gets garbage collected
    gui.image = tkimg
    canvas = gui.canvas

    canvas.configure(image=tkimg)
    canvas.pack(side="bottom", fill="both", expand="yes")
