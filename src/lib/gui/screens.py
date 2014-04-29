# gui.screens.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains the window screens

### Imports

import tk.ttkExtra as tk
import tk.graphics as graph

from lib.constants import *
from grid import *
from wm import *

### Main classes

class Screen(tk.Frame):
	'''Base screen class'''
	current = START
	prev = START
	next = MAIN_PROGRAM

	def __init__(self, master, wm, n = None):
		self.master = master
		self.WM = wm
		tk.Frame.__init__(self, self.master) # create a new Frame instance
		if not n is None:
			self.current = n
			self.prev = n - 1
			self.next = n + 1
		self.createInterface()

	def createInterface(self):
		'''Override in child classes'''
		pass

	def setOptions(self):
		'''Override in child classes'''
		return True

	def onload(self):
		'''Override in child classes'''
		pass

	def addNavigator(self, next = None, prev = None, **options):
		'''Adds the navigation buttons'''
		nextCommand = options.get("nextCommand", lambda: self.setOptions())
		prevCommand = options.get("prevCommand", lambda: self.setOptions())
		if not next:
			next = self.next
		if not prev:
			prev = self.prev
		self.nextButton = tk.Button(self, text = next, command = lambda: nextCommand() + self.WM.open(self.next))
		self.prevButton = tk.Button(self, text = prev, command = lambda: prevCommand() + self.WM.open(self.prev))

class RuleDisplay(tk.Frame):
	'''Displays a set of Celullar Automata rules'''
	def __init__(self, master, width = 5):
		self.master = master
		tk.Frame.__init__(self, self.master)
		self.rules = {}
		self.width = width
		self.createInterface()

	def createInterface(self):
		'''Creates the Rule display interface'''
		self.buttonFrame = tk.Frame(self)
		self.current = tk.Label(self, text = "No Rules")

		self.buttonFrame.grid(row = 1, pady = 5)
		self.current.grid(row = 2, pady = 5)

	def click(self, rule):
		'''Shows a specific rule'''
		frame = self.rules[rule]
		self.current.grid_remove()
		frame.grid()
		self.current = frame

	def addRule(self, number, frame):
		'''Adds a rule to the display'''
		self.rules[number] = frame
		ruleButton = tk.Button(self.buttonFrame, text = number, command = lambda: self.click(number), width = 5)
		self.click(number)
		column = number % self.width
		if column == 0:
			column = self.width
		ruleButton.grid(row = int((number - 1) / self.width), column = column, padx = 5, pady = 5)

### Main display screens

class StartScreen(Screen):
	'''Start screen for the entire application'''
	current = START

	def createInterface(self):
		'''Creates the main interface'''
		self.mainLabel = tk.Label(self.master, text = NAME, style = "Header.TLabel")
		self.aboutButton = tk.Button(self, text = "About CA", command = lambda: self.WM.open(ABOUT))
		self.creditsButton = tk.Button(self, text = "Credits", command = lambda: self.WM.open(CREDITS))
		self.startButton = tk.Button(self, text = "Start", command = lambda: self.WM.open(MAIN_PROGRAM))
		self.historyButton = tk.Button(self, text = "User History", command = lambda: self.WM.open(HISTORY))
		self.exitButton = tk.Button(self, text = "Exit", command = self.master.close, style = "Quit.TButton")

		self.mainLabel.place(anchor = tk.N, relx = 0.5, y = 0)

		self.gridWidgets([
			self.startButton,
			self.aboutButton,
			self.creditsButton,
			self.historyButton,
			self.exitButton,
			], pady = 5)
		
		self.pack(side = "top", fill = "both", expand = True, ipadx = 15)
	
