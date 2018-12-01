# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 16:49:45 2015

@author: miha
"""


import os
os.chdir("/media/diskC/Documents and Settings/miha/Documents/adventofcode/16/")

f = open("input.txt", "r")

import re

slovar = {"children": 3,
          "cats": 7,
          "samoyeds": 2,
          "pomeranians": 3,
          "akitas": 0,
          "vizslas": 0,
          "goldfish": 5,
          "trees": 3,
          "cars": 2,
          "perfumes": 1}



# part1
for line in f:
    st = int(re.search('\d+', line).group())
    numbers = [int(i) for i in re.findall('(?<=:\s)\d+', line)]
    names = re.findall('\w+(?=:\s\d+)', line)
    
    if sum(1 for i in range(3) if slovar[names[i]] == numbers[i] ) == 3:
        print st
        break

f.close()


f = open("input.txt", "r")
# part2
for line in f:
    st = int(re.search('\d+', line).group())
    numbers = [int(i) for i in re.findall('(?<=:\s)\d+', line)]
    names = re.findall('\w+(?=:\s\d+)', line)
    
    tocke = 0
    try:
        indc = names.index("cats")
        if slovar[names[indc]] < numbers[indc]:
            tocke += 1
        del numbers[indc]
        del names[indc]
    except:
        pass
    
    try:
        indc = names.index("trees")
        if slovar[names[indc]] < numbers[indc]:
            tocke += 1
        del numbers[indc]
        del names[indc]
    except:
        pass
    
    try:
        indc = names.index("pomeranians")
        if slovar[names[indc]] > numbers[indc]:
            tocke += 1
        del numbers[indc]
        del names[indc]
    except:
        pass
    
    try:
        indc = names.index("goldfish")
        if slovar[names[indc]] > numbers[indc]:
            tocke += 1
        del numbers[indc]
        del names[indc]
    except:
        pass
    
    for i in range(len(names)):
        if slovar[names[i]] == numbers[i]:
            tocke += 1
    
    if tocke == 3:
        print line
        print st
        
f.close()




















