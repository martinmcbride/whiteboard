# Author:  Martin McBride
# Created: 2023-03-13
# Copyright (C) 2023, Martin McBride
# License: MIT
from dataclasses import dataclass
import wx


@dataclass
class BoardItem():
    x = 0
    y = 0
    width = 0
    height = 0
    stroke_color = wx.Colour(0, 0, 0)
    stroke_width = 2
    fill_color = wx.Colour(255, 255, 128)


class Rectangle(BoardItem):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, dc):
        dc.SetPen(wx.Pen(self.stroke_color, self.stroke_width, style=wx.SOLID))
        dc.SetBrush(wx.Brush(self.fill_color, wx.SOLID))
        dc.DrawRectangle(self.x, self.y, self.width, self.height)


class BoardItems:

    def __init__(self):
        self.items= []
        rect = Rectangle(100, 100, 100, 200)
        rect.fill_color = wx.Colour("red")
        self.items.append(rect)
        rect = Rectangle(250, 300, 200, 200)
        self.items.append(rect)

