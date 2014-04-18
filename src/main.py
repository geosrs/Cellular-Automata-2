# main.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Main Cellular Automata Project

''''
Notes:
	- need to fix the sizing when dimensions are changed

Tasks:
	Rushy: Interface/Main program optimization:
		https://wiki.python.org/moin/PythonSpeed/PerformanceTips
	George: Optimizing in Python + separating tasks (so some can be ported to C in the future)
	Naomi: Researching + experimenting with extending Python with C
		- need to port the computationally extensive tasks (state checking?) to C

	Optimization Notes:
		- use str.join instead of concatenation
		- xrange instead of range (in Python 2.7)
		- x + x is faster than 2 * x
		- use fewer function calls for small tasks
		- use builtin functions (written in C)
		- map is faster than loops
		- use profiling modules (profile, cProfile) to test where the program is slowest
		- use for loops instead of while loops
'''

### Imports

import tk.ttkExtra as tk

from lib import *

def main():
	'''Main application process'''
	root = tk.Tk()
	initializeStyles(root)
	app = App(root)
	app.center()
	app.mainloop()

if __name__ == "__main__":
	main()
	