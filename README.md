Cellular-Automata
=================

What is Cellular Automata?
	Cellular Automata is a simulation of the life and death of various entities that affect each other. 
	A typical Automaton consists of a grid (though other arrangements are also common) of "cells" that have one of numerous states.
	This project uses a binary system, so a cell can either be ON or OFF.

	The Automaton evolves by following a set of discrete rules.
	For example, a popular implementation of Cellular Automata, Conway's Game of Life, turns on a cell when two of its adjacent cells are currently on.
	A cell is turned off, however, if more than three of its adjacent cells are on. This implementation also uses a binary system..

	By applying these rules repeatedly, the various generations can become increasingly complex and form very intricate patterns.

	An Automaton can be Totalistic or Non-Totalistic, and can exist in more than one dimension.
	A Totalistic Automaton only counts the number of neighboring cells; a Non-Totalistic considers the arrangement of the neighboring cells as well.
	Our program allows the choice of the dimension, as well as the cell of interest, rules, and initial state.

Cellular Automata Terms
	Automaton - Entire evolving system
	Cell - Singular entity that can affect other entities
	State - Variance of cell (can be ON or OFF in Chaotic Automata)
	Rules - A set of predefined laws that govern how a cell affects its neighboring cells
	Cell of Interest - The cell that is affected when a particular rule matches
	Cellstate - State and arrangement of the cells at a given generation

Using the Program
	Every aspect of the program contains a "Help" button if it was necessary.
	These contain small, simple bits of text that help explain how the program works to the user.

	The user can input the following characteristics: Dimension, Cell of Interest, Rules, and Initial State.

Features of Chaotic Automata:
	- 1-Dimensional (Non-Totalistic) and 2-Dimensional (Totalistic) Automata
	- Wrap mode
	- Supports an unlimited number of rules
	- Allows different Cells of Interest
	- Custom initial cellstate
	- Various Preset Examples
	- Automatic Automaton History Recording (can run previous automata)
	- Settings Editor (including Font, Fullscreen, Color, etc.)

DEVELOPER DISCLAIMER

Chaotic Automata is licensed under the General Public License (GPL) version 3.0.

The source may be modified and/or distributed as open-source software, under the condition that the original creator names and license are provided and kept intact.

The developers provide the software "as-is" and do not take any responsibility for any damage or harm caused by the software.
Changing the source code may lead to unexpected results, and the developers do not have any liabilities toward this.

GPL DISCLAIMER

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License (version 3) as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Created by Rushy Panchal and George Georges. &#169; 2014. All rights reserved.