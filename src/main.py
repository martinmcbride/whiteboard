import wx
from foldertree import FolderTree


class BoardPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)


class TreePanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.tree = FolderTree(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_HAS_BUTTONS)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.tree, 0, wx.EXPAND)
        self.SetSizer(sizer)


class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, parent=None, title='TreeCtrl Demo')
        splitter = wx.SplitterWindow(self)
        board_panel = BoardPanel(splitter)
        tree_panel = TreePanel(splitter)

        # split the window
        splitter.SplitVertically(tree_panel, board_panel)
        splitter.SetMinimumPaneSize(200)
        self.Show()


if __name__ == '__main__':
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()