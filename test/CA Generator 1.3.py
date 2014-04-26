# George Georges
# Cellular Automata Example
# Cell Space: 1D
from graphics import *

def main():
	root = Tk()
	CA = GraphWin(root, 401, 401, autoflush = False)
	# CA = GraphWin("Cellular Automata", 401, 401, autoflush = False)
	CA.setBackground("white") # white background saves computational power (off cells are white and do not need to be plotted)
	CA.setCoords(0, 0, 400, 400)
	cellspace = []
	rules = [[-1], [0], [1]]
	for i in range(401):
		if i == 200:
			cellspace.append(1) # center cell is on
		else:
			cellspace.append(0) # rest of the cells are off
	generateCA(CA, cellspace, rules)

def generateCA(window, cellspace, rules, wrap = True):
	ymax = 400
	ymin = 0
	step = 1
	for y in reversed(range(ymin, ymax)): # starts from the top of the window and works down
		 #print(cellspace)
		 for x in range(len(cellspace)):
			if cellspace[x] == 1:
			 window.plot(x, y, "black")
		 cellspace = generateCellSpace(rules, cellspace)
		 window.update() # window updates after every row

def generateCellSpace(rules, state, wrap = False):
	'''input: rules is a list of lists of integers
	(i.e. [[-1,0,1], [-1,1], [0]]), where 0 is the
	cell of interest, and state is a 1D array of
	the current state of all cells in the cell space
	wrap is a boolean that states whether or not the
	cell space is a wrapping cell space'''
	newstate = state[:]
	indexlist = []
	for a in range(len(rules)):
		 for b in range(len(rules[a])):
			 indexlist.append(rules[a][b])
	minindex = min(indexlist)
	maxindex = max(indexlist)
	for cell in range(len(state)):
		 for i in range(len(rules)): # i represents the ith rule in rules
			ruleset = {'on': rules[i], 'off': list(set(range(minindex, maxindex+1)) - set(rules[i]))}
			if wrap == True:
			 if all(state[(cell + index)%len(state)] == 1 for index in ruleset['on']) and all(state[(cell + index)%len(state)] == 0 for index in ruleset['off']):
				newstate[cell] = 1
				break
			 else:
				newstate[cell] = 0
			else:
			 if all(0 < cell + index < len(state) - 1 and state[(cell + index)] == 1 for index in ruleset['on']) and all(0 < cell + index < len(state) - 1 and state[(cell + index)] == 0 for index in ruleset['off']):
				newstate[cell] = 1
				i = 0
				j = 0
				break
			 else:
				newstate[cell] = 0
			
	return newstate

if __name__ == "__main__":
	main()
