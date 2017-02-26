'''
Created on 26 Feb 2017

@author: Daniele
'''


from nose.tools import eq_

from src.led_tester import *


uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
            
def test_inputline():
    line = "turn on 0,0 through 11,11"
    expected = ["turn on",0,0,11,11]
    result = extract(line)
    eq_(result, expected, "[]".format(result))
    
def test_inputline2():
    line = "turn on 0, through 11,11"
    expected = 0
    result = extract(line)
    eq_(result, expected, "The function should have returned none")

def test_inputline3():
    line = "churn on 0,0 through 11,11"
    expected = 0
    result = extract(line)
    eq_(result, expected, "The function should have returned none")

def test_count():
    count = turn_switch(uri)
    expected = [uri,400410]
    eq_(count, expected, "The count should be 400410")
