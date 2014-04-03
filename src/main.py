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
		self.padx, self.pady = 25, 25
		self.mainFrame = tk.Frame(self.master)
		self.subFrame = tk.Frame(self.mainFrame)
		self.aboutButton = tk.Button(self.mainFrame, text = "About CA", command = lambda: self.WM.open(ABOUT))
		self.creditsButton = tk.Button(self.mainFrame, text = "Credits", command = lambda: self.WM.open(CREDITS))
		self.startButton = tk.Button(self.mainFrame, text = "Start", command = lambda: self.WM.open(MAIN_PROGRAM))
		self.helpButton = tk.Button(self.mainFrame, text = "Help", command = lambda: self.WM.open(HELP))
		self.historyButton = tk.Button(self.subFrame, text = "User History", command = lambda: self.WM.open(HISTORY))
		self.exitButton = tk.Button(self.subFrame, text = "Exit", command = self.close, style = "Quit.TButton")
		self.subFrame.gridWidgets([(self.exitButton, self.historyButton)], padx = self.padx, pady = self.pady)
		self.mainFrame.gridWidgets([
			(None, self.aboutButton),
			(self.creditsButton, self.startButton, self.helpButton),
			self.subFrame,
			], padx = self.pady, pady = self.pady)
		
		self.mainFrame.grid(padx = 15, pady = 15)
	
class CAWindow(tk.BaseCustomWindow):
	'''Houses the entire Cellular Automata interface'''
	def __init__(self, master):
		self.master = master
	
if __name__ == "__main__":
	main()