# http://adventofcode.com/day/10


import re

def talking(input):
    input = str(input)
    length = len(input)
    new_input = ""
    r = re.compile('(\\d)\\1*')
    while length > 0:
        r = r.match(input)
        together = r.group()
        length1 = len(together)
        new_input = new_input + str(length1) + together[0]
        input = input[len(together):len(input)]
        length = len(input)
    
    return new_input

input = 1113222113
for i in range(40):
    print i
    input = talking(input)
    
len(input)


