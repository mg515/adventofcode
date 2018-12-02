
import numpy as np

d = {}
with open('input.txt', 'r') as f:
    for line in f:
        sez = list(line)[:-1]
        cv = np.unique(sez, return_counts=True)[1]
        cv = cv[cv != 1]
        
        cv2 = np.unique(cv, return_counts=True)
        for k in cv2[0]:
            if k in d.keys():
                d[k] += 1
            else:
                d[k] = 1

res = 1
for k in d.keys():
    res *= d[k]

print(res)