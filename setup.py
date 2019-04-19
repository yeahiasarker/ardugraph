from setuptools import setup

setup(name='ardugraph',
      version='0.1',
      install_requires=['pyserial','matplotlib'],
      description = "A Python module that provides a serial communication with \
      Arduino microcontroller boards in order to plot, write, visualize of data ",
      author='Tristan Hearn',
      author_email='goyeahia@gmail.com',
      url='https://github.com/goyeahia/ardugraph',
      license='MIT',
      packages=['ardugraph'],
)