# http://adventofcode.com/day/11


import os
os.chdir("/media/diskC/Documents and Settings/miha/Documents/adventofcode/11/")

import re
import string

def go_to_next(s, abc):
    try:
        return s[0:-1] + abc[abc.index(s[-1]) + 1]
    except IndexError:
        return go_to_next(s[0:-1], abc) + 'a'


def preveri_pogoj(niz, reg):
    try:
        re.search(r'i|o|l', niz).group()
        return False
    except: pass
    
    if len(set(re.findall(r'(\w)\1', niz))) >= 2:
        pass
    else: return False
    
    try:
        re.search(reg, niz).group()
        return True
    except: return False
    

niz = "hepxcrrq"

abc = string.ascii_lowercase
reg = ''.join(abc[i:(i+3)] + "|" for i in range(len(abc)))[:-6]

while not preveri_pogoj(niz, reg):
    niz = go_to_next(niz, abc)
    
    
    