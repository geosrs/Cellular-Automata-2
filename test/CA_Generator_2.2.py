# George Georges
# Cellular Automata Example
# Cell Space: 1D/2D
from graphics import *

WIDTH = 401
HEIGHT = 401
INTEREST = 0
WRAP = True
TOTALISTIC = True
DIMENSION = 2
#RULES = [[[1,2]], [[0,0]], [[1,-1]], [[5, 4]], [[3, 1], [0,0]]]
#RULES = [[-1], [0], [1]]
RULES = [[1], [2]]
#CELLSPACE = [0] * WIDTH
CELLSPACE = [[0] * WIDTH for i in range(HEIGHT)]
#CELLSPACE[int(WIDTH/2)] = 1 # set the center cell to 1
CELLSPACE[int(WIDTH/2)][int(HEIGHT/2)] = 1

def main():
	CA = GraphWin(None, WIDTH, HEIGHT, autoflush = False) # this is to run with Tkinter
	CA.grid()
	generateCA(CA, CELLSPACE, RULES, WIDTH, HEIGHT, DIMENSION, WRAP, TOTALISTIC)

def generateCA(window, cellspace, rules, width, height, dimension, wrap = True, totalistic = False):
	'''Generates the CA on the window
	  Note: if totalistic = True, rules is a 
	  list of integers that dictate the number
	  of on cells in the neighborhood 
	  (including the cell of interest)
	  1D neighborhood will be adjacent
	  cells plus cell of interest only; 2D 
	  neighborhood will be eight adjacent
	  plus cell of interest only'''
	window.setBackground("white") # white background saves computational power (off cells are white and do not need to be plotted)
	window.setCoords(0, 0, width, height)
	if dimension == 1 and totalistic == False:
			ymin, ymax = 0, width
			minindex, maxindex = rules[0][0], rules[0][0]
			for rule in rules: # find the minimum and maximum of all the rules
					for rule_item in rule:
							if rule_item > maxindex:
									maxindex = rule_item
							if rule_item < minindex:
									minindex = rule_item
				# calculate the sets of rules
			rulesets = [{'on': rule, 'off': list(set(range(minindex, maxindex+1)) - set(rule))} for rule in rules]
			for y in reversed(range(ymin, ymax)): # starts from the top of the window and works down
					# print(cellspace)
					for x in range(len(cellspace)):
							if cellspace[x] == 1: # only print the "on" cells
									window.plot(x, y, "black")
					cellspace = generateCellSpace1D(rulesets, cellspace, wrap, False)
					window.update() # window updates after every row
	elif dimension == 2 and totalistic == False:
			ymin, ymax = 0, height
			xmin, xmax = 0, width
			# calculate the sets of rules, neighborhood restricted to 5x5 grid
			# all_row_cells = set(range(-2, 3))
			rulesets = [{'on': rule} for rule in rules]
			for i in range(10):
				for y in reversed(range(ymin, ymax)):
					for x in range(xmin, xmax):
						if cellspace[x][y] == 1: # only print the "on" cells
							window.plot(x, y, "black")
				cellspace = generateCellSpace2D(rulesets, cellspace, wrap, False)
				window.update()
	elif dimension == 1 and totalistic == True:
			ymin, ymax = 0, width
			rulesets = [{'on': rule, 'off': [list(set(range(0, 3)) - set(rule))]} for rule in rules]
			for y in reversed(range(ymin, ymax)):
				for x in range(len(cellspace)):
					if cellspace[x] == 1:
						window.plot(x, y, "black")
				cellspace = generateCellSpace1D(rulesets, cellspace, wrap, True)
				window.update()
	elif dimension == 2 and totalistic == True:
			ymin, ymax = 0, height
			xmin, xmax  = 0, width
			rulesets = [{'on': rule, 'off': [list(set(range(0, 10)) - set(rule))]} for rule in rules]
			for i in range(100):
				for y in reversed(range(ymin, ymax)):
					for x in range(xmin, xmax):
						if cellspace[x][y] == 1:
							window.plot(x, y, "black")
				cellspace = generateCellSpace2D(rulesets, cellspace, wrap, True)
				window.update()

