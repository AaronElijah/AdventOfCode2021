from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("solution2_fast.pyx", annotate=True))
