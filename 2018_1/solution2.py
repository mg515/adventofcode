
d = {}
curr = 0
notOver = True
while notOver:
  with open('input.txt', 'r') as f:
    for line in f:
      curr += int(line)
      if curr in d.keys():
        print(curr)
        notOver = False
        break
      else:
        d[curr] = 1
