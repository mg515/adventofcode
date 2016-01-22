# http://adventofcode.com/day/14


import os
os.chdir("/media/diskC/Documents and Settings/miha/Documents/adventofcode/14/")

import re


cas = 2503

f = open( "input.txt", "r" )


razd = 0
slovar = {}
for line in f:
    ime = re.search(r'\w+(?=\scan)', line).group()
    hitrost = int(re.search(r'\d+(?=\skm/s)', line).group())
    cas_hitrost = int(re.search(r'\d+(?=\sseconds)', line).group())
    cas_pocitek = int(re.search(r'\d+(?=\sseconds.$)', line).group())

    razd1 = sum(hitrost for i in range(cas) if i % (cas_hitrost + cas_pocitek) < cas_hitrost )
    if razd1 > razd:
        razd = razd1


    # part2
    slovar[ime] = (hitrost, cas_hitrost, cas_pocitek)
    
f.close()



# part2
progresiva = [0 for i in slovar.keys()]
tocke = [0 for i in slovar.keys()]
for i in range(cas):
    
    for j in range(len(slovar.keys())):

        # prepisan zgornji pogoj v obliki z indeksi
        if (i % (slovar[slovar.keys()[j]][1] + slovar[slovar.keys()[j]][2]) < slovar[slovar.keys()[j]][1]):
            progresiva[j] = progresiva[j] + slovar[slovar.keys()[j]][0]
    
    maksi = max(progresiva)
    leaders = [j for j,k in enumerate(progresiva) if k == maksi]
    print leaders
    for j in leaders:
        tocke[j] = tocke[j] + 1
        
        