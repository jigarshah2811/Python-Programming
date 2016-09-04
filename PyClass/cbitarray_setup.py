from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
  name = 'Bitarray AdvancedPython app',
  cmdclass = {'build_ext': build_ext},
  ext_modules = [Extension("cbitarray", ["cbitarray.pyx"])]
)
