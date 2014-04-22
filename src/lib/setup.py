# lib.setup.py
# Rushy Panchal, Krish Pamani, George Georges, Naomi Popkin, Allan Lee
# Cellular Automata Project
# Sets the program up

### Imports

import xmlparse as xml
import pysqlite as sql
import shutil
import os

### Constants

CUR_DIR = os.getcwd()
USER_DIR = os.path.join(CUR_DIR, "user")
LIB_DIR = os.path.join(CUR_DIR, "lib")
DEFAULT_DIR = os.path.join(LIB_DIR, "defaults")

FILES = ["settings.json"]
SQL_FILE = "rules.sql"
DB_PATH = os.path.join(USER_DIR, "rules.db")

def run():
	'''Sets up the program'''
	status = {}
	if os.path.exists(USER_DIR):
		status["user_dir"] = "exists"
	else:
		# set up user folder if it does not exist
		try:
			os.makedirs(USER_DIR)
			for path in FILES:
				new_path = os.path.join(USER_DIR, path)
				default_path = os.path.join(DEFAULT_DIR, path)
				shutil.copyfile(default_path, new_path)
			status["user_dir"] = "created"
		except OSError:
			status["user_dir"] = "creation failed"
	if os.path.exists(DB_PATH):
		status["rules_db"] = "exists"
	else:
		sql.Database.create(DB_PATH, os.path.join(DEFAULT_DIR, SQL_FILE))
		status["rules_db"] = "created"
	return status
