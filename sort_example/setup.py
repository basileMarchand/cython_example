from setuptools import setup, Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize
import numpy 

ext_options = {
    'language':"c++",
    'extra_compile_args':["-O3",],
    'include_dirs':[numpy.get_include()]}

extensions = [
    Extension("sortcpp", sources=["src/sortcpp.pyx", "src/cpp_sort.cpp"], **ext_options),
]

setup(
    ext_modules=cythonize(extensions)
)