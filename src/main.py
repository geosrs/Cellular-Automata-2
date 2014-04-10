# main.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Main Cellular Automata Project

import tk.ttkExtra as tk

from constants import *

def main():
	'''Main application process'''
	root = tk.Tk()
	tk.createBaseStyles(root)
	app = StartScreen(root)
	app.mainloop()

class WindowManager(object):
	'''Main Window Manager'''
	def __init__(self, master):
		self.master = master
		self.current = self.master
		self.windows = {
			START: StartScreen,
			MAIN_PROGRAM: CAWindow,
			}
		
	def open(self, window, replace = True, **options):
		'''Opens a window'''
		# this will close the older window
		# if we want to just switch screens, then use a Frame per "screen", pack to show it, unpack the screen when it's done (to show another)
		if 'inherit' not in options:
			options['inherit'] = False
		appClass = self.windows.get(window, NOT_FOUND)
		if appClass == NOT_FOUND:
			return False
		else:
			if replace:
				self.current.close()
			newWindow = tk.Toplevel(self.master, **options) if not replace else tk.Tk()
			app = appClass(newWindow)
			self.current = app
			app.mainloop()
			return True
	
class StartScreen(tk.BaseCustomWindow):
	'''Start screen for the entire application'''
	def __init__(self, master):
		self.master = master
		self.master.title(NAME)
		self.WM = WindowManager(self.master)
		self.createInterface()
		
	def createInterface(self):
		'''Creates the main interface'''
		self.mainFrame = tk.Frame(self.master)
		self.leftFrame = tk.Frame(self.mainFrame)
		self.rightFrame = tk.Frame(self.mainFrame)
		self.centerFrame = tk.Frame(self.mainFrame)
		self.mainLabel = tk.Label(self.mainFrame, text = NAME)
		self.aboutButton = tk.Button(self.leftFrame, text = "About CA", command = lambda: self.WM.open(ABOUT))
		self.creditsButton = tk.Button(self.leftFrame, text = "Credits", command = lambda: self.WM.open(CREDITS))
		self.startButton = tk.Button(self.rightFrame, text = "Start", command = lambda: self.WM.open(MAIN_PROGRAM))
		self.helpButton = tk.Button(self.rightFrame, text = "Help", command = lambda: self.WM.open(HELP))
		self.historyButton = tk.Button(self.mainFrame, text = "User History", command = lambda: self.WM.open(HISTORY))
		self.exitButton = tk.Button(self.mainFrame, text = "Exit", command = self.close, style = "Quit.TButton")
		
		self.aboutButton.pack(side = "top")
		self.creditsButton.pack(side = "bottom")
		self.historyButton.pack(side = "top")
		self.exitButton.pack(side = "bottom")
		self.startButton.pack(side = "top")
		self.helpButton.pack(side = "bottom")
		self.leftFrame.pack(side = "left", fill = "both")
		self.rightFrame.pack(side = "right", fill = "both")
		# self.centerFrame.pack(side = "top", fill = "both")
		# self.mainFrame.gridWidgets([
			# (self.aboutButton, self.historyButton, self.startButton),
			# (None, self.mainLabel),
			# (self.creditsButton, self.exitButton, self.helpButton)
			# ])
		
		self.mainFrame.pack(side = "top", fill = "both", expand = True, ipadx = 15)
	
class CAWindow(tk.BaseCustomWindow):
	'''Houses the entire Cellular Automata interface'''
	def __init__(self, master):
		self.master = master
	
if __name__ == "__main__":
	main()