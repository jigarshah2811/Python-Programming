

from distutils.core import setup, Extension

setup (name = 'CWrapperDemo',
       version = '0.1',
       description = 'Show how to make basic C wrapper functions',
       ext_modules = [Extension('mytools', sources = ['mytools_wrapper.c', 'mytools.c'])])
