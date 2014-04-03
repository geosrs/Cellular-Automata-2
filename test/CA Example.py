# George Georges
# Cellular Automata Example
# Cell Space: 1D, infinite
# Neighborhood: adjacent, inclusive
# Rule: one cell on only in the neighborhood turns the main cell on, else it turns off
from graphics import *

def main():
	# ca = GraphWin(None, 401, 401, autoflush = False)
	# ca.grid() # this is for running when integrated with Tkinter
	ca = GraphWin("Cellular Automata", 401, 401, autoflush = False)
	ca.setBackground("white") # white background saves computational power (off cells are white and do not need to be plotted)
	ca.setCoords(0, 0, 400, 400)
	cs = [0] * 401
	cs[200] = 1
	# Rushy: the above two lines are equivalent to your for loop, just shorter and more efficient
	
	# cs = []
	# for i in range(401):
		# if i == 200:
			# cs.append(1) # center cell is on
		# else:
			# cs.append(0) # rest of the cells are off
	genca(ca, cs)

def genca(window, cellspace):
	y = 400
	xmin = 0
	x = 0
	ymin = 0
	xmax = 400
	step = 1
	while y >= ymin: # starts from the top of the window and works down
		newcellspace = [] # new cell space created after every row in order to store the current row to generate the next row
		x = xmin
		while x <= xmax:
			if (cellspace[(x - 1)] == 1 and cellspace[x] == 0 and cellspace[(x + 1)%401] == 0): 
				window.plot(x, y, "black") # cell turns ON (turns black)
				newcellspace.append(1)
			elif (cellspace[(x - 1)] == 0 and cellspace[x] == 1 and cellspace[(x + 1)%401] == 0):
				window.plot(x, y, "black") # cell turns ON (turns black)
				newcellspace.append(1)
			elif (cellspace[(x - 1)] == 0 and cellspace[x] == 0 and cellspace[(x + 1)%401] == 1):
				window.plot(x, y, "black") # cell turns ON (turns black)
				newcellspace.append(1)
			else:
				# cell turns OFF (stays white)
				newcellspace.append(0)
			x += step
		window.update() # window updates after every row
		y -= step
		cellspace = newcellspace[:]
		
if __name__ == "__main__":
	main()
