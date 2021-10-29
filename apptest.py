#!/usr/bin/env python3

import wx
app = wx.App()
frm = wx.Frame(None, title="vine_boom_sfx testing app")
sfxbtn = wx.Button(None, label='vine_boom_sfx', pos=(5, 5))
frm.Show()
app.MainLoop()
