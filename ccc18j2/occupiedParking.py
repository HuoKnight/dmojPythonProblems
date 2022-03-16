import re

num = 0
numSpaces = int(input())
ySpaces = [char for char in input()]
tSpaces = [char for char in input()]


for i in range(numSpaces):
    if ySpaces[i] == tSpaces[i] == 'C':
       num += 1 
    ###
###

print(num)
