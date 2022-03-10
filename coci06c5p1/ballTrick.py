string = input()
index = 1
array = [char for char in string]

for i in array:
    if i == 'A':
        if index == 1:
            index = 2
        elif index == 2:
            index = 1
        else:
            continue
        ###
    elif i == 'B':
        if index == 2:
            index = 3
        elif index == 3:
            index = 2
        else:
            continue
        ###
    elif i == 'C':
        if index == 1:
            index = 3
        elif index == 3:
            index = 1
        else:
            continue
        ###
    ###
###

print(index)
