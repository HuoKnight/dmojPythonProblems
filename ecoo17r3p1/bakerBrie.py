import numpy as np

for e in range(10):
    points = 0
    dim = [int(char) for char in input().split(' ')]
    grid = []


    for i in range(dim[1]):
        b = []
        a = [int(char) for char in input().split(' ')]
        for p in range(dim[0]):
            b.append(a[p])
        ###
        grid.append(np.array(b))
    ###


    for i in range(dim[1]):
        if sum(grid[i]) % 13 == 0:
            points += sum(grid[i]) / 13
        ###
    ###

    add = sum(grid)

    for i in range(dim[0]):
        if add[i] % 13 == 0:
            points += add[i] / 13
        ###
    ###

    print(points)
###
