machines = []
tPlayed = 0
slot = 1
numCoins = int(input())

machines.extend([int(input()), int(input()), int(input())])


while numCoins > 0:
    
    numCoins -= 1
    if slot == 1:
        slot = 2
        machines[0] += 1
        if machines[0] == 35:
            numCoins += 30
            machines[0] = 0
        ###
    elif slot == 2:
        slot = 3
        machines[1] += 1
        if machines[1] == 100:
            numCoins += 60
            machines[1] = 0
        ###
    elif slot == 3:
        slot = 1
        machines[2] += 1
        if machines[2] == 10:
            numCoins += 9
            machines[2] = 0
        ###
    ###
    
    tPlayed += 1
    
###


print("Martha plays %d times before going broke." % tPlayed)
