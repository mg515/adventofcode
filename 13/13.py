# http://adventofcode.com/day/13


import os
os.chdir("/media/diskC/Documents and Settings/miha/Documents/adventofcode/13/")

import re
import itertools

f = open( "input.txt", "r" )

slovar = {}
osebe = set()
for line in f:
    
        oseba1 = re.search(r'\w+', line).group()
        try:
            len(re.search(r'gain', line).group())
            weight = int(re.search(r'\d+', line).group())
        except:
            weight = -int(re.search(r'\d+', line).group())
        oseba2 = re.search(r'(?<=to\s)(\w+)', line).group()
        
        osebe.add(oseba1); osebe.add(oseba2)
        
        tup = (oseba1, oseba2)
        slovar[tup] = weight

f.close()


for oseba in osebe:
    slovar[('me', oseba)] = 0
    slovar[(oseba, 'me')] = 0


def izracunaj_sreco(chain, slovar, part2):
    
    chain = list(chain)
    if part2:
        chain.append('me')
    vs = slovar[(chain[0], chain[len(chain)-1])] + slovar[(chain[len(chain)-1], chain[0])]
    return sum(slovar[(chain[i], chain[i+1])] + slovar[(chain[i+1], chain[i])] for i in range(len(chain)-1)) + vs
    
# True for part1, False for part2 solution
max([izracunaj_sreco(chain, slovar, False) for chain in itertools.permutations(osebe)])
    
