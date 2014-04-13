# constants.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains the main constants

### Imports

import xmlparse as xml
import json
import os

import setup

### Main constants

SETUP_STATUS = setup.run()

CUR_DIR = os.getcwd()
USER_DIR = os.path.join(CUR_DIR, "user")
LIB_DIR = os.path.join(CUR_DIR, "lib")
DEFAULT_DIR = os.path.join(LIB_DIR, "defaults")

DATA_PATH = os.path.join(LIB_DIR, "data.xml")
SETTINGS_PATH = os.path.join(USER_DIR, "settings.json")
HISTORY_PATH = os.path.join(USER_DIR, "history.json")

# Remove once testing is done
SETTINGS_PATH = os.path.join(DEFAULT_DIR, "settings.json")
HISTORY_PATH = os.path.join(DEFAULT_DIR, "history.json")

# retrieve data from the various files
DATA = xml.dictionary(DATA_PATH, xml.FILE, contains = xml.TEXT)

with open(SETTINGS_PATH, 'r') as SETTINGS_FILE:
	SETTINGS = json.load(SETTINGS_FILE)
with open(HISTORY_PATH, 'r') as HISTORY_FILE:	
	HISTORY = json.load(HISTORY_FILE)

### Supplementary constants

NAME = DATA.title.text
AUTHORS = DATA.authors.text
COPYRIGHT = DATA.copyright.text

### Window-managing constants

START = 1
MAIN_PROGRAM = 2
ABOUT = 3
HELP = 4
CREDITS = 5
HISTORY = 6
OPTIONS_SPACE = 7

### Miscellaneous Constants

NOT_FOUND = "not found"