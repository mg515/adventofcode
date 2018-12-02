


myfile = open('input.txt', 'r')
sez = myfile.read().strip().splitlines()
myfile.close()


for x in sez:
    for y in sez:
        if x == y:
            continue
        else:
            count = 0
            for z in  zip(x,y):
                if z[0] != z[1]:
                    count += 1
                if count > 1:
                    break
            if count == 1:
                print(x)
                print(y)