# http://adventofcode.com/day/12


import os
os.chdir("/media/diskC/Documents and Settings/miha/Documents/adventofcode/12/")

import re

f = open( "input.txt", "r" )
sez = []
for line in f:
    sez = str(line)
f.close()


test = re.findall("(-\d+)|(\d+)", sez)
a =[]
for tup in test:
    try: a.append(int(tup[0]))
    except: a.append(int(tup[1]))
    
    
    