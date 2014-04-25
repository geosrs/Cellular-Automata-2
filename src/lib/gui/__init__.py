# gui.__init__.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains the graphical interface modules

### Imports

import tk.ttkExtra as tk

from lib.constants import *
from screens import *
from styles import *
from grid import *
from wm import *

### Main classes

class App(tk.BaseCustomWindow):
	'''Main application'''
	def __init__(self, master):
		self.master = master
		self.master.title(NAME)
		self.master.geometry("{w}x{h}".format(w = int(tk.SCREENDIM['w'] * 0.66), h = int(tk.SCREENDIM['h'] * 0.66)))
		self.WM = WindowManager(self.master,
			place_options = {'anchor': tk.CENTER, 'relx': 0.5, 'rely': 0.5})
		self.createScreens()
		self.WM.open(START)
		self.copyrightLabel = tk.Label(self.master, text = COPYRIGHT)
		self.copyrightLabel.place(anchor = tk.S, relx = 0.5, rely = 1)

	def cleanup(self):
		'''Actions before the program closes'''
		DATABASE.close()

	def createScreens(self):
		'''Creates all of the screens'''
		self.startScreen = StartScreen(self.master, self.WM)
		self.programScreen = CAScreen(self.master, self.WM)
		self.aboutScreen = AboutScreen(self.master, self.WM)
		self.creditsScreen = CreditsScreen(self.master, self.WM)
		self.historyScreen = HistoryScreen(self.master, self.WM)
		self.optionsCellspaceScreen = Options_CellspaceScreen(self.master, self.WM)
		self.optionsInterestScreen = Options_InterestScreen(self.master, self.WM)
		self.optionsRulesScreen = Options_RuleScreen(self.master, self.WM)
		self.drawScreen = DrawScreen(self.master, self.WM)
		
		self.WM.set({ # Set the Window Manager's screens
			START: self.startScreen,
			MAIN_PROGRAM: self.programScreen,
			ABOUT: self.aboutScreen,
			CREDITS: self.creditsScreen,
			HISTORY: self.historyScreen,
			OPTIONS_SPACE: self.optionsCellspaceScreen,
			OPTIONS_INTEREST: self.optionsInterestScreen,
			OPTIONS_RULES: self.optionsRulesScreen,
			DRAW: self.drawScreen,
			})
