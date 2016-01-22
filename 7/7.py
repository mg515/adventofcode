# http://adventofcode.com/day/7


import os
os.chdir("/media/diskC/Documents and Settings/miha/Documents/adventofcode/7/")

import re

operators = {
    None: lambda x: x[0],
    "NOT": lambda x: ~x[0],
    "AND": lambda x: x[0] & x[1],
    "OR": lambda x: x[0] | x[1],
    "LSHIFT": lambda x: x[0] << x[1],
    "RSHIFT": lambda x: x[0] >> x[1]
}


dict_of_values = {}

def recursion(wire, operators, dict_of_values):
    
    try:
        dict_of_values[wire]
        return dict_of_values[wire], dict_of_values
    except: print 'no match'
    
    # find the instruction, that defines our wire input
    f = open( "input.txt", "r" )
    for line in f:
        line = line[0:len(line) - 1]
        a = re.search(r'(?<=->\s)' + str(wire) + '$', line)
        try:
            a.group()
            instruction = line
            break
        except: next
    f.close()
    
    

    # extract the values, that define the wire
    defin = re.findall(r'([a-z+]+|\d+)', instruction)
    del defin[-1]

    # recursively calculate the wires, in case they are not integers (yet)
    for i in range(len(defin)):
        try: int(defin[i])
        except: defin[i], dict_of_values = recursion(defin[i], operators, dict_of_values)
    

    # define the operator specified in the instruction
    try: op = re.search(r'NOT|AND|OR|LSHIFT|RSHIFT', instruction).group()
    except: op = None
    
    # calculate and return the value of the wire
    if len(defin) == 2:
        val = operators[op]([int(defin[0]), int(defin[1])])
        dict_of_values[wire] = val
        return val, dict_of_values
    else:
        val = operators[op]([int(defin[0])])
        dict_of_values[wire] = val
        return val, dict_of_values
        
recursion('a', operators, dict_of_values)
    

    
    
    


