# Author:  Martin McBride
# Created: 2023-03-12
# Copyright (C) 2023, Martin McBride
# License: MIT

import wx

class Board(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_size(self, event):
        event.Skip()
        self.Refresh()

    def on_paint(self, event):
        w, h = self.GetClientSize()
        dc = wx.AutoBufferedPaintDC(self)
        dc.Clear()
        dc.DrawLine(0, 0, w, h)
        dc.SetPen(wx.Pen(wx.BLACK, 5))
        dc.DrawCircle(w / 2, h / 2, 100)



