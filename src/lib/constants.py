# lib.constants.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Contains the main constants

### Imports

import xmlparse as xml
import pysqlite as sql
import setup
import json
import os

### Main constants

SETUP_STATUS = setup.run() # set up the program files

CUR_DIR = os.getcwd()
USER_DIR = os.path.join(CUR_DIR, "user")
LIB_DIR = os.path.join(CUR_DIR, "lib")
DEFAULT_DIR = os.path.join(LIB_DIR, "defaults")

DATA_PATH = os.path.join(LIB_DIR, "data.xml")
SETTINGS_PATH = os.path.join(USER_DIR, "settings.json")
DATABASE_PATH = os.path.join(USER_DIR, "rules.db")

# Remove once testing is done
SETTINGS_PATH = os.path.join(DEFAULT_DIR, "settings.json")

# retrieve data from the various files
DATA = xml.dictionary(DATA_PATH, xml.FILE, contains = xml.TEXT)

with open(SETTINGS_PATH, 'r') as SETTINGS_FILE:
	SETTINGS = xml.Object(json.load(SETTINGS_FILE))

DATABASE = sql.Database(DATABASE_PATH)

### Supplementary constants

NAME = DATA.title.text

### Window-managing constants --- they identify the various windows

START = "Home"
MAIN_PROGRAM = "Main Program"
ABOUT = "About"
CREDITS = "Credits"
HISTORY = "History"
OPTIONS_SPACE = "Cell Space"
OPTIONS_INTEREST = "Cell of Interest"
OPTIONS_RULES =  "Rules"
DRAW = "Draw"

### User Options

OPTIONS = xml.Object({
	"width": 250,
	"height": 250,
	"dimension": 2,
	"interest": 2,
	"rules": [],
	})

def setOption(key, value = None):
	'''Sets the option "key" to "value"'''
	global OPTIONS
	value = value.get() if hasattr(value, 'get') else value
	OPTIONS[key] = value
	return value

### Miscellaneous Constants

NOT_FOUND = "not found"
