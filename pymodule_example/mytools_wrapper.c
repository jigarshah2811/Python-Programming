#include "Python.h"
#include <stdio.h>

/* Prototype for the wrapped functions */
extern int collatz(int x);

PyObject *
wrap_collatz(PyObject *self, PyObject *args)
{
	int answer = 0;
	if(!PyArg_ParseTuple(args, "i", &x))
		return NULL;
	answer = collatz(x);
	return Py_BuildValue("i", answer);
}

static PyMethodDef demo_funcs[] = {
  {"collatz", (PyCFunction)wrap_collatz,       METH_VARARGS,   "Use collatz from C"},
  {NULL}
};

void
initdemo(void)
{
    Py_InitModule3("demo", demo_funcs, "misc helper functions module");
}
