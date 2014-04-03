Cellular-Automata
=================

Nonlinear Dynamics Cellular Automata Project 2014

Current Tasks:
 - Krish: Interface design
 - Rushy: Interface creation
 - George: Create 2D CA test program
 - Naomi: Convert George's 1D CA program to use classes
 - Allan: Work on description of CA for "About CA" screen

Also, we need a standardized indentation (at least with Python).
I use tabs, or you can use 4 spaces. Those are general standards, so stick with one or the either.
 
I still think we should use HTML + CSS + JavaScript for the interface, and then embed
a Java applet with the actual CA. George/Naomi would have to learn Java graphics,
but the overall app would look MUCH better.
 
Notes on Commits:

 - Create a new commit for any change (so we have a running record of changes)
 - Add a decent comment for each commit (so we know what is being changed)
 - Don't commit to a file that someone is still working on (might override some changes)


For any window to work with the main interface, it should be in this format:

	class WindowName(tk.BaseCustomWindow):
		def __init__(self, master):
			self.master

WindowName is your window name, and tk is my library (see https://github.com/panchr/Python-Tkinter-Extensions)
