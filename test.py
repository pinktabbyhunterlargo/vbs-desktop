import wx

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='vine_boom_sfx testing app')
        panel = wx.Panel(self)

        my_btn = wx.Button(panel, label='vine boom sfx', pos=(10, 5))

        self.Show()

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()

