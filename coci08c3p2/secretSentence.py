import re

a = [char for char in input()]
b = ""


for i in range(len(a)):
    if len(a) == i or (len(a) - 1) == i:
        break
    elif re.search(a[i], "aeiou"):
        for p in range(2):
            a.pop(i + 1)
        ###
    ###
    print(b.join(a))
###

print(b.join(a))
