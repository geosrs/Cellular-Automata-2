# constants.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains the main constants

import xmlparse as xml

### Main constants

DATA = xml.dictionary('data.xml', xml.FILE, contains = xml.TEXT)

### Supplementary constants

NAME = DATA.title.text
AUTHORS = DATA.authors.text
COPYRIGHT = DATA.copyright.text

### Window-managing constants

START = 0
MAIN_PROGRAM = 1
ABOUT = 2
HELP = 3
CREDITS = 4
HISTORY = 5

### Miscellaneous Constants

NOT_FOUND = "not found"