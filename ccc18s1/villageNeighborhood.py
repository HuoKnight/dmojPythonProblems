
def avg(a, b):
    return ((a + b)/2)
###

numVil = int(input())
vilPos = []
size = {}
h = 0
allSize = []

for i in range(numVil):
    a = int(input())
    vilPos.append(a)
###

vilPos = sorted(vilPos)

for p in vilPos:
    if vilPos.index(p) == 0:
        h += 1
        continue
    else:
        size["n%d"%h] = []
        if vilPos.index(p) == len(vilPos):
            continue
        else:
            size["n%d"%h].append(avg(vilPos[h], vilPos[h-1]))        
        ###
        #size["n%d"%h].append(avg(vilPos[h], vilPos[h-1]))
        if vilPos.index(p) != 1:
            size["n%d"%(h-1)].append(avg(vilPos[h], vilPos[h-1]))
        ###
        h += 1
    ###
###

for i in range(len(size)):
    if i == len(size) - 1:
        break
    ###
    allSize.append(size["n%d"%(i + 1)][1] - size["n%d"%(i + 1)][0])
###
    

print(sorted(allSize)[0])
