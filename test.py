"""
Created on 20 Feb 2017

@author: Daniele

import sys

from nose.tools import ok_,eq_


from src.main import calculate


def test_calculate():
    ok_(calculate(2,3) == 6, 'calculation is incorrect')
    
def test_version():
    eq_(sys.version_info[0],3,"Python is not version 3")
    
"""