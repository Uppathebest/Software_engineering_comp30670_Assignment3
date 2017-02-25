'''
Created on 24 Feb 2017

@author: Daniele
'''
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