# main.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Main Cellular Automata Project

import tk.ttkExtra as tk

from constants import *
from gui import *

def main():
	'''Main application process'''
	root = tk.Tk()
	tk.createBaseStyles(root)
	app = App(root)
	app.mainloop()
	
if __name__ == "__main__":
	main()