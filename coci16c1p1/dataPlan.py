_max = int(input())
months = int(input())
avail = 0
spent = [int(input()) for _int in range(months)]

for i in range(months):
    avail = (_max - spent[i]) + avail
###

print(avail + _max)