class AboutScreen(Screen):
	'''Shows the about information'''
	current = ABOUT
	prev = START

	def createInterface(self):
		'''Creates the main About interface'''
		self.mainLabel = tk.Label(self, text = "About", style = "Subheader.TLabel")
		self.screenFrame = tk.Frame(self)
		self.screens_wm = WindowManager(self.screenFrame,
			place_options = {'anchor': tk.CENTER, 'relx': 0.5, 'rely': 0.5})
		self.addScreens()
		self.screens_wm.open(1)
		self.addNavigator(prev = "Home")

		self.gridWidgets([
			self.mainLabel,
			self.screenFrame,
			self.prevButton,
			], padx = 5, pady = 5)

	def addScreens(self):
		'''Adds the screens to the widget'''
		self.initialScreen = Screen(self.screenFrame, self.screens_wm, 1)
		self.secondScreen = Screen(self.screenFrame, self.screens_wm, 2)

		for screen in [self.initialScreen, self.secondScreen]:
			screen.addNavigator()

		self.screens_wm.set({
			1: self.initialScreen,
			2: self.secondScreen,
			})
	
class HistoryScreen(Screen):
	'''Shows the user's history'''
	current = HISTORY
	prev = START

	def createInterface(self):
		'''Displays user history'''
		self.baseQuery = "SELECT * FROM history ORDER BY `time` DESC LIMIT {limit} OFFSET {offset}"
		self.db = DATABASE
		self.db.setTable("history")
		self.displayed = []

		self.mainLabel = tk.Label(self, text = "History", style = "Subheader.TLabel")
		self.searchLabel = tk.Label(self, text = "Search")
		self.searchEntry = tk.Entry(self, justify = tk.CENTER)
		self.historyFrame = tk.Frame(self)
		self.addNavigator(prev = "Home")

		self.gridWidgets([
			self.mainLabel,
			(self.searchLabel, self.searchEntry),
			self.historyFrame,
			self.prevButton,
			], padx = 5, pady = 5)

	def onload(self):
		'''Loads the latest rows'''
		self.displayRows(0, 10) # show the ten most recent rules

	def displayRows(self, start = 0, end = 10):
		'''Displays the rows from "start" to "end"'''
		row_cursor = self.db.query(self.baseQuery.format(limit = end - start, offset = start))
		rows = self.db.fetch(row_cursor)
		for widget in self.displayed:
			widget.grid_forget()
		for row_number, row in enumerate(rows, 1):
			image_rule, rule, rule_number = row["image"], row["rule"], row["rule_number"]
			ruleFrame = tk.Frame(self.historyFrame)
			numberLabel = tk.Label(ruleFrame, text = rule_number)
			ruleLabel = tk.Label(ruleFrame, text = image_rule if image_rule else rule)
			numberLabel.pack(side = "left")
			ruleLabel.pack(side = "right")
			ruleFrame.grid(row = row_number)
			ruleFrame.bind("<Button-1>", lambda event: self.openRule(rule_number))
			self.displayed.append(ruleFrame)

	def openRule(self, number):
		'''Opens the "number" rule'''
		print number, type(number)

class CreditsScreen(Screen):
	'''Shows the creator credits'''
	current = CREDITS
	prev = START

	def createInterface(self):
		'''Creates the main Credits interface'''
		self.mainLabel = tk.Label(self, text = "About", style = "Subheader.TLabel")
		self.creditsText = tk.ScrolledText(self, height = 10, font = "Calibri 12")
		self.creditsText.insert(tk.END, DATA.credits.text)
		self.creditsText.configure(state = tk.DISABLED)
		self.addNavigator(prev = "Home")

		self.gridWidgets([
			self.mainLabel,
			self.creditsText,
			self.prevButton,
			], padx = 5, pady = 5)

### Cellular Automata-related screens
	
class CAScreen(Screen):
	'''Houses the entire Cellular Automata interface'''
	current = MAIN_PROGRAM
	prev = START
	next = OPTIONS_SPACE

	def createInterface(self):
		'''Creates the main interface for the CA window'''
		self.homeText = tk.Label(self, text = "Welcome to " + NAME, style = "Subheader.TLabel")
		self.addNavigator("Next", "Home")

		self.gridWidgets([
			self.homeText,
			(self.prevButton, self.nextButton)
			], pady = 5)
		
