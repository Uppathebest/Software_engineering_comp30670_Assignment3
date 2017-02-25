"""
Created on 20 Feb 2017

@author: Daniele

"""

import sys

from nose.tools import *
from src.led_tester import *


uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"

def test_calculate():
    eq_(len(read_uri(uri)), 9506, "buffer length does not match" )
            
def test_inputline(line, expected):
    line = "turn on 0,0 through 11,11"
    expected = ["turn on",0,0,11,11]
    result = extract(line)
    eq_(result, expected, "[]".format(result))





