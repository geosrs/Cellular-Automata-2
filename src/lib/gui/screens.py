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

from ast import literal_eval
from datetime import datetime

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
		try:
			frame = self.rules[rule]
		except KeyError:
			return False
		self.current.grid_forget()
		frame.grid(row = 2, pady = 5, columnspan = 3)
		self.current = frame
		return True

	def addRule(self, number, frame):
		'''Adds a rule to the display'''
		self.rules[number] = frame
		ruleButton = tk.Button(self.buttonFrame, text = number, command = lambda: self.click(number), width = 5)
		self.click(number)
		column = number % self.width
		if column == 0:
			column = self.width
		# add the button to the grid of buttons
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

		self.photo = tk.PhotoImage(master = self, file = IMAGE_PATHS["logo.gif"])
		self.homeImage = tk.Label(self, image = self.photo)
		self.homeImage.image = self.photo

		self.mainLabel.place(anchor = tk.N, relx = 0.5, y = 0)

		self.gridWidgets([
			self.homeImage,
			self.startButton,
			self.historyButton,
			self.settingsButton,
			self.aboutButton,
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
		self.helpLabel = tk.Label(self, text = HELP.history.text, style = "Help.TLabel")
		self.searchLabel = tk.Label(self, text = "Search")
		self.searchEntry = tk.Entry(self, justify = tk.CENTER, command = self.filter)
		self.historyFrame = tk.Frame(self)
		self.clearButton = tk.Button(self, text = "Clear", command = self.clear, style = "Quit.TButton")
		self.prevRowsButton = tk.Button(self, text = "Previous", command = lambda: self.next(-10))
		self.nextRowsButton = tk.Button(self, text = "Next", command = lambda: self.next(10))
		self.addNavigator(prev = "Home")
		self.current_rows = (0, 10)

		self.gridWidgets([
			self.mainLabel,
			self.helpLabel,
			# (self.searchLabel, self.searchEntry),
			self.historyFrame,
			self.clearButton,
			(self.prevRowsButton, self.nextRowsButton),
			self.prevButton,
			], padx = 5, pady = 5)

	def filter(self):
		'''Filters the history'''
		pass # not implemented yet

	def clear(self):
		"""Clears all the history"""
		self.db.delete("history", where = "1 = 1")
		self.displayRows(*self.current_rows)

	def onload(self):
		'''Loads the latest rows'''
		self.displayRows(*self.current_rows) # show the ten most recent rules
		self.nextRowsButton.configure(state = tk.NORMAL)
		self.prevRowsButton.configure(state = tk.NORMAL)

	def next(self, delta = 10):
		'''Displays the next/previous "delta" rows'''
		total_rows_cursor = self.db.select("row_count", where = "1 = 1")
		num_rows = self.db.fetch(total_rows_cursor)[0]["amount"]
		new_rows = map(lambda x: x + delta, self.current_rows)

		if new_rows[0] < num_rows and new_rows[1] <= num_rows:
			self.displayRows(*new_rows)
		self.prevRowsButton.configure(state = tk.DISABLED if new_rows[0] - abs(delta) < 0 else tk.NORMAL)	
		self.nextRowsButton.configure(state = tk.DISABLED if new_rows[1] + abs(delta) > num_rows else tk.NORMAL)

	def displayRows(self, start = 0, end = 10):
		'''Displays the rows from "start" to "end"'''
		# fetch the rows
		self.current_rows = (start, end)
		row_cursor = self.db.query(self.baseQuery.format(limit = end - start, offset = start))
		rows = self.db.fetch(row_cursor)
		# remove the previous rows
		for widget in self.displayed:
			widget.grid_forget()
		# show the new rows
		for row_number, row in enumerate(rows, 1):
			image_rule, rule, rule_number = row["image"], row["rule"], row["rule_number"]
			ruleFrame = tk.Frame(self.historyFrame)
			numberLabel = tk.Button(ruleFrame, text = "{n})".format(n = rule_number), command = tk.createLambda(self.openRule, rule_number))
			ruleLabel = tk.Label(ruleFrame, text = image_rule if image_rule else rule)
			numberLabel.pack(side = "left")
			ruleLabel.pack(side = "right")
			ruleFrame.grid(row = row_number)
			self.displayed.append(ruleFrame)

	def openRule(self, number):
		'''Opens the "number" rule'''
		# get that row's data
		data = self.db.fetch(self.db.select("history", equal = {"rule_number": number}))[0]
		dimension = data["dimension"]
		rules = literal_eval(data["rule"])
		rowWindow = tk.Toplevel(self.master)
		data_time = datetime.strptime(data["time"], "%Y-%m-%d %H:%M:%S")
		time_created = data_time.strftime("%B %d, %Y at %H:%M:%S") # format the time to display

		# display the associated data
		ruleNumber = tk.Label(rowWindow, text = "Automaton {n}".format(n = number), style = "Subheader.TLabel")
		timeDesc = tk.Label(rowWindow, text = "Time Created", style = "OptionHeader.TLabel")
		timeLabel = tk.Label(rowWindow, text = time_created)
		dimensionDesc = tk.Label(rowWindow, text = "Dimensions", style = "OptionHeader.TLabel")
		dimensionLabel = tk.Label(rowWindow, text = dimension)
		interestDesc = tk.Label(rowWindow, text = "Cell of Interest", style = "OptionHeader.TLabel")
		interestLabel = tk.Label(rowWindow, text = data["interest"])
		ruleFrame = RuleDisplay(rowWindow, 5)

		# create the rule displays for the automata
		for n, rule in enumerate(rules, 1):
			newRuleFrame = tk.Frame(ruleFrame)
			newRuleFrame.number = n
			ruleLabel = tk.Label(newRuleFrame, text = "Rule {n}".format(n = n), style = "OptionHeader.TLabel")
			ruleGrid = CAGrid(newRuleFrame, SETTINGS.width / 2, SETTINGS.height / 10 if dimension == 1 else SETTINGS.height / 2)
			ruleGrid.draw(5, 1 if dimension == 1 else 5)
			if dimension == 1: # show the current cells
				for x in rule:
					ruleGrid.clickCell(x + 2, 0)
			else:
				for x, y in rule:
					ruleGrid.clickCell(x + 2, y + 2)
			ruleGrid.edit = False
			newRuleFrame.ca_grid = ruleGrid

			newRuleFrame.gridWidgets([
				ruleLabel,
				ruleGrid,
				], pady = 5)
			ruleFrame.addRule(n, newRuleFrame)

		ruleFrame.click(1) # select the first rule to show as default

		def deleteItem():
			self.db.delete("history", equal = {"rule_number": number})
			rowWindow.close()
			self.displayRows(*self.current_rows)

		delButton = tk.Button(rowWindow, text = "Delete", command = deleteItem, style = "Quit.TButton")
		closeButton = tk.Button(rowWindow, text = "Close", command = rowWindow.close)

		rowWindow.gridWidgets([
			ruleNumber,
			(timeDesc, timeLabel),
			(dimensionDesc, dimensionLabel),
			(interestDesc, interestLabel),
			ruleFrame,
			delButton,
			closeButton
			], padx = 5, pady = 5)

		rowWindow.center()
		rowWindow.mainloop()

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
		self.helpLabel = tk.Label(self, text = HELP.settings.text, style = "Help.TLabel")
		self.widthLabel = tk.Label(self, text = "Width", style = "OptionHeader.TLabel")
		self.widthSlider = tk.LabelledScale(self, type = int, from_ = 1, to = tk.SCREENDIM["width"],
			length = 250, default = SETTINGS.width, step = 2, edit = True)
		self.heightLabel = tk.Label(self, text = "Height", style = "OptionHeader.TLabel")
		self.heightSlider = tk.LabelledScale(self, type = int, from_ = 1, to = tk.SCREENDIM["height"],
			length = 250, default = SETTINGS.height, step = 2, edit = True)
		self.fontLabel = tk.Label(self, text = "Program Font", style = "OptionHeader.TLabel")
		self.fontEntry = tk.Entry(self, width = 20, justify = tk.CENTER)
		self.fontEntry.insert(tk.END, SETTINGS.font)
		self.sizeLabel = tk.Label(self, text = "Font Size", style = "OptionHeader.TLabel")
		self.sizeSlider = tk.LabelledScale(self, type = int, from_ = 8, to = 24, length = 250, default = SETTINGS.size, step = 1, edit = True)
		self.saveButton = tk.Button(self, text = "Apply", command = self.saveSettings)
		self.defaultButton = tk.Button(self, text = "Reset to Default", command = self.loadDefaults, style = "Quit.TButton")
		self.addNavigator()

		self.gridWidgets([
			self.mainLabel,
			self.helpLabel,
			self.fullscreenOption,
			(self.fontLabel, self.fontEntry),
			(self.sizeLabel, self.sizeSlider),
			(self.widthLabel, self.widthSlider),
			(self.heightLabel, self.heightSlider),
			self.saveButton,
			self.defaultButton,
			self.prevButton,
			], padx = 5, pady = 5)

	def saveSettings(self, get = True):
		'''Saves the settings'''
		if get: # need to get the new settings
			SETTINGS.fullscreen = bool(self.fullscreenVar.get())
			SETTINGS.font = self.fontEntry.get()
			SETTINGS.size = self.sizeSlider.get()
			SETTINGS.width = self.widthSlider.get()
			SETTINGS.height = self.heightSlider.get()

		# apply any changes
		if SETTINGS.fullscreen:
			self.master.geometry("+0+0")
			self.master.fullscreen(False)
		else:
			self.master.overrideredirect(0)
			self.master.geometry("{w}x{h}".format(w = int(tk.SCREENDIM['w'] * 0.8), h = int(tk.SCREENDIM['h'] * 0.8)))
			self.master.center()
		initializeStyles(self.master, SETTINGS.size) # style the new fonts

		# save the settings and reopen the window
		saveSettings(SETTINGS)
		self.createInterface()

	def loadDefaults(self):
		'''Loads the default settings'''
		SETTINGS.update(DEFAULT_SETTINGS)
		self.saveSettings(False)

### Cellular Automata-related screens
	
class CAScreen(Screen):
	'''Houses the entire Cellular Automata interface'''
	current = MAIN_PROGRAM
	prev = START
	next = OPTIONS_SPACE

	def createInterface(self):
		'''Creates the main interface for the CA window'''
		self.homeText = tk.Label(self, text = "Welcome to {name}!".format(name = NAME), style = "Subheader.TLabel")
		self.photo = tk.PhotoImage(master = self, file = IMAGE_PATHS["ca_label.gif"])
		self.homeImage = tk.Label(self, image = self.photo)
		self.homeImage.image = self.photo
		self.addNavigator("Next", "Home")

		self.gridWidgets([
			self.homeText,
			self.homeImage,
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
		self.helpLabel = tk.Label(self, text = HELP.cellspace.text, style = "Help.TLabel")
		self.dimensionVar = tk.IntVar(self)
		self.dimensionVar.set(OPTIONS.dimension)
		self.wrapVar = tk.IntVar(self)
		self.wrapVar.set(OPTIONS.wrap)

		self.dim1D = tk.Radiobutton(self, text = "1 Dimensional", value = 1,
			variable = self.dimensionVar)
		self.dim2D = tk.Radiobutton(self, text = "2 Dimensional", value = 2,
			variable = self.dimensionVar)

		self.wrapOption = tk.Checkbutton(self, text = "Wrap", variable = self.wrapVar)

		self.addNavigator()

		self.gridWidgets([
			self.mainLabel,
			self.helpLabel,
			(self.dim1D, self.dim2D),
			self.wrapOption,
			(self.prevButton, self.nextButton)
			], pady = 5)

	def setOptions(self, again = False):
		'''Sets the global options'''
		setOption("dimension", self.dimensionVar.get())
		setOption("wrap", bool(self.wrapVar.get()))
		return True

class Options_InterestScreen(Screen):
	'''Allows the user to select a cell of interest'''
	current = OPTIONS_INTEREST
	prev = OPTIONS_SPACE
	next = OPTIONS_RULES

	def createInterface(self):
		'''Creates the Cell of Interest interface'''
		self.mainLabel = tk.Label(self, text = "Cell of Interest", style = "Subheader.TLabel")
		self.helpLabel = tk.Label(self, text = HELP.interest.text, style = "Help.TLabel")
		self.caGrid = CAGrid(self, SETTINGS.width / 2, SETTINGS.height / 10 if OPTIONS.dimension == 1 else SETTINGS.height / 2)
		self.caGrid.draw(5, 1 if OPTIONS.dimension == 1 else 5)
		self.caGrid.toggle([0, 2]) # toggle the first cell as default
		self.addNavigator()

		self.gridWidgets([
			self.mainLabel,
			self.helpLabel,
			self.caGrid,
			(self.prevButton, self.nextButton),
			], pady = 5)

	def setOptions(self):
		'''Sets the global options'''
		clicked =  self.caGrid.clicked() if OPTIONS.dimension == 1 else self.caGrid.clicked(False)
		if clicked:
			clicked = clicked[0]
		shift = -6 if OPTIONS.dimension == 1 else -2
		setOption("interest", (clicked + shift if OPTIONS.dimension == 1 else map(lambda x: x + shift, clicked)) if clicked else OPTIONS.interest)
		return True

	def onload(self):
		'''Called when the screen is loaded'''
		newHeight = 1 if OPTIONS.dimension == 1 else 5
		if newHeight != self.caGrid.height:
			# dimension changed --- create a new CAGrid
			self.caGrid.mainFrame.grid_remove()
			self.caGrid = CAGrid(self, SETTINGS.width / 2, SETTINGS.height / 10 if OPTIONS.dimension == 1 else SETTINGS.height / 2)
			self.caGrid.grid(row = 3, padx = 5, pady = 5, columnspan = 3)
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
		self.helpLabel = tk.Label(self, text = HELP.rules.text, style = "Help.TLabel")
		self.ruleFrame = RuleDisplay(self, 5)
		self.addRuleButton = tk.Button(self, text = "Add Rule", command = self.addRule)
		self.addNavigator()

		self.gridWidgets([
			self.mainLabel,
			self.helpLabel,
			self.ruleFrame,
			self.addRuleButton,
			(self.prevButton, self.nextButton),
			], pady = 5)

	def addRule(self):
		'''Adds a rule to the interface'''
		# create a new rule frame
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
		for rule_grid in self.rules.values(): # add the rules to the global options
			rule_list = rule_grid.ca_grid.clicked(False)
			if rule_list:
				rules.append([x[0] - 2 for x in rule_list] if OPTIONS.dimension == 1 else [(x - 2, y - 2) for x, y in rule_list])
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
		self.graph = graph.GraphWin(self, width = SETTINGS.width, height = SETTINGS.height, autoflush = False)
		self.graph.setBackground("white")
		self.ca_grid.setBackground("white")
		self.ca_grid.draw(OPTIONS.width, OPTIONS.height, False)

		self.mainLabel = tk.Label(self, text = "Automata", style = "Subheader.TLabel")
		self.examplesFrame = tk.Frame(self)
		self.exampleLabel = tk.Label(self, text = "Examples", style = "OptionHeader.TLabel")
		self.ruleFrame = RuleDisplay(self, 5)
		self.ruleLabel = tk.Label(self, text = "Rules", style = "OptionHeader.TLabel")

		self.drawing = False
		self.drawButton = tk.Button(self, text = "Draw", command = self.draw)
		self.addNavigator()

		self.gridWidgets([
			(self.exampleLabel, self.mainLabel, self.ruleLabel),
			(None, self.graph, self.ruleFrame),
			(self.prevButton, self.drawButton, self.nextButton),
			], padx = 5, pady = 5)

		self.graph.grid_remove()
		self.ca_grid.grid(row = 2, column = 2, padx = 5, pady = 5)

	def onload(self, force = False):
		'''Draws the Cellular Automata screen'''
		# add the latest rules to the history database
		if OPTIONS.rules:
			DATABASE.insert("history", dimension = OPTIONS.dimension, interest = str(OPTIONS.interest),
				rule = str(OPTIONS.rules))
		if self.graph.getHeight() != SETTINGS.height or self.graph.getWidth() != SETTINGS.width:
			# width or height settings changed
			self.graph.configure(width = SETTINGS.width, height = SETTINGS.height)
			self.ca_grid.configure(width = SETTINGS.width, height = SETTINGS.height)
		# show the current rules on the side
		for n, frame in self.ruleFrame.rules.items(): # remove the current frames
			frame.grid_forget()
			del self.ruleFrame.rules[n]
		for n, rule in enumerate(OPTIONS.rules, 1):
			newRuleFrame = tk.Frame(self.ruleFrame)
			newRuleFrame.number = n
			ruleLabel = tk.Label(newRuleFrame, text = "Rule {n}".format(n = n), style = "OptionHeader.TLabel")
			ruleGrid = CAGrid(newRuleFrame, SETTINGS.width / 2, SETTINGS.height / 10 if OPTIONS.dimension == 1 else SETTINGS.height / 2)
			ruleGrid.draw(5, 1 if OPTIONS.dimension == 1 else 5)
			# show the current cells
			if OPTIONS.dimension == 1:
				for x in rule:
					ruleGrid.clickCell(x + 2, 0)
			else:
				for x, y in rule:
					ruleGrid.clickCell(x + 2, y + 2)
			ruleGrid.edit = False
			newRuleFrame.ca_grid = ruleGrid

			newRuleFrame.gridWidgets([
				ruleLabel,
				ruleGrid,
				], pady = 5)

			self.ruleFrame.addRule(n, newRuleFrame)
		self.ruleFrame.click(1)

	def draw(self):
		''"Draws the Cellular Automata"""
		self.drawing = not self.drawing
		start = self.ca_grid.clicked(False)
		self.ca_grid.mainFrame.grid_remove()
		self.graph.grid()
		self.drawButton.configure(text = "Pause" if self.drawing else "Draw")
		if not self.drawing: # exit the program if not drawing
			return False
		self.graph.setCoords(0, 0, OPTIONS.width, OPTIONS.height)
		if OPTIONS.dimension == 1:
			try:
				self.cellspace
			except AttributeError:
				self.cellspace = [0] * OPTIONS.width
				for x, y in filter(lambda cell: cell[1] <= 1, start): # set the initial cellstate
					try:
						self.cellspace[x - SETTINGS.width / 10] = 1
					except IndexError:
						pass
			try:
				self.start_row
			except AttributeError:
				self.start_row = OPTIONS.height
			# generate the list of rulesets
			all_rule_ranges = set(xrange(-2, 3))
			rulesets = [{'on': rule, 'off': list(all_rule_ranges - set(rule))} for rule in OPTIONS.rules]
			ymin, ymax = 0, OPTIONS.height
			while self.drawing:
				# keeps drawing the cellular automata
				for y in reversed(xrange(ymin, self.start_row)): # starts from the top of the window and works down
					r = graph.Rectangle(graph.Point(0, y), graph.Point(SETTINGS.width, y - 1))
					r.setFill("white")
					r.setOutline("white")
					r.draw(self.graph) # erase the current row before drawing
					for x in xrange(len(self.cellspace)):
						# plot the "on" cells
						if self.cellspace[x] == 1:
							self.graph.plot(x, y, "black")
					self.cellspace = self.generateCellspace1D(rulesets, self.cellspace, OPTIONS.wrap)
					self.graph.update() # window updates after every row
					if not self.drawing:
						self.start_row = y # pause the drawing, and save the current row
						break
				if self.drawing:
					self.start_row = ymax # reset the current row
		else: # need to draw 2D --- only need lengths of the rules, not the rules themselves
			try:
				self.cellspace
			except AttributeError:
				self.cellspace = [[0] * SETTINGS.width for i in xrange(SETTINGS.height)]
				for x, y in start: # set the initial cellstate
					self.cellspace[x - SETTINGS.width / 10][-y] = 1
			# generate the rulesets
			all_rule_ranges = set(xrange(0, 10))
			rulesets = [{'on': [len(rule)], 'off': [list(all_rule_ranges - set(rule))]} for rule in OPTIONS.rules]
			ymin, ymax = 0, OPTIONS.height
			xmin, xmax  = 0, OPTIONS.width
			while self.drawing:
				for y in reversed(xrange(ymin, ymax)):
					for x in xrange(xmin, xmax):
						if self.cellspace[x][y] == 1:
							self.graph.plot(x, y, "black")
				self.cellspace = self.generateCellspace2D(rulesets, self.cellspace, OPTIONS.wrap)
				self.graph.update()

	def generateCellspace1D(self, rulesets, state, wrap = True):
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

	def generateCellspace2D(self, rulesets, state, wrap = True):
		'''input: rulesets is a list of lists of coordinates
		(i.e. [[[-1,0],[1,2]], [[-1,1]], [[0,2],[-1,2],[-2,0]]]),
		where [0,0] is the cell of interest, and state is a 2D array of
		the current state of all cells in the cell space
		wrap is a boolean that states whether or not the
		cell space is a wrapping cell space'''
		wrap_x, wrap_y = len(state), len(state[0])
		newstate = [[0] * wrap_y for i in xrange(wrap_x)]
		if wrap:
			for cell in xrange(wrap_x):
				for row in xrange(wrap_y):
					count = 0
					# iterate over the adjacent cells
					for y in xrange(-1, 2):
						for x in xrange(-1, 2):
							# count the number of "on" cells
							if state[(cell + x) % wrap_x - 1][(row + y) % wrap_y - 1] == 1:
								count += 1
					for rule in rulesets:
						rule = rule['on'][0]
						if int(rule) == count:
							newstate[(cell + OPTIONS.interest[0]) % wrap_x][(row + OPTIONS.interest[1]) %wrap_y] = 1
							break
		else:
			for cell in xrange(wrap_x):
				for row in xrange(wrap_y):
					count = 0
					for y in xrange(-1, 2):
						for x in xrange(-1, 2):
							if ((0 < cell + x < wrap_x - 1) and (0 < row + y < wrap_y- 1) and (state[(cell + x)][(row + y)] == 1)):
								count += 1
					for rule in rulesets:
						rule = rule['on'][0]
						if int(rule) == count:
							newstate[cell + x + OPTIONS.interest[0]][row + y + OPTIONS.interest[1]] = 1
		return newstate