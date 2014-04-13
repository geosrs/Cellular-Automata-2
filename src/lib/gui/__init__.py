# gui.__init__.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains the graphical interface modules

### Imports

import tk.ttkExtra as tk

from lib.constants import *
from screens import *
from wm import *

### Main classes

class App(tk.BaseCustomWindow):
	'''Main application'''
	def __init__(self, master):
		self.master = master
		self.master.title(NAME)
		self.WM = WindowManager(self.master, grid_options = {'row': 1, 'pady': 5})
		self.createScreens()
		self.WM.open(START)
		self.copyrightLabel = tk.Label(self.master, text = COPYRIGHT)
		self.copyrightLabel.grid(row = 2, pady = 5)

	def createScreens(self):
		'''Creates all of the screens'''
		self.startScreen = StartScreen(self.master, self.WM)
		self.programScreen = CAScreen(self.master, self.WM)

		self.WM.set({
			START: self.startScreen,
			MAIN_PROGRAM: self.programScreen,
			})
