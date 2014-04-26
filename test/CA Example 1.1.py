# George Georges
# Cellular Automata Example
# Cell Space: 1D, infinite
# Neighborhood: adjacent, inclusive
# Rule: one cell on only in the neighborhood turns the main cell on, else it turns off
from graphics import *

def main():
     CA = GraphWin("Cellular Automata", 401, 401, autoflush = False)
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
        print(cellspace)
        for x in range(len(cellspace)):
            if cellspace[x] == 1:
                window.plot(x, y, "black")
        cellspace = generateCellSpace(rules, cellspace)
        window.update() # window updates after every row

def generateCellSpace(rules, state, wrap = True):
    '''input: rules is a list of lists of integers
    (i.e. [[-1,0,1], [-1,1], [0]]), where 0 is the
    cell of interest, and state is a 1D array of
    the current state of all cells in the cell space
    wrap is a boolean that states whether or not the
    cell space is a wrapping cell space'''
    newstate = state[:] 
    for cell in range(len(state)):
        for i in range(len(rules)): # i represents the ith rule in rules
            #for j in range(len(rules[i])): # j represents the jth parameter of rule i
                if wrap == True:
                    if all([newstate[(cell + rules[i][j])%len(newstate)]]) == 1:
                        newstate[cell] = 1
                        # cell += 1
                        i = 0
                        j = 0
                        break
                    else:
                        newstate[cell] = 0
                else:
                    if 0 < rules[i][j] + cell < len(newstate) - 1:
                        if all([newstate[cell + rules[i][j]]]) == 1:
                            newstate[cell] = 1
                            # cell += 1
                            i = 0
                            j = 0
                            break
                        else:
                            newstate[cell] = 0
    return newstate

if __name__ == "__main__":
     main()
