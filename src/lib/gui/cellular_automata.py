# cellstate.py
# Rushy Panchal & George Georges
# Copyright 2014

import tk.ttkExtra as tk
import tk.graphics as graph

### Main CAGrid class

class CAGenerator(object):
	'''Cellular Automata Generator window'''
	def __init__(self, window):
	 	self.window = window

	def initializeDraw(self, initial, rules, width, height, dimension = 2, wrap = True, interest = 0):
	 	'''Draws the Cellular Automata'''
	 	window = self.window
	 	window.setBackground("white")
	 	self.initial, self.rules, self.width, self.height, self.dimension, self.wrap = initial, rules, width, height, dimension, wrap
	 	self.cellstate = self.initial
	 	self.interest = interest
	 	self.rulesets = [{'on': rule, 'off': list(set(xrange(-2, 3)) - set(rule))} for rule in self.rules]
	 	self.current = 1

	def draw(self, amount = 1):
		'''Draws the next "amount" of iterations'''
		if self.dimension == 1:
			done = 0
			cellspace = self.initial
			while done < amount:
				for x in xrange(len(cellspace)):
					if cellspace[x] == 1:
						self.window.click(x, self.current, True)
				self.cellstate = cellspace = self.generate1D(cellspace)
				done += 1
				self.current = (self.current + 1) % self.height

	def generate1D(self, state):
		'''Returns the 1D cellstate'''
		wrap_amount = len(state)
		newstate = [0] * wrap_amount
		if self.wrap:
			for cell in xrange(wrap_amount):
				for ruleset in self.rulesets:
					if (all(state[(cell + index) % wrap_amount] == 1 for index in ruleset['on'])
						and all(state[(cell + index) % wrap_amount] == 0 for index in ruleset['off'])):
							newstate[(cell + self.interest) % wrap_amount] = 1
							break
		else:
			for cell in xrange(wrap_amount):
				for ruleset in self.rulesets:
					if (all(0 < cell + index < wrap_amount - 1 and state[(cell + index)] == 1 for index in ruleset['on'])
						and all(0 < cell + index < wrap_amount - 1 and state[(cell + index)] == 0 for index in ruleset['off'])):
							newstate[cell + self.interest] = 1
							break
		return newstate
