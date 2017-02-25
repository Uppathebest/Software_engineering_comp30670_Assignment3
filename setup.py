'''
Created on 20 Feb 2017

@author: Daniele
'''
from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for COMP30670",
      url="",
      author="Daniele Strafile",
      author_email="daniele.strafile@ucdconnect.ie",
      license="GPL3",
      packages=['src'],
      entry_points={
          'console_scripts':['led_tester=src.main:main']
          },
      install_requires=[
          'numpy',
          ],
      )
