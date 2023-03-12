# Author:  Martin McBride
# Created: 2023-03-12
# Copyright (C) 2023, Martin McBride
# License: MIT

import wx

class FolderTree(wx.TreeCtrl):

    def __init__(self, parent, id, pos, size, style):
        wx.TreeCtrl.__init__(self, parent, id, pos, size, style)
        self.root = self.AddRoot('FolderTree')
        self.SetItemData(self.root, ('key', 'value'))
        os = self.AppendItem(self.root, 'Operating Systems')
        self.Expand(self.root)
