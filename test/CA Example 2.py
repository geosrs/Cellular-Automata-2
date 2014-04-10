# George Georges
# Cellular Automata Example 2
# Cell Space: 2D, finite
# Neighborhood: adjacent 8 spaces, inclusive
# Rule: one to three cells only on in the neighborhood turns on the main cell, else it turns off
from graphics import *
import copy
import time

def main():
    ca = GraphWin("Cellular Automata", 401, 401, autoflush = False)
    ca.setBackground("white") # white background saves computational power (off cells are white and do not need to be plotted)
    ca.setCoords(0, 0, 400, 400)
    cs = [[0 for i in range(401)] for j in range(401)]
    cs[200][200] = 1 # center cell is on
    genca2(ca, cs)

def genca2(window, cs):
    y = 399
    ymax = 399
    xmin = 1
    x = 1
    ymin = 1
    xmax = 399
    step = 1
    for m in range(195):
        newcellspace = [[0 for i in range(401)] for j in range(401)]
        window.clear()
        while y >= ymin: # starts from the top of the cell space and works down
            x = xmin
            while x <= xmax: # moves across each row
                if 1 <= cs[x-1][y-1] + cs[x][y-1] + cs[x-1][y] + cs[x][y] + cs[x+1][y] + cs[x][y+1] + cs[x+1][y+1] + cs[x+1][y-1] + cs[x-1][y+1] <= 4:
                    window.plot(x, y, "black")
                    newcellspace[x][y] = 1
                x += step
            y -= step
        cs = copy.deepcopy(newcellspace) # copies the 2D array
        y = ymax
        #window.update()
        print(m)

if __name__ == "__main__":
    main()
