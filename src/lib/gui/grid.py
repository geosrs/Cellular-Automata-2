# gui.grid.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains the CAGrid and CACell classes

### Imports

import tk.ttkExtra as tk
import tk.graphics as graph

### Main classes

class CAGrid(tk.BaseCustomWidget):
	'''Displays a CA grid interface'''
	def __init__(self, master, w, h, **options):
		self.master = master
		self.width, self.height, self.options = w, h, options
		self.mainFrame = tk.Frame(self.master)
		self.activeColor = tk.dictGet(options, "activeColor", "black")
		self.hoverColor = tk.dictGet(options, "hoverColor", "blue")
		self.outlineColor = tk.dictGet(options, "outlineColor", "black")
		options["width"] = options["height"] = tk.dictGet(options, "size", 200)
		self.graph = graph.GraphWin(self.mainFrame, **options)
		self.graph.grid()
		self.draw()
	
	def configure(self, *kw, **kwargs):
		'''Configures the CAGrid'''
		return self.graph.configure(*kw, **kwargs)

	def draw(self, width = None, height = None):
		'''Draws the grid'''
		self.cells = []
		self.graph.clear()
		self.width = width if width else self.width
		self.height = height if height else self.height
		self.graph.setCoords(1, 1, self.width + 1, self.height + 1)
		for x in xrange(1, self.width + 1):
			for y in xrange(1, self.height + 1):
				# create a new clickable cell
				cell = CACell(self.graph, x = x, y = y, active = self.activeColor,
					hover = self.hoverColor, outline = self.outlineColor)
				self.cells.append(cell)
		self.graph.update()

	def clicked(self):
		'''Returns the clicked items'''
		# get the coordinates of only the clicked cells
		return map(lambda cell: (cell.x, cell.y), filter(lambda cell: cell.clicked, self.cells))

class CACell(tk.BaseCustomWidget):
	'''A clickable cell'''
	def __init__(self, master, **options):
		self.master = master
		self.options = options
		self.x, self.y = options.get("x", 0), options.get("y", 0)
		self.activeColor = options.get("active", "black")
		self.hoverColor = options.get("hover", "blue")
		self.outlineColor = options.get("outline", "black")
		self.clicked = True
		self.rectangle = graph.Rectangle(graph.Point(self.x, self.y), graph.Point(self.x + 1, self.y + 1))
		self.rectangle.draw(self.master)
		self.id = self.rectangle.id
		self.master.tag_bind(self.id, "<Button-1>", self.click) # if clicked, call self.click
		# if the user hovers over the cell, change the color
		self.master.tag_bind(self.id, "<Enter>", lambda event: self.hover(True))
		self.master.tag_bind(self.id, "<Leave>", lambda event: self.hover(False))
		self.rectangle.setOutline(self.outlineColor)
		self.click()

	def click(self, event = None):
		'''Simulates a cell click'''
		self.clicked = not self.clicked
		# if the cell is clicked, set it to the active color (becomes the background color otherwise)
		self.color = self.activeColor if self.clicked else self.master.configure("background")[-1]
		self.rectangle.setFill(self.color)

	def hover(self, on):
		'''Simulates a cell hover'''
		color = self.hoverColor if on else self.color
		self.rectangle.setFill(color)
		