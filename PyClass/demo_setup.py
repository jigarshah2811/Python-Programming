from distutils.core import setup, Extension

setup(name = 'CExtDemo',
      version = '1.0',
      description = 'Show how to make basic C extensions',
      ext_modules = [Extension('demo', sources = ['demo.c'])])
