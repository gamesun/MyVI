
import sys,os
import wx

""" 

"""

#---------------------------------------------------------------------------

class MyFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, -1, title, size = (800,500), 
            style=wx.DEFAULT_FRAME_STYLE|wx.NO_FULL_REPAINT_ON_RESIZE)
        self.Show(True)

        


#---------------------------------------------------------------------------

class App(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, "test")
        self.SetTopWindow(frame)

        return True


#---------------------------------------------------------------------------


overview = """\
"""


if __name__ == '__main__':
    app = App(0)
    app.MainLoop()
