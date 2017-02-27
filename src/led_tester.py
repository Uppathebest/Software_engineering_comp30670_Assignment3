'''
Created on 24 Feb 2017

@author: Daniele
'''
import argparse
import re
import urllib.request


def read_uri():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input help')
    args = parser.parse_args()
    # initialise uri as global variable because i need it in the output of the turn_switch function
    global uri
    uri = args.input
    if uri.startswith('http'):
        req = urllib.request.urlopen(uri)
        buffer = req.read().decode('utf-8')
        lines = buffer.splitlines()
        return lines
    else:
        buffer = open(uri).read()
        return buffer
            # process line
            



def extract(line):
    # check that line contains one of the three possible commands at the beginning
    for string in ["turn on", "turn off", "switch"]:
        if line.strip().startswith(string):
            # now take from the string the 4 integer values we need
            values = re.findall('\d+', line)
            # check that we have found 4 values
            if len(values) == 4:
                # convert values to integer
                values_int = [int(x) for x in values]
                # insert one of the 3 possible commands into the string
                values_int.insert(0, string)
                return values_int
            else:
                return 0
    else:
        return 0
                
                
# create square             
def LED_TESTER(value):
    if value > 0 and value < 10**9:  
        return [ [False]*value for _ in range(value) ]  
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
def turn_switch():
    read_file = read_uri()
    for i, line in enumerate(read_file):
        if i == 0:
            n = int(line)
            square = LED_TESTER(n)
        else:
            instructions = extract(line)
            #handle exception of coordinates, instructions, exception of area of square and exception in the instructions
            if instructions != 0 and square != 0 and instructions[1] < instructions[3] and instructions[2] < instructions[4] and instructions[0] != 0:
                # sanity checks to ensure the coordinate are within the boundaries
                if instructions[1] < 0:
                    instructions[1] = 0
                if instructions[2] < 0:
                    instructions[2] = 0
                if instructions[3] >= n:
                    instructions[3] = n-1
                if instructions[4] >= n:
                    instructions[4] = n-1
                for i in range(instructions[1], instructions[3] + 1):
                    for j in range(instructions[2], instructions[4] + 1):
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
    output = [uri, lights_number(square)]  
    print(output)
    return output

if __name__ == '__main__':
    turn_switch()
    
    
    
'''
RESULTS

uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
['http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt', 400410]


uri2 = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt"
['http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt', 6]


uri3 = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt"
['http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt', 29942250]


uri4 = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt"
['http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt', 389206]



uri5 = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt"
['http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt', 349037]


 
'''




         

    
    


    

    
    
    
    