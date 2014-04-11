# screens.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains the window screens

import tk.ttkExtra as tk

from constants import *

class StartScreen(tk.Frame):
	'''Start screen for the entire application'''
	def __init__(self, master, wm):
		self.master = master
		self.WM = wm
		tk.Frame.__init__(self, self.master)
		self.createInterface()
		
	def createInterface(self):
		'''Creates the main interface'''
		self.mainFrame = self
		self.leftFrame = tk.Frame(self.mainFrame)
		self.rightFrame = tk.Frame(self.mainFrame)
		self.centerFrame = tk.Frame(self.mainFrame)
		self.mainLabel = tk.Label(self.mainFrame, text = NAME)
		self.aboutButton = tk.Button(self.leftFrame, text = "About CA", command = lambda: self.WM.open(ABOUT))
		self.creditsButton = tk.Button(self.leftFrame, text = "Credits", command = lambda: self.WM.open(CREDITS))
		self.startButton = tk.Button(self.rightFrame, text = "Start", command = lambda: self.WM.open(MAIN_PROGRAM))
		self.helpButton = tk.Button(self.rightFrame, text = "Help", command = lambda: self.WM.open(HELP))
		self.historyButton = tk.Button(self.mainFrame, text = "User History", command = lambda: self.WM.open(HISTORY))
		self.exitButton = tk.Button(self.mainFrame, text = "Exit", command = None, style = "Quit.TButton")
		# command used to be self.close, but this is a Frame now (not a window)

		self.aboutButton.pack(side = "top")
		self.creditsButton.pack(side = "bottom")
		self.historyButton.pack(side = "top")
		self.exitButton.pack(side = "bottom")
		self.startButton.pack(side = "top")
		self.helpButton.pack(side = "bottom")
		self.leftFrame.pack(side = "left", fill = "both")
		self.rightFrame.pack(side = "right", fill = "both")
		# self.centerFrame.pack(side = "top", fill = "both")
		# self.mainFrame.gridWidgets([
			# (self.aboutButton, self.historyButton, self.startButton),
			# (None, self.mainLabel),
			# (self.creditsButton, self.exitButton, self.helpButton)
			# ])
		
		self.mainFrame.pack(side = "top", fill = "both", expand = True, ipadx = 15)
	
class CAScreen(tk.Frame):
	'''Houses the entire Cellular Automata interface'''
	def __init__(self, master, wm):
		self.master = master
		self.WM = wm
		tk.Frame.__init__(self, self.master)