#include "Python.h"

/* Prototypes for the wrapped functions */
extern int collatz(int);
extern int count_vowels(char *);
extern int sumpoly(int);

PyObject *
wrap_collatz(PyObject *self, PyObject *args)
{
    int x, y;

    if(!PyArg_ParseTuple(args, "i", &x))
        return NULL;
    if (x < 0) {
        PyErr_SetString(PyExc_ValueError, "Input must be non-negative");
        return NULL;
    }
    y = collatz(x);
    return Py_BuildValue("i", y);
}

PyObject *
wrap_count_vowels(PyObject *self, PyObject *args)
{
    char *s;
    int y;

    if(!PyArg_ParseTuple(args, "s", &s))
        return NULL;
    y = count_vowels(s);
    return Py_BuildValue("i", y);
}

PyObject *
wrap_sumpoly(PyObject *self, PyObject *args)
{
    int x, y;

    if(!PyArg_ParseTuple(args, "i", &x))
        return NULL;
    y = sumpoly(x);
    return Py_BuildValue("i", y);
}

static PyMethodDef mytools_funcs[] = {
  {"collatz", (PyCFunction)wrap_collatz,       METH_VARARGS,   ""},
  {"sumpoly", (PyCFunction)wrap_sumpoly,       METH_VARARGS,   ""},
  {"count_vowels", (PyCFunction)wrap_count_vowels,       METH_VARARGS,   ""},
  {NULL}
};

void
initmytools(void)
{
    Py_InitModule3("mytools", mytools_funcs, "misc helper functions module");
}
