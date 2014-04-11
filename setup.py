# setup.py
# Sets up the Cellular Automata Files

import subprocess
import shutil
import os

CUR_DIR = os.getcwd()

# Other settings

BUILD_PATH = os.path.join(CUR_DIR, "src")

# Files and extensions to include

PACKAGES = ["tk"]
MODULES = ['xmlparse']

def setup():
	'''Sets up the files'''
	print("Copying Packages and Modules")
	for package in PACKAGES:
		try:
			shutil.rmtree(os.path.join(BUILD_PATH, package))
		except (WindowsError, IOError):
			pass
		try:
			path = __import__(package).__path__[0]
			subprocess.call(['robocopy', path, '/E', os.path.join(BUILD_PATH, package)])
			print("\tCopied {} successfully".format(package))
		except AttributeError:
			print("\tError copying {}".format(package))
	for module in MODULES:
		try:
			os.remove(os.path.join(BUILD_PATH, module + '.py'))
			os.remove(os.path.join(BUILD_PATH, module + '.pyc'))
		except (WindowsError, IOError):
			pass
		path = __import__(module).__file__.replace('.pyc', '.py')
		shutil.copyfile(path, os.path.join(BUILD_PATH, module + '.py'))
		print("\tCopied {} successfully".format(module))
	
if __name__ == "__main__":
	setup()