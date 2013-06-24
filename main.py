# -*- coding:utf-8 -*-

import sys,os
import wx
import layout as lyt

""" 

"""

#---------------------------------------------------------------------------



#---------------------------------------------------------------------------

class App(wx.App):
    def OnInit(self):
        self.frame = lyt.myFrame(None, wx.ID_ANY, "")
        
#         self.frame.SetSize((800,600))
        self.SetTopWindow(self.frame)
        self.frame.Show()
        
        return True


#---------------------------------------------------------------------------


overview = """\
"""


if __name__ == '__main__':
    app = App(0)
    app.MainLoop()
