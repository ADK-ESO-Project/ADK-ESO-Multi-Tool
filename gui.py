# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

m_mniOpenId = 1000
m_mniSaveId = 1001
m_mniExitId = 1002
m_mniAboutId = 1003
DownloadButtonID = 1004
SubmitButtonID = 1005

###########################################################################
## Class MainFrameStart
###########################################################################

class MainFrameStart ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ESO Multi-Tool", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar = wx.MenuBar( 0 )
		self.m_mnFile = wx.Menu()
		self.m_mniOpen = wx.MenuItem( self.m_mnFile, m_mniOpenId, u"&Open...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_mniOpen )
		
		self.m_mniSave = wx.MenuItem( self.m_mnFile, m_mniSaveId, u"&Save...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_mniSave )
		
		self.m_mnFile.AppendSeparator()
		
		self.m_mniExit = wx.MenuItem( self.m_mnFile, m_mniExitId, u"&Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_mniExit )
		
		self.m_menubar.Append( self.m_mnFile, u"&File" ) 
		
		self.m_mnHelp = wx.Menu()
		self.m_mniAbout = wx.MenuItem( self.m_mnHelp, m_mniAboutId, u"&About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnHelp.AppendItem( self.m_mniAbout )
		
		self.m_menubar.Append( self.m_mnHelp, u"&?" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.m_mniOpenClick, id = self.m_mniOpen.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniSaveClick, id = self.m_mniSave.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniExitClick, id = self.m_mniExit.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniAboutClick, id = self.m_mniAbout.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def m_mniOpenClick( self, event ):
		event.Skip()
	
	def m_mniSaveClick( self, event ):
		event.Skip()
	
	def m_mniExitClick( self, event ):
		event.Skip()
	
	def m_mniAboutClick( self, event ):
		event.Skip()
	

###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"ESO Multi-Tool", pos = wx.DefaultPosition, size = wx.Size( 671,492 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_rtMain = wx.richtext.RichTextCtrl( self.m_panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_AUTO_URL|wx.HSCROLL|wx.SUNKEN_BORDER|wx.VSCROLL|wx.WANTS_CHARS )
		bSizer4.Add( self.m_rtMain, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.DownloadButton = wx.Button( self.m_panel, DownloadButtonID, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DownloadButton.SetToolTipString( u"Download latest Database" )
		
		bSizer5.Add( self.DownloadButton, 0, wx.ALL, 5 )
		
		self.SubmitButton = wx.Button( self.m_panel, SubmitButtonID, u"Submit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SubmitButton.SetToolTipString( u"Upload Your changes to the database" )
		
		bSizer5.Add( self.SubmitButton, 0, wx.ALL, 5 )
		
		
		bSizer4.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		
		bSizer3.Add( bSizer4, 1, wx.EXPAND, 5 )
		
		
		self.m_panel.SetSizer( bSizer3 )
		self.m_panel.Layout()
		bSizer3.Fit( self.m_panel )
		bSizer2.Add( self.m_panel, 1, wx.EXPAND |wx.ALL, 0 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		self.m_menubar = wx.MenuBar( 0 )
		self.m_mnFile = wx.Menu()
		self.m_mniOpen = wx.MenuItem( self.m_mnFile, m_mniOpenId, u"&Open...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_mniOpen )
		
		self.m_mniSave = wx.MenuItem( self.m_mnFile, m_mniSaveId, u"&Save...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_mniSave )
		
		self.m_mnFile.AppendSeparator()
		
		self.m_mniExit = wx.MenuItem( self.m_mnFile, m_mniExitId, u"&Exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnFile.AppendItem( self.m_mniExit )
		
		self.m_menubar.Append( self.m_mnFile, u"&File" ) 
		
		self.m_mnHelp = wx.Menu()
		self.m_mniAbout = wx.MenuItem( self.m_mnHelp, m_mniAboutId, u"&About", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnHelp.AppendItem( self.m_mniAbout )
		
		self.m_menubar.Append( self.m_mnHelp, u"&?" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		
		# Connect Events
		self.DownloadButton.Bind( wx.EVT_BUTTON, self.DownloadButtonClick )
		self.SubmitButton.Bind( wx.EVT_BUTTON, self.SubmitButtonClick )
		self.Bind( wx.EVT_MENU, self.m_mniOpenClick, id = self.m_mniOpen.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniSaveClick, id = self.m_mniSave.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniExitClick, id = self.m_mniExit.GetId() )
		self.Bind( wx.EVT_MENU, self.m_mniAboutClick, id = self.m_mniAbout.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def DownloadButtonClick( self, event ):
		event.Skip()
	
	def SubmitButtonClick( self, event ):
		event.Skip()
	
	def m_mniOpenClick( self, event ):
		event.Skip()
	
	def m_mniSaveClick( self, event ):
		event.Skip()
	
	def m_mniExitClick( self, event ):
		event.Skip()
	
	def m_mniAboutClick( self, event ):
		event.Skip()
	

