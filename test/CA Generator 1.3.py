# George Georges
# Cellular Automata Example
# Cell Space: 1D
from graphics import *

WIDTH = 401
HEIGHT = 401
INTEREST = 2
WRAP = True

RULES = [[-1], [0], [1]]
CELLSPACE = [0] * WIDTH
CELLSPACE[int(WIDTH/ 2)] = 1 # set the center cell to 1

def main():
	CA = GraphWin(None, WIDTH, HEIGHT, autoflush = False) # this is to run with Tkinter
	CA.grid()
	# CA = GraphWin("Cellular Automata", WIDTH, HEIGHT, autoflush = False)
	generateCA(CA, CELLSPACE, RULES, WIDTH, HEIGHT, WRAP)

def generateCA(window, cellspace, rules, width, height, wrap = True):
	'''Generates the CA on the window'''
	window.setBackground("white") # white background saves computational power (off cells are white and do not need to be plotted)
	window.setCoords(0, 0, width, height)
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
		cellspace = generateCellSpace(rulesets, cellspace, wrap)
		window.update() # window updates after every row

def generateCellSpace(rulesets, state, wrap = False):
	'''input: rules is a list of lists of integers
	(i.e. [[-1,0,1], [-1,1], [0]]), where 0 is the
	cell of interest, and state is a 1D array of
	the current state of all cells in the cell space
	wrap is a boolean that states whether or not the
	cell space is a wrapping cell space'''
	wrap_amount = len(state)
	newstate = [0] * wrap_amount
	if wrap:
		for cell in range(wrap_amount):
			for ruleset in rulesets:
				# if the rule matches (on cells are on and rest are off), then turn the cell of interest on
				if (all(state[(cell + index) % wrap_amount] == 1 for index in ruleset['on'])
					and all(state[(cell + index) % wrap_amount] == 0 for index in ruleset['off'])):
						newstate[(cell + INTEREST) % wrap_amount] = 1
						break
	else:
		for cell in range(wrap_amount):
			for ruleset in rulesets:
				if (all(0 < cell + index < wrap_amount - 1 and state[(cell + index)] == 1 for index in ruleset['on'])
					and all(0 < cell + index < wrap_amount - 1 and state[(cell + index)] == 0 for index in ruleset['off'])):
						newstate[cell + INTEREST] = 1
						break			
	return newstate

if __name__ == "__main__":
	main()
