# gui.wm.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains the window manager

### Imports

import tk.ttkExtra as tk

from lib.constants import *

### Main classes

class WindowManager(object):
	'''Handles the screen switching'''
	def __init__(self, master, **options):
		self.master = master
		self.options = options
		self.place_options = options.get('place_options', {})
		self.current = None
		self.screens = {}
			
	def set(self, screens):
		'''Sets the window manager's screens'''
		if not self.screens: # "screens" dictionary is empty
			self.screens = screens
		else:
			for name, screen in screens.items():
				self.add(name, screen)
			
	def add(self, name, screen):
		'''Adds a screen to the window manager'''
		self.screens[name] = screen
			
	def open(self, screen, **options):
		'''Switches to a new screen'''
		if not self.screens:
			raise ValueError("No screens set!")
		if self.current:
			self.current.place_forget() # hide the previous window
		if 'inherit' not in options:
			options['inherit'] = False
		window = self.screens.get(screen, NOT_FOUND)
		if window == NOT_FOUND:
			return False
		else:
			if not isinstance(window, tk.Frame): # create a new Frame object if it does not exist already
				window = window(self.master, self)
				self.screens[screen] = window
			# window.pack(**self.pack_options)
			window.place(**self.place_options)
			# window.grid(**self.grid_options) # show the new window
			if hasattr(window, 'onload'):
				window.onload()
			self.current = window
		self.master.update()
		return True
		