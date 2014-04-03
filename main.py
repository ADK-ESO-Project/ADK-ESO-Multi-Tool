import wx
from MainFrameBase import MainFrameBase


class ADKESOMultiTool(wx.App):
    def OnInit(self):
        self.m_frame = MainFrameBase(None)
        self.m_frame.Show()
        self.SetTopWindow(self.m_frame)
        return True

app = ADKESOMultiTool(0)
app.MainLoop()
