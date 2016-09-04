from distutils.core import setup, Extension

setup (name = 'SwigDemo',
       version = '0.1',
       description = 'Show how to apply SWIG to create basic C wrapper functions',
       ext_modules = [Extension('_project', sources = ['mytools.c', 'project_wrap.c'])])
