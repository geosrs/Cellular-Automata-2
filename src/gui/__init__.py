# __init__.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains the graphical interface modules

import tk.ttkExtra as tk

from wm import *
from screens import *
from constants import *

class App(tk.BaseCustomWindow):
	'''Main application'''
	def __init__(self, master):
		self.master = master
		self.master.title(NAME)
		self.wm = WindowManager(self.master)
		self.createScreens()
		self.wm.open(START)

	def createScreens(self):
		'''Creates all of the screens'''
		self.startScreen = StartScreen(self.master, self.wm)
		self.programScreen = CAScreen(self.master, self.wm)

		self.wm.set({
			START: self.startScreen,
			MAIN_PROGRAM: self.programScreen,
			})
