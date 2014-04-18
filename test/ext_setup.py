from distutils.core import setup, Extension
 
c_ext = Extension('c_extension', sources = ['c_extension.c'])
 
setup(name = 'C Extension',
	version = '1.0',
	description = 'Testing with C extensions',
	ext_modules = [c_ext])