class Options_CellspaceScreen(Screen):
	'''Cellspace Options window'''
	current = OPTIONS_SPACE
	prev = MAIN_PROGRAM
	next = OPTIONS_INTEREST

	def createInterface(self):
		'''Creates the interface for the Cellspace Options window'''
		self.mainLabel = tk.Label(self, text = "Cellspace", style = "Subheader.TLabel")
		self.widthLabel = tk.Label(self, text = "Grid Width", style = "OptionHeader.TLabel")
		self.widthSlider = tk.LabelledScale(self, type = int, from_ = 1, to = tk.SCREENDIM["width"],
			length = 250, default = OPTIONS.width, step = 5, edit = True)
		self.heightFrame = tk.Frame(self)
		self.heightLabel = tk.Label(self.heightFrame, text = "Grid Height", style = "OptionHeader.TLabel")
		self.heightSlider = tk.LabelledScale(self.heightFrame, type = int, from_ = 1, to = tk.SCREENDIM["height"], 
			length = 250, default = OPTIONS.height, step = 5, edit = True)
		self.dimensionVar = tk.IntVar(self)
		self.dimensionVar.set(OPTIONS.dimension)
		# disable the height slider if 1D is selected
		self.dim1D = tk.Radiobutton(self, text = "1 Dimensional", value = 1,
			variable = self.dimensionVar, command = lambda: self.toggleHeight(False))
		self.dim2D = tk.Radiobutton(self, text = "2 Dimensional", value = 2,
			variable = self.dimensionVar, command = lambda: self.toggleHeight(True))
		self.addNavigator()

		self.heightLabel.grid(row = 1, pady = 5)
		self.heightSlider.grid(row = 2, pady = 5)

		self.gridWidgets([
			self.mainLabel,
			self.widthLabel,
			self.widthSlider,
			(self.dim1D, self.dim2D),
			self.heightFrame,
			(self.prevButton, self.nextButton)
			], pady = 5)

	def toggleHeight(self, on):
		'''Toggles the Height frame'''
		self.heightFrame.grid() if on else self.heightFrame.grid_remove()

	def setOptions(self, again = False):
		'''Sets the global options'''
		setOption("width", self.widthSlider.get())
		setOption("height", self.heightSlider.get())
		setOption("dimension", self.dimensionVar.get())
		return True

class Options_InterestScreen(Screen):
	'''Allows the user to select a cell of interest'''
	current = OPTIONS_INTEREST
	prev = OPTIONS_SPACE
	next = OPTIONS_RULES

	def createInterface(self):
		'''Creates the Cell of Interest interface'''
		self.mainLabel = tk.Label(self, text = "Cell of Interest", style = "Subheader.TLabel")
		self.caGrid = CAGrid(self, 5, 1 if OPTIONS.dimension == 1 else 5)
		self.addNavigator()

		self.gridWidgets([
			self.mainLabel,
			self.caGrid,
			(self.prevButton, self.nextButton),
			], pady = 5)

	def setOptions(self):
		'''Sets the global options'''
		clicked =  self.caGrid.clicked()
		setOption("interest", clicked[0] if clicked else OPTIONS.interest)
		return True

	def onload(self):
		'''Called when the screen is loaded'''
		newHeight = 1 if OPTIONS.dimension == 1 else 5
		if newHeight != self.caGrid.height:
			# dimension changed --- create a new CAGrid
			self.caGrid.configure(height = int(self.caGrid.configure("height")[-1]) * (1.0/5if OPTIONS.dimension == 1 else 5))
			self.caGrid.draw(5, newHeight)
			self.caGrid.toggle([sorted(self.caGrid.cells.keys())[OPTIONS.interest]])
		return True

