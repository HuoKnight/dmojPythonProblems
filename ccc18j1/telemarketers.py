import re

num = input() + input() + input() + input ()

x = re.search("[89](\d)\\1[89]", num)

if x:
    print("ignore")
else:
    print("answer")
###