def generateCellSpace2D(rulesets, state, wrap = False, totalistic = False):
	'''input: rulesets is a list of lists of coordinates
	(i.e. [[[-1,0],[1,2]], [[-1,1]], [[0,2],[-1,2],[-2,0]]]),
	where [0,0] is the cell of interest, and state is a 2D array of
	the current state of all cells in the cell space
	wrap is a boolean that states whether or not the
	cell space is a wrapping cell space'''
	wrap_amount = len(state)
	newstate = [[0] * wrap_amount for i in range(wrap_amount)]
	if wrap:
		if totalistic == False:
			for cell in range(wrap_amount):
				for row in range(wrap_amount):
					for ruleset in rulesets:
							#  if the rule matches (on cells are on and rest are off), then turn the cell of interest on
						if all(state[(cell + index[0]) % wrap_amount][(row + index[1]) % wrap_amount] == 1 for index in ruleset['on']): #and all(state[(cell + index[0]) % wrap_amount][(row + index[1]) % wrap_amount] == 0 for index in ruleset['off']):
							newstate[(cell % wrap_amount)][(row % wrap_amount)] = 1
							break
		else: # wrap_amount has to be different for BOTH width and height
			for cell in range(wrap_amount):
				for row in range(wrap_amount):
					count = 0
					for y in range(-1, 2):
						for x in range(-1, 2):
							if state[(cell + x) % wrap_amount][(row + y) % wrap_amount] == 1:
								count += 1
					for rule in rulesets:
						rule = rule['on'][0]
						if int(rule) == count:
							newstate[(cell % wrap_amount)][(row % wrap_amount)] = 1
							break
	else:
		if totalistic == False:
			for cell in range(wrap_amount):
				for row in range(wrap_amount):
					if (all(0 < cell + index[0] < wrap_amount - 1 and 0 < row + index[1] < wrap_amount - 1 and state[(cell + index[0])][(row + index[1])] == 1 for index in ruleset['on'])
						and (all(0 < cell + index[0] < wrap_amount - 1 and 0 < row + index[1] < wrap_amount - 1 and state[(cell + index[0])][(row + index[1])] == 0 for index in ruleset['off']))):
							newstate[cell][row] = 1
							break
		else:
			for cell in range(wrap_amount):
				for row in range(wrap_amount):
					count = 0
					for y in range(-1, 2):
						for x in range(-1, 2):
							if ((0 < cell + x < wrap_amount - 1) and (0 < row + y < wrap_amount - 1) and (state[(cell + x)][(row + y)] == 1)):
								count += 1
					for rule in rulesets:
						rule = rule['on'][0]
						if int(rule) == count:
							newstate[cell][row] = 1
	return newstate
									

def generateCellSpace1D(rulesets, state, wrap = False, totalistic = False):
	'''input: rulesets is a list of lists of integers
	(i.e. [[-1,0,1], [-1,1], [0]]), where 0 is the
	cell of interest, and state is a 1D array of
	the current state of all cells in the cell space
	wrap is a boolean that states whether or not the
	cell space is a wrapping cell space'''
	wrap_amount = len(state)
	newstate = [0] * wrap_amount
	if wrap:
		if totalistic == False:
			for cell in range(wrap_amount):
				for ruleset in rulesets:
					# if the rule matches (on cells are on and rest are off), then turn the cell of interest on
					if (all(state[(cell + index) % wrap_amount] == 1 for index in ruleset['on'])
						and all(state[(cell + index) % wrap_amount] == 0 for index in ruleset['off'])):
							newstate[(cell + INTEREST) % wrap_amount] = 1
							break
		else:
			for cell in range(wrap_amount):
				count = 0
				for x in range(-1, 2):
					if state[(cell + x) % wrap_amount] == 1:
						count += 1
				for rule in rulesets:
					rule = rule['on'][0]
					if int(rule) == count:
						newstate[(cell + INTEREST) % wrap_amount] = 1
						break
	else:
		if totalistic == False:
			for cell in range(wrap_amount):
				for ruleset in rulesets:
					if (all(0 < cell + index < wrap_amount - 1 and state[(cell + index)] == 1 for index in ruleset['on'])
						and all(0 < cell + index < wrap_amount - 1 and state[(cell + index)] == 0 for index in ruleset['off'])):
							newstate[cell + INTEREST] = 1
							break
		else:
			for cell in range(wrap_amount):
				count = 0
				for x in range(-1, 2):
					if (0 < cell + x < wrap_amount - 1 and state[(cell + x)] == 1):
						count += 1
				for rule in rulesets:
					rule = rule['on'][0]
					if int(rule) == count:
						newstate[(cell + INTEREST) % wrap_amount] = 1
						break
	return newstate

if __name__ == "__main__":
	main()
