import wx
from playsound import playsound

class MyFrame(wx.Frame):    
    def __init__(self):
        super().__init__(parent=None, title='vine_boom_sfx testing app')
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        my_btn = wx.Button(panel, label='vine boom sfx', pos=(10, 5))
        my_btn.Bind(wx.EVT_BUTTON, self.on_press)
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(my_sizer)
        self.Show()

def on_press(self, event):
    playsound('files/Vine-boom-sound-effect.mp3')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame()
    app.MainLoop()

