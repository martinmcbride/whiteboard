# Author:  Martin McBride
# Created: 2023-03-12
# Copyright (C) 2023, Martin McBride
# License: MIT

import wx

class Board(wx.Panel):
    def __init__(self, parent, items):
        wx.Panel.__init__(self, parent=parent)
        self.items = items
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        #self.Bind(wx.EVT_SIZE, self.on_size)
        self.Bind(wx.EVT_PAINT, self.on_paint)

    # def on_size(self, event):
    #     self.Refresh()
    #     #event.Skip()

    def on_paint(self, event):
        w, h = self.GetClientSize()
        dc = wx.AutoBufferedPaintDC(self)
        dc.Clear()
        for item in self.items.items:
            item.draw(dc)



