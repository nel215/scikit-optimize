try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(name='skopt',
      version='0.0',
      description='Sequential model-based optimization toolbox.',
      packages=find_packages(),
      py_modules=['skopt'])
