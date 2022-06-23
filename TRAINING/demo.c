
#include "Python.h"
#include <stdio.h>
#include <string.h>

PyObject *
c_show(PyObject *self, PyObject *args)
{
    const char *s;

    if(!PyArg_ParseTuple(args, "s", &s))
        return NULL;
    printf("<<%s>>\n", s);
    return Py_BuildValue("");
}

/* extract the n-th character from a string */
PyObject *
myindex(PyObject *self, PyObject *args)
{
    const char *s;
    char c;
    int x;
    int n;

    if(!PyArg_ParseTuple(args, "si", &s, &x))
        return NULL;
    n = strlen(s);
    if (x < 0) {
        x += n;
    }    
    if (x >= n || x < 0) {
        PyErr_SetString(PyExc_IndexError, "Oops, I did it again.");
        return NULL;
    }
    c = s[x];
    return Py_BuildValue("c", c);
}

/* sumpoly(3x**2 + 2x - 5, over 0 .. n-1) 
   sumpoly = lambda n:  sum(3*x**2 + 2*x - 5 for x in range(n))
*/
PyObject *
c_sumpoly(PyObject *self, PyObject *args)
{
    int x, n, total=0;

    if(!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    for (x=0 ; x<n ; x++) {
        total += x*(3*x + 2) - 5;
    }
    
    return Py_BuildValue("i", total);
}

static PyMethodDef demo_funcs[] = {
  {"show",    (PyCFunction)c_show,    METH_VARARGS,   "Expose the printf() function from C"},
  {"extract", (PyCFunction)myindex,   METH_VARARGS,   "Extract(str, i) --> s[i]"},
  {"sumpoly", (PyCFunction)c_sumpoly, METH_VARARGS,   "sumpoly(3x**2 + 2x - 5, over 0 .. n-1)"},
  {NULL}
};

void
initdemo(void)
{
    Py_InitModule3("demo", demo_funcs, "misc helper functions module");
}
