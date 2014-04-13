# main.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Main Cellular Automata Project

### Imports

import tk.ttkExtra as tk

from lib import *

def main():
	'''Main application process'''
	root = tk.Tk()
	tk.createBaseStyles(root)
	app = App(root)
	app.center()
	app.mainloop()

if __name__ == "__main__":
	main()