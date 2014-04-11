# wm.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains the window manager

import tk.ttkExtra as tk

from constants import *

class WindowManager(object):
	'''Handles the screen switching'''
	def __init__(self, master):
		self.master = master
		self.current = None
		self.screens = None
			
	def set(self, screens):
		'''Sets the window manager's screens'''
		self.screens = screens
			
	def open(self, screen, **options):
		'''Switches to a new screen'''
		if not self.screens:
			raise ValueError("No screens set!")
		if self.current:
			self.current.grid_forget()
		if 'inherit' not in options:
			options['inherit'] = False
		appClass = self.screens.get(screen, NOT_FOUND)
		if appClass == NOT_FOUND:
			return False
		else:
			window = self.screens[screen]
			if isinstance(window, tk.Frame):
				window.grid()
			else:
				window = window(self.master)
				window.grid()
			self.current = window
			