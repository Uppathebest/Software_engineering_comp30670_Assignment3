'''
Created on 20 Feb 2017

@author: Daniele
'''
from setuptools import setup

setup(name="led_tester",
      version="0.1",
      description="Assignment 3 Software Engineering",
      url="",
      author="Daniele Strafile",
      author_email="daniele.strafile@ucdconnect.ie",
      license="GPL3",
      packages=['src'],
      entry_points={
          'console_scripts':['led_test=src.led_tester:turn_switch']
          }
      )
