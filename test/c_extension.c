// Rushy Panchal

#include "C:\Python27\Include\Python.h"
#include "stdbool.h"
#include "stdio.h"

int pyLength(PyObject *array) {
	// Returns the length of the array
	return PyList_Size(array);
	}

static PyObject * generateCellSpace(PyObject *rulesets, PyObject *state, PyObject *wrap) {
	// Generates the cell space
	int wrap_amount = pyLength(state);
	int newstate[wrap_amount]; // create array with 0 as every value
	int c_state[wrap_amount];
	// extract all of the elements into a C array for faster processing
	for (int index = 0; index < wrap_amount; index++) {
		PyObject *item = PyList_GetItem(state, index);
		if (!item) {
			return NULL;
			}
		c_state[index] = PyInt_AsLong(item);
		}
	if (wrap == Py_True) {
		for (int cell = 0; cell < wrap_amount; cell++) {
				// need to iterate over the rulesets
			}
		}
	// Convert the array to a Python List
	PyObject *py_newstate = PyList_New(wrap_amount);
	if (!py_newstate) {
		return NULL;
		}
	for (int i = 0; i < wrap_amount; i++) {
		PyObject *cell = PyInt_FromLong(newstate[i]);
		if (!cell) {
			Py_DECREF(py_newstate);
			return NULL;
			}
		PyList_SET_ITEM(py_newstate, i, cell);
		}
	return py_newstate;
	}

int main() {
	printf("derp");
	return 0;
	}
