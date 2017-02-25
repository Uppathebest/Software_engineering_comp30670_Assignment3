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
        lines = buffer.splitlines()
        return lines
    else:
        buffer = open(fname).read()
        return buffer
            # process line
            
uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"


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
                
                
# create square             
def LED_TESTER(value):
    if value > 0 and value < 10**9:
        list_false = [ [False]*value for _ in range(value) ]    
        return list_false

# count number of lights which are turned on in square
def lights_number(square):
    count = 0
    for x in square:
        for j in x:
            if j == True:
                count += 1
    return count 
    

# this is the function to turn off/on/ switch lights
def turn_switch(file):
    read_file = read_uri(file)
    for i, line in enumerate(read_file):
        if i == 0:
            n = int(line)
            square = LED_TESTER(n)
        else:
            instructions = extract(line)
            if instructions[0] == "turn on":
                for i in range(instructions[1],instructions[3] + 1):
                    for j in range(instructions[2], instructions[4] + 1):
                        square[i][j] = True
            elif instructions[0] == "turn off":
                for i in range(instructions[1],instructions[3] + 1):
                    for j in range(instructions[2], instructions[4] + 1):
                        square[i][j] = False
            elif instructions[0] == "switch":
                for i in range(instructions[1],instructions[3] + 1):
                    for j in range(instructions[2], instructions[4] + 1):
                        if square[i][j] == True:
                            square[i][j] = False
                        else:
                            square[i][j] = True
    return lights_number(square)
                         
turn_switch(uri)

"""
    
    for i in range(10):
        for j in range(10):
            print(LED_TESTER(10)[i][j], end="")
            print()
            
"""           
            

    
    


    

    
    
    
    