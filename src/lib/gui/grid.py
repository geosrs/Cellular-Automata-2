# gui.grid.py
# Rushy Panchal and George Georges
# Cellular Automata Project
# Contains the CAGrid and CACell classes

### Imports

import tk.ttkExtra as tk

### Main classes

class CAGrid(tk.BaseCustomWidget):
	'''Creates a CAGrid object'''
	def __init__(self, master, width, height, **options):
		self.master = master
		self.mainFrame = tk.Frame(self.master)
		self.width, self.height = width, height
		self.activeColor = tk.dictGet(options, "activeColor", "black")
		self.hoverColor = tk.dictGet(options, "hoverColor", "blue")
		self.outlineColor = tk.dictGet(options, "outlineColor", "black")
		self.graph = tk.Canvas(self.mainFrame, width = self.width, height = self.height, **options)
		self.graph.grid()
		self.graph.bind("<Button-1>", lambda event: self.click(event.x, event.y))
		self.graph.bind("<B1-Motion>", lambda event: self.click(event.x, event.y))
		self.setBackground("white")
		self.cells = {}
		self.edit = True
	
	def configure(self, *args, **kwargs):
		'''Configures the CAGrid'''
		return self.graph.configure(*args, **kwargs)

	def setBackground(self, color):
		'''Sets the background color of the CAGrid'''
		self.background = color
		self.graph.configure(background = color)
		
	def coordinateToPoint(self, x, y):
		'''Transforms the (x, y) board coordinate into a linear point'''
		return (self.width_cells * (y + 1) + x) - 1
	
	def pointToCoordinate(self, n):
		'''Transforms the linear point into an (x, y) board coordinate'''
		n += 1
		x = n % self.width_cells
		y = n // self.width_cells + 1
		if x == 0:
			x = self.width_cells
			y -= 1
		return (x, y)
		
	def toggle(self, cells):
		'''Toggles the given cells on or off'''
		if isinstance(cells[0], (list, tuple, set)):
			for x, y in cells:
				self.click(x, y)
		else:
			for cell in cells:
				self.click(cell, 0)
		
	def draw(self, width, height, drawAll = True):
		'''Draws the CAGrid'''
		w, h = self.width / width, self.height / height
		self.width_cells, self.height_cells = width, height
		if w < 3 or h< 3:
			self.outlineColor = self.background
		if drawAll:
			def drawCells(x):
				for y in xrange(height):
					self.graph.create_rectangle(x * w, y * h, (x + 1) * w, (y + 1) * h, outline = self.outlineColor)
				self.graph.update_idletasks()
				if x < width:
					self.graph.after(1, lambda: drawCells(x + 1))
			drawCells(0)
				
	def click(self, x, y, state = None):
		'''Simulates a click event on a cell'''
		if self.edit:
			w, h = self.width / self.width_cells, self.height / self.height_cells
			x, y = (x - (x % w)) / w, (y - (y % h)) / h
			current = self.cells.get((x, y), self.background)
			on = current == self.background
			if not state is None:
				on = state
			new = self.activeColor if on else self.background
			self.graph.create_rectangle(x * w, y * h, (x + 1) * w, (y + 1) * h, fill = new, outline = new if on else self.outlineColor)
			self.cells[(x, y)] = new
		
	def clickCell(self, x, y, state = None):
		'''Clicks a specific cell'''
		if self.edit:
			self.click(x * self.width / self.width_cells, y * self.height / self.height_cells, state)

	def clicked(self, convert = True):
		'''Returns which elements have been clicked'''
		# get the coordinates of only the clicked cells
		points = filter(lambda item: self.cells[item] == self.activeColor, self.cells.keys())
		if convert:
			return map(lambda cell: self.coordinateToPoint(cell[0], cell[1]), points)
		else:
			return points
