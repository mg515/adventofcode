# http://adventofcode.com/day/10


import re

input = "1113222113"
iterations = 40

r = re.compile("((\\d)\\2*)")
for i in range(40):
    input = ''.join(str(len(i)) + i[0] for i,j in r.findall(input))
    
print len(input)