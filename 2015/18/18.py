# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 14:22:52 2015

@author: miha
"""


import os
os.chdir("/media/diskC/Documents and Settings/miha/Documents/adventofcode/18/")

import numpy as np
from copy import copy

f = open("input.txt", "r")
matrika = np.matrix([list(line)[:-1] for line in f]).astype(int)
f.close()
matrika[0, 0] = 1
matrika[99, 99] = 1
matrika[0, 99] = 1
matrika[99, 99] = 1
matrika = np.append(np.zeros((100,1), dtype=int), matrika, axis=1)
matrika = np.append(matrika, np.zeros((100,1), dtype=int), axis = 1)
matrika = np.append(matrika, np.zeros((1,102), dtype=int), axis = 0)
matrika = np.append(np.zeros((1,102), dtype=int), matrika, axis = 0)

def povej_akcijo(okvir):
    sredinski = okvir[1,1]
    prizgani = okvir.sum() - sredinski
    if sredinski == 1 and (prizgani == 2 or prizgani == 3):
        return 1
    elif sredinski == 0 and prizgani == 3:
        return 1
    else: return 0


matrika1 = copy(matrika)
for obrat in range(100):

    for vrstica in range(1,101):
        for stolpec in range(1,101):
            okvir = matrika[(vrstica-1):(vrstica+2), (stolpec-1):(stolpec+2)]
            matrika1[vrstica, stolpec] = povej_akcijo(okvir)
            
    matrika1[1, 1] = 1
    matrika1[100, 100] = 1
    matrika1[1, 100] = 1
    matrika1[100, 1] = 1
    matrika = copy(matrika1)
    print "vsota"+str(matrika.sum())
    print matrika

