# gui.screens.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains the window screens

### Imports

import tk.ttkExtra as tk

from lib.constants import *
from wm import *

### Main classes

class Screen(tk.Frame):
	'''Base screen class'''
	def __init__(self, master, wm):
		self.master = master
		self.WM = wm
		tk.Frame.__init__(self, self.master)
		self.createInterface()
		
	def createInterface(self):
		'''Override in child classes'''
		pass

class StartScreen(Screen):
	'''Start screen for the entire application'''
	def createInterface(self):
		'''Creates the main interface'''
		self.mainLabel = tk.Label(self, text = NAME)
		self.aboutButton = tk.Button(self, text = "About CA", command = lambda: self.WM.open(ABOUT))
		self.creditsButton = tk.Button(self, text = "Credits", command = lambda: self.WM.open(CREDITS))
		self.startButton = tk.Button(self, text = "Start", command = lambda: self.WM.open(MAIN_PROGRAM))
		self.helpButton = tk.Button(self, text = "Help", command = lambda: self.WM.open(HELP))
		self.historyButton = tk.Button(self, text = "User History", command = lambda: self.WM.open(HISTORY))
		self.exitButton = tk.Button(self, text = "Exit", command = self.master.close, style = "Quit.TButton")

		self.gridWidgets([
			self.mainLabel,
			self.startButton,
			self.aboutButton,
			self.creditsButton,
			self.helpButton,
			self.historyButton,
			self.exitButton,
			])
		
		self.pack(side = "top", fill = "both", expand = True, ipadx = 15)
	
class CAScreen(Screen):
	'''Houses the entire Cellular Automata interface'''
	def createInterface(self):
		'''Creates the main interface for the CA window'''
		self.homeFrame = tk.Frame(self)
		self.homeText = tk.Label(self.homeFrame, text = NAME)
		self.homeButton = tk.Button(self.homeFrame, text = "Home", command = lambda: self.WM.open(START))
		self.nextButton = tk.Button(self.homeFrame, text = "Next", command = lambda: self.WM.open(OPTIONS_SPACE))
		self.homeFrame.gridWidgets([
			self.homeText,
			(self.homeButton, self.nextButton)
			])
		self.homeFrame.grid()
		
class Options_Cellspace(Screen):
	'''Cellspace Options window'''
	def createInterface(self):
		'''Creates the interface for the Cellspace Options window'''
		self.mainLabel = tk.Label(self, text = "Cellspace")
		