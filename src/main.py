# main.py
# Rushy Panchal and George Georges
# Main Cellular Automata Project

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
	