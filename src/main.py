# Author:  Martin McBride
# Created: 2023-03-12
# Copyright (C) 2023, Martin McBride
# License: MIT

import wx
from foldertree import FolderTree
from board import Board
from boarditems import BoardItems


class TreePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.tree = FolderTree(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_HAS_BUTTONS)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        self.SetSizer(sizer)

class View(wx.Panel):
    def __init__(self, parent):
        super(View, self).__init__(parent)
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

class MainFrame(wx.Frame):

    def __init__(self, items):
        wx.Frame.__init__(self, parent=None, title='TreeCtrl Demo')
        splitter = wx.SplitterWindow(self, style = wx.SP_LIVE_UPDATE)
        board_panel = Board(splitter, items)
        tree_panel = TreePanel(splitter)

        # split the window
        splitter.SplitVertically(tree_panel, board_panel)
        splitter.SetMinimumPaneSize(300)
        self.Show()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    board_items = BoardItems()
    frame = MainFrame(board_items)
    app.MainLoop()