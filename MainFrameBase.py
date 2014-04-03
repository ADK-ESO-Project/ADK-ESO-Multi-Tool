"""Subclass of MainFrameBase, which is generated by wxFormBuilder."""

import wx
import gui

# Implementing MainFrameBase
class MainFrameBase( gui.MainFrameBase ):
	def __init__( self, parent ):
		gui.MainFrameBase.__init__( self, parent )
	
	# Handlers for MainFrameBase events.
	def DownloadButtonClick( self, event ):
		wx.MessageBox("No Function yet","ESO Multi-Tool")
	
	def UploadButtonClick( self, event ):
		wx.MessageBox("No Function yet","ESO Multi-Tool")
	
	def m_mniOpenClick( self, event ):
		fdlg = wx.FileDialog(self,"Choose a file","Open file",wx.EmptyString,"*.*",wx.FD_OPEN | wx.FD_FILE_MUST_EXIST);
		if fdlg.ShowModal() != wx.ID_OK:
			return;
		self.m_rtMain.LoadFile(fdlg.GetPath())
	
	def m_mniSaveClick( self, event ):
		fdlg = wx.FileDialog(self,"Choose a file","Save file",wx.EmptyString,"*.*",wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT);
		if fdlg.ShowModal() != wx.ID_OK:
			return;
		self.m_rtMain.SaveFile(fdlg.GetPath())
	
	def m_mniExitClick( self, event ):
		self.Close()
	
	def m_mniAboutClick( self, event ):
		wx.MessageBox("ADK ESO Multi-Tool Written By Raziel23x.","ESO Multi-Tool")
