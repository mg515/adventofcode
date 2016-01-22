# http://adventofcode.com/day/8


import os
os.chdir("/media/diskC/Documents and Settings/miha/Documents/adventofcode/8/")

# part1
f = open("input.txt", "r" )
sum(len(line[:-1]) - len(eval(line)) for line in f)
f.close()

# part2
f = open("input.txt", "r" )
sum(2 + line.count('\\') + line.count('"') for line in f)
f.close()