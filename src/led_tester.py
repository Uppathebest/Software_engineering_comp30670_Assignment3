'''
Created on 24 Feb 2017

@author: Daniele
'''
import re
import urllib.request
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input help')
args = parser.parse_args()

uri = args.input


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
            



def extract(line):
    # trim whitespaces from line on both sides
    line = line.strip()
    # check that line contains one of the three possible commands at the beginning
    for string in ["turn on", "turn off", "switch"]:
        if line.startswith(string):
            # now take from the string the 4 values we need
            values = re.findall('\d+', line)
            # check that we have found 4 values
            if len(values) == 4:
                # convert values to integer
                values_int = [int(x) for x in values]
                # sanity check: did we find 4 integers?
                if all(isinstance(num, int) for num in values_int) == True:
                    # insert one of the 3 possible commands into the string
                    values_int.insert(0, string)
                    return values_int
                else:
                    return 0
            else:
                return 0
    else:
        return 0
                
                
# create square             
def LED_TESTER(value):
    if value > 0 and value < 10**9:
        list_false = [ [False]*value for _ in range(value) ]    
        return list_false
    else:
        # handle exception
        return 0


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
            # sanity check of instructions
            if instructions != 0:
                y0 = instructions[1]
                x0 = instructions[2]
                y1 = instructions[3]
                x1 = instructions[4]
                # sanity checks to ensure the coordinate are within the boundaries
                if y0 < 0:
                    y0 = 0
                if x0 < 0:
                    x0 = 0
                if x1 >= n:
                    x1 = n-1
                if y1 >= n:
                    y1 = n-1
                #handle exception of coordinates, exception of area of square and exception in the instructions
                if square != 0 and y0 < y1 and x0 < x1 and instructions[0] != 0:
                    for i in range(y0, y1 + 1):
                        for j in range(x0, x1 + 1):
                            if instructions[0] == "turn on":
                                square[i][j] = True
                            elif instructions[0] == "turn off":
                                square[i][j] = False
                            else:
                                # switch : if its on, turn off. if its off, turn on
                                if square[i][j] == True:
                                    square[i][j] = False
                                else:
                                    square[i][j] = True                                 
    output = [file, lights_number(square)]
    print(output)
    return output
'''
uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
uri2 = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt"
uri3 = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt"
uri4 = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt"
uri5 = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt"
 
'''

turn_switch(uri)



         

    
    


    

    
    
    
    