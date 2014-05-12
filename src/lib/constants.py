# lib.constants.py
# Rushy Panchal and George Georges
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
IMAGES_DIR = os.path.join(CUR_DIR, "img")
DEFAULT_DIR = os.path.join(LIB_DIR, "defaults")

DATA_PATH = os.path.join(LIB_DIR, "data.xml")
SETTINGS_PATH = os.path.join(USER_DIR, "settings.json")
DEFAULT_SETTINGS_PATH = os.path.join(DEFAULT_DIR, "settings.json")
DATABASE_PATH = os.path.join(USER_DIR, "history.db")
IMAGE_PATHS = {name: os.path.join(IMAGES_DIR, name) for name in os.listdir(IMAGES_DIR)}

# retrieve data from the various files
DATA = xml.dictionary(DATA_PATH, xml.FILE, contains = xml.ALL)

with open(SETTINGS_PATH, 'r') as SETTINGS_FILE:
	SETTINGS = xml.Object.fromDictionary(json.load(SETTINGS_FILE))
with open(DEFAULT_SETTINGS_PATH, 'r') as DEFAULT_FILE:
	DEFAULT_SETTINGS = xml.Object.fromDictionary(json.load(DEFAULT_FILE))

DATABASE = sql.Database(DATABASE_PATH)

### Supplementary constants

NAME = DATA.title.text
HELP = DATA.help

### Window-managing constants --- they identify the various windows

START = "Home"
MAIN_PROGRAM = "Main Program"
ABOUT = "About"
CREDITS = "Credits"
HISTORY = "History"
SETTINGS_EDIT = "Settings"
OPTIONS_SPACE = "Cell Space"
OPTIONS_INTEREST = "Cell of Interest"
OPTIONS_RULES =  "Rules"
DRAW = "Draw"

### User Options

OPTIONS = xml.Object({
	"width": 400,
	"height": 400,
	"dimension": 1,
	"interest": 0,
	"wrap": True,
	"rules": [],
	})

def setOption(key, value = None):
	'''Sets the option "key" to "value"'''
	global OPTIONS
	value = value.get() if hasattr(value, 'get') else value
	OPTIONS[key] = value
	return value

def saveSettings(d):
	'''Saves the settings as a new dictionary'''
	SETTINGS.update(d)
	with open(SETTINGS_PATH, 'w') as SETTINGS_FILE:
		SETTINGS_FILE.write(json.dumps(d, indent = 4).replace('    ', '\t'))

### Miscellaneous Constants

NOT_FOUND = "not found"
