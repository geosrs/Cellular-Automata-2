# lib.examples.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains various Cellular Automata examples

EXAMPLES = {
	"Sierpinski Triangle": {"dimension": 1, "interest": 0, "wrap": True, "rules": [[-1], [1]]},
	"Diagonal Lines": {"dimension": 1, "interest": 1, "wrap": True, "rules": [[-2], [0, 1]]},
	"Evolving Square": {"dimension": 2, "interest": (0, 0), "wrap": True, "rules": [[(1, 1)], [(2, 2), (0, -1)]]},
	"Moving Snake": {"dimension": 2, "interest": (2, -1), "wrap": True, "rules": [[(1, 1)], [(2, 2), (0, -1)]]},
	}
