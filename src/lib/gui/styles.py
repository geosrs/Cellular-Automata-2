# gui.styles.py
# Rushy Panchal and George Georges
# Cellular Automata Project
# Contains all styling methods

### Imports

import tk.ttkExtra as tk

from lib.constants import *

### Other Constants

def initializeStyles(window, size = None):
	'''Initializes the styles for the window'''
	global STYLES
	BASE_FONT = SETTINGS.font
	if not size:
		size = SETTINGS.size
	STYLES = tk.createBaseStyles(window, (BASE_FONT, size)) # create the base styles
	# other styles
	tk.configureStyle(STYLES["Label"], "Header.TLabel", foreground = "red",
		font = (BASE_FONT, size + 8))
	tk.configureStyle(STYLES["Label"], "Subheader.TLabel", foreground = "blue",
		font = (BASE_FONT, size + 4))
	tk.configureStyle(STYLES["Label"], "OptionHeader.TLabel", foreground = "purple",
		font = (BASE_FONT, size + 2))
	tk.configureStyle(STYLES["Label"], "Help.TLabel", foreground = "darkgreen",
		font = (BASE_FONT, size))
	tk.configureStyle(STYLES["Button"], "Help.TButton", foreground = "blue",
		font = (BASE_FONT, size))
	