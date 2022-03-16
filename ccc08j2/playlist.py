values = []
a = 0
PL = ['A', 'B', 'C', 'D', 'E']


while True:
    b = int(input())
    values.append(b)
    if b == 1:
        if values[(len(values) - 2)] == 4:
            break
        ###
    ###
###


button = values[0::2]
num = values[1::2]


for i in button:
    for r in range(num[a]):
        if i == 1:
            PL.append(PL[0])
            PL.pop(0)
        elif i == 2:
            PL.insert(0, PL[-1])
            PL.pop(-1)
        elif i == 3:
            PL.insert(0, PL[1])
            PL.pop(2)
        ###
    ###

    a += 1
    
###



print("%s %s %s %s %s" % (PL[0], PL[1], PL[2], PL[3], PL[4]))
