'''
Created on 24 Feb 2017

@author: Daniele
'''
import re
import urllib.request


def read_uri(fname):
    if fname.startswith('http'):
        req = urllib.request.urlopen(fname)
        buffer = req.read().decode('utf-8')
        return buffer
    else:
        buffer = open(fname).read()
        return buffer
            # process line
            
uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"

read_uri(uri)

def extract(line):
    # check that line contains one of the three possible commands at the beginning
    for string in ["turn on", "turn off", "switch"]:
        if line.startswith(string):
            # now take from the string the 4 values we need
            values = re.findall('\d+', line)
            # check that we have found 4 values
            if len(values) == 4:
                # convert values to integer
                values_int = [int(x) for x in values]
                # insert one of the 3 possible commands into the string
                values_int.insert(0, string)
                return values_int
                
                
                
def LED_TESTER(value):
    return None          

    
    
    
    
    
    