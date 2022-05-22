def is_increasing(lst):
    smaller = True
    for i in range(len(lst)):
        if lst[i] >= lst[i + 1]:
            continue
        else:
            break
        ###
    ###
    return smaller
###


numInput = int(input())
boxes = {}

for i in range(numInput):
    boxes["%d" % (i + 1)] = [char for char in input()]
    for b in range(int(boxes["%d" % (i + 1)][0])):
        boxes["%d" % (i + 1)].remove(' ')
    ###
    boxes["%d" % (i + 1)].pop(0)
###



print(boxes)