class Options_RuleScreen(Screen):
	'''Interface for user to add Celluar Automata rules'''
	current = OPTIONS_RULES
	prev = OPTIONS_INTEREST
	next = DRAW

	def createInterface(self):
		'''Creates the Rules interface'''
		self.currentRule = 1
		self.rules = {}
		self.mainLabel = tk.Label(self, text = "Rules", style = "Subheader.TLabel")
		self.ruleFrame = RuleDisplay(self, 5)
		self.addRuleButton = tk.Button(self, text = "Add Rule", command = self.addRule)
		self.addNavigator()

		self.gridWidgets([
			self.mainLabel,
			self.ruleFrame,
			self.addRuleButton,
			(self.prevButton, self.nextButton),
			], pady = 5)

	def addRule(self):
		'''Adds a rule to the interface'''
		newRuleFrame = tk.Frame(self.ruleFrame)
		self.rules[self.currentRule] = newRuleFrame
		newRuleFrame.number = self.currentRule
		ruleLabel = tk.Label(newRuleFrame, text = "Rule {n}".format(n = self.currentRule), style = "OptionHeader.TLabel")
		ruleGrid = CAGrid(newRuleFrame, 5, 1 if OPTIONS.dimension == 1 else 5)
		newRuleFrame.ca_grid = ruleGrid

		newRuleFrame.gridWidgets([
			ruleLabel,
			ruleGrid,
			], pady = 5)
		self.ruleFrame.addRule(self.currentRule, newRuleFrame)
		self.currentRule += 1

	def onload(self):
		'''Changes the grid dimensions'''
		newHeight = 1 if OPTIONS.dimension == 1 else 5
		if not self.rules:
			return False
		if newHeight != self.rules.values()[-1].ca_grid.height:
			# dimension changed --- create a new CAGrid
			for rule in self.rules.values():
				grid = rule.ca_grid
				grid.configure(height = int(grid.configure("height")[-1]) * (1.0/5 if OPTIONS.dimension == 1 else 5))
				grid.draw(5, newHeight)
		return True

	def setOptions(self):
		'''Sets  the global options'''
		rules = []
		convert = OPTIONS.dimension == 1
		for rule_grid in self.rules.values():
			rule_list = rule_grid.ca_grid.clicked(convert)
			if rule_list:
				rules.append(rule_list)
		setOption("rules", rules)
		return True

class DrawScreen(Screen):
	'''Displays the Cellular Automata'''
	current = DRAW
	prev = OPTIONS_RULES
	next = MAIN_PROGRAM

	def createInterface(self):
		'''Creates the main CA interface'''
		self.ca_screen = graph.GraphWin(self, width = SETTINGS.width, height = SETTINGS.height)
		self.ca_screen.setBackground("white")
		self.descFrame = tk.Frame(self)
		self.descLabel = tk.Label(self.descFrame, text = "Description", style = "Subheader.TLabel")
		self.description = tk.Label(self.descFrame, text = DATA.about.text)
		self.exampleLabel = tk.Label(self.descFrame, text = "Examples", style = "Subheader.TLabel")
		self.exampleFrame = tk.Frame(self.descFrame)

		self.optionFrame = tk.Frame(self)
		self.options_label = tk.Label(self.optionFrame, text = "Options", style = "Subheader.TLabel")

		self.addNavigator()

		self.descFrame.gridWidgets([
			self.descLabel,
			self.description,
			self.exampleLabel,
			self.exampleFrame,
			])

		self.gridWidgets([
			(self.descFrame, self.ca_screen, self.optionFrame),
			self.nextButton,
			], padx = 5, pady = 5)

	def onload(self):
		'''Draws the Cellular Automata screen'''
		# add the latest rules to the history database
		DATABASE.insert("history", dimension = OPTIONS.dimension, interest = OPTIONS.interest,
			rule = str(OPTIONS.rules))
