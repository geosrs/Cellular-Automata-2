# gui.styles.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains all styling methods

### Imports

import tk.ttkExtra as tk

from lib.constants import *

### Other Constants

BASE_FONT = SETTINGS.font

def initializeStyles(window):
	'''Initializes the styles for the window'''
	global STYLES
	STYLES = tk.createBaseStyles(window, BASE_FONT + " 12") # create the base styles
	# other styles
	tk.configureStyle(STYLES["Label"], "Header.TLabel", foreground = "red",
		font = BASE_FONT + " 20")
	tk.configureStyle(STYLES["Label"], "Subheader.TLabel", foreground = "blue",
		font = BASE_FONT + " 16")
	tk.configureStyle(STYLES["Label"], "OptionHeader.TLabel", foreground = "purple",
		font = BASE_FONT + " 14")