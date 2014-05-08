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
from styles import *

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
		self.current.grid_forget()
		frame.grid(row = 2, pady = 5, columnspan = 3)
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
		self.settingsButton = tk.Button(self, text = "Settings", command = lambda: self.WM.open(SETTINGS_EDIT))
		self.historyButton = tk.Button(self, text = "User History", command = lambda: self.WM.open(HISTORY))
		self.exitButton = tk.Button(self, text = "Exit", command = self.master.close, style = "Quit.TButton")

		self.mainLabel.place(anchor = tk.N, relx = 0.5, y = 0)

		self.gridWidgets([
			self.startButton,
			self.settingsButton,
			self.aboutButton,
			self.creditsButton,
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
		self.aboutText = tk.ScrolledText(self, height = 10, font = "Calibri 12")
		self.aboutText.insert(tk.END, DATA.about.text)
		self.aboutText.configure(state = tk.DISABLED)
		self.addNavigator(prev = "Home")

		self.gridWidgets([
			self.mainLabel,
			self.aboutText,
			self.prevButton,
			], padx = 5, pady = 5)
	
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

class SettingsScreen(Screen):
	"""Allows the user to change the program settings"""
	current = SETTINGS_EDIT
	prev = START

	def createInterface(self):
		'''Creates the main settings interface'''
		self.mainLabel = tk.Label(self, text = "Settings", style = "Subheader.TLabel")
		self.fullscreenVar = tk.IntVar(self)
		self.fullscreenVar.set(SETTINGS.fullscreen)
		self.fullscreenOption = tk.Checkbutton(self, text = "Fullscreen", variable = self.fullscreenVar)
		self.allowInitialVar = tk.IntVar(self)
		self.allowInitialVar.set(SETTINGS.initial)
		self.allowInitialOption = tk.Checkbutton(self, text = "Initial Cellstate Input", variable = self.allowInitialVar)
		self.widthLabel = tk.Label(self, text = "Width", style = "OptionHeader.TLabel")
		self.widthSlider = tk.LabelledScale(self, type = int, from_ = 1, to = tk.SCREENDIM["width"],
			length = 250, default = OPTIONS.width, step = 2, edit = True)
		self.heightLabel = tk.Label(self, text = "Height", style = "OptionHeader.TLabel")
		self.heightSlider = tk.LabelledScale(self, type = int, from_ = 1, to = tk.SCREENDIM["height"],
			length = 250, default = OPTIONS.height, step = 2, edit = True)
		self.fontLabel = tk.Label(self, text = "Program Font", style = "OptionHeader.TLabel")
		self.fontEntry = tk.Entry(self, width = 20, justify = tk.CENTER)
		self.fontEntry.insert(tk.END, SETTINGS.font)
		self.saveButton = tk.Button(self, text = "Save", command = self.saveSettings)
		self.addNavigator()

		self.gridWidgets([
			self.mainLabel,
			self.fullscreenOption,
			self.allowInitialOption,
			(self.fontLabel, self.fontEntry),
			(self.widthLabel, self.widthSlider),
			(self.heightLabel, self.heightSlider),
			self.saveButton,
			self.prevButton,
			], padx = 5, pady = 5)

	def saveSettings(self):
		'''Saves the settings'''
		SETTINGS.fullscreen = bool(self.fullscreenVar.get())
		SETTINGS.font = self.fontEntry.get()
		SETTINGS.initial = bool(self.allowInitialVar.get())

		if SETTINGS.fullscreen:
			self.master.geometry("+0+0")
			self.master.fullscreen(False)
		else:
			self.master.overrideredirect(0)
			self.master.geometry("{w}x{h}".format(w = int(tk.SCREENDIM['w'] * 0.8), h = int(tk.SCREENDIM['h'] * 0.8)))
			self.master.center()
		initializeStyles(self.master)

		saveSettings(SETTINGS)
		self.WM.open(START)

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
		self.dimensionVar = tk.IntVar(self)
		self.dimensionVar.set(OPTIONS.dimension)
		# disable the height slider if 1D is selected
		self.dim1D = tk.Radiobutton(self, text = "1 Dimensional", value = 1,
			variable = self.dimensionVar)
		self.dim2D = tk.Radiobutton(self, text = "2 Dimensional", value = 2,
			variable = self.dimensionVar)
		self.addNavigator()

		self.gridWidgets([
			self.mainLabel,
			(self.dim1D, self.dim2D),
			(self.prevButton, self.nextButton)
			], pady = 5)

	def setOptions(self, again = False):
		'''Sets the global options'''
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
		self.caGrid = CAGrid(self, SETTINGS.width / 2, SETTINGS.height / 10 if OPTIONS.dimension == 1 else SETTINGS.height / 2)
		self.caGrid.draw(5, 1 if OPTIONS.dimension == 1 else 5)
		self.caGrid.toggle([0, 2])
		self.addNavigator()

		self.gridWidgets([
			self.mainLabel,
			self.caGrid,
			(self.prevButton, self.nextButton),
			], pady = 5)

	def setOptions(self):
		'''Sets the global options'''
		clicked =  self.caGrid.clicked()
		shift = -6 if OPTIONS.dimension == 1 else 0
		setOption("interest", clicked[0] + shift if clicked else OPTIONS.interest)
		return True

	def onload(self):
		'''Called when the screen is loaded'''
		newHeight = 1 if OPTIONS.dimension == 1 else 5
		if newHeight != self.caGrid.height:
			# dimension changed --- create a new CAGrid
			self.caGrid.mainFrame.grid_remove()
			self.caGrid = CAGrid(self, SETTINGS.width / 2, SETTINGS.height / 10 if OPTIONS.dimension == 1 else SETTINGS.height / 2)
			self.caGrid.grid(row = 2, padx = 5, pady = 5, columnspan = 3)
			self.caGrid.draw(5, newHeight)
			self.caGrid.toggle([(0, 2)])
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
		ruleGrid = CAGrid(newRuleFrame, SETTINGS.width / 2, SETTINGS.height / 10 if OPTIONS.dimension == 1 else SETTINGS.height / 2)
		ruleGrid.draw(5, 1 if OPTIONS.dimension == 1 else 5)
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
				# grid.configure(height = SETTINGS.height / 10 if OPTIONS.dimension == 1 else SETTINGS.height / 2)
				grid.draw(5, newHeight)
		return True

	def setOptions(self):
		'''Sets  the global options'''
		rules = []
		for rule_grid in self.rules.values():
			rule_list = rule_grid.ca_grid.clicked(False)
			if rule_list:
				rules.append([x[0] - 2 for x in rule_list])
		setOption("rules", rules)
		return True

class DrawScreen(Screen):
	'''Displays the Cellular Automata'''
	current = DRAW
	prev = OPTIONS_RULES
	next = MAIN_PROGRAM

	def createInterface(self):
		'''Creates the main CA interface'''
		self.ca_grid = CAGrid(self, SETTINGS.width, SETTINGS.height, activeColor = "red")
		self.ca_grid.setBackground("white")
		self.graph = graph.GraphWin(self, width = SETTINGS.width, height = SETTINGS.height, autoflush = False)
		self.graph.setBackground("white")
		self.ca_grid.draw(OPTIONS.width, OPTIONS.height, False)

		self.drawing, self.needUpdate = False, True
		self.drawButton = tk.Button(self, text = "Draw", command = self.draw)
		self.addNavigator()

		self.gridWidgets([
			self.ca_grid,
			(self.prevButton, self.drawButton, self.nextButton),
			], padx = 5, pady = 5)

	def onload(self, force = False):
		'''Draws the Cellular Automata screen'''
		# add the latest rules to the history database
		if OPTIONS.rules and OPTIONS.interest:
			DATABASE.insert("history", dimension = OPTIONS.dimension, interest = OPTIONS.interest,
				rule = str(OPTIONS.rules))

	def draw(self):
		''"Draws the Cellular Automata"""
		start = self.ca_grid.clicked(False)
		self.ca_grid.mainFrame.grid_remove()
		self.graph.grid(row = 1, padx = 5, pady = 5, columnspan = 4)
		if OPTIONS.dimension == 1:
			self.drawButton.configure(state = tk.DISABLED)
			cellspace = [0] * OPTIONS.width
			self.graph.setCoords(0, 0, OPTIONS.width, OPTIONS.height)
			for x, y in filter(lambda cell: cell[1] <= 1, start):
				try:
					cellspace[x - 40] = 1
					print x
				except IndexError:
					pass
			rulesets = [{'on': rule, 'off': list(set(xrange(-2, 3)) - set(rule))} for rule in OPTIONS.rules]
			ymin, ymax = 0, OPTIONS.height
			print rulesets, OPTIONS.interest
			while True:
				for y in reversed(xrange(ymin, ymax)): # starts from the top of the window and works down
					# erase current row
					r = graph.Rectangle(graph.Point(0, y), graph.Point(SETTINGS.width, y - 1))
					r.setFill("white")
					r.setOutline("white")
					r.draw(self.graph) # not drawing correctly
					for x in xrange(len(cellspace)):
						if cellspace[x] == 1:
							self.graph.plot(x, y, "black")
					cellspace = self.generateCellSpace1D(rulesets, cellspace, True)
					self.graph.update() # window updates after every row

	def generateCellSpace1D(self, rulesets, state, wrap = False):
		'''input: rulesets is a list of lists of integers
		(i.e. [[-1,0,1], [-1,1], [0]]), where 0 is the
		cell of interest, and state is a 1D array of
		the current state of all cells in the cell space
		wrap is a boolean that states whether or not the
		cell space is a wrapping cell space'''
		wrap_amount = len(state)
		newstate = [0] * wrap_amount
		if wrap:
			for cell in xrange(wrap_amount):
				for ruleset in rulesets:
					# if the rule matches (on cells are on and rest are off), then turn the cell of interest on
					if (all(state[(cell + index) % wrap_amount] == 1 for index in ruleset['on'])
						and all(state[(cell + index) % wrap_amount] == 0 for index in ruleset['off'])):
							newstate[(cell + OPTIONS.interest) % wrap_amount] = 1
							break
		else:
			for cell in xrange(wrap_amount):
				for ruleset in rulesets:
					if (all(0 < cell + index < wrap_amount - 1 and state[(cell + index)] == 1 for index in ruleset['on'])
						and all(0 < cell + index < wrap_amount - 1 and state[(cell + index)] == 0 for index in ruleset['off'])):
							newstate[cell + OPTIONS.interest] = 1
							break			
		return newstate
