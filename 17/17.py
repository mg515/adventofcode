# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 01:09:10 2015

@author: miha
"""

import os
os.chdir("/media/diskC/Documents and Settings/miha/Documents/adventofcode/17/")


f = open("input.txt", "r")
sez = [int(line[:-1]) for line in f]
f.close()



def prestej(conts, target, st):
    
    if target == 0 and st == 0:
        return 1
    if target < 0:
        return 0
    if len(conts) <= 0:
        return 0

    uporabimo_cont = prestej(conts[1:], target-conts[0], st - 1)
    ne_uporabimo_cont = prestej(conts[1:], target, st)
    
    return uporabimo_cont + ne_uporabimo_cont
    
    
prestej(sez, 150, 4)
