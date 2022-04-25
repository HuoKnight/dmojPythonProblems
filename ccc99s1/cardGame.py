deck = []
high = ['ace', 'queen', 'king', 'jack']
A = 0
B = 0
points = 0

for i in range(52):
    deck.append(input())
###

for i in range(len(deck)):
    points = 0
    if deck[i] == 'ace' and i < 48 and not deck[i + 1] in high and not deck[i + 2] in high and not deck[i + 3] in high and not deck[i + 4] in high:
        points = 4
    elif deck[i] == 'king' and i < 49 and not deck[i + 1] in high and not deck[i + 2] in high and not deck[i + 3] in high:
        points = 3
    elif deck[i] == 'queen' and i < 50 and not deck[i + 1] in high and not deck[i + 2] in high:
        points = 2
    elif deck[i] == 'jack' and i < 51 and not deck[i + 1] in high:
        points = 1
    ###

    if (i + 1) % 2 != 0 and points != 0:
        print("Player A scores %d point(s)." % points)
        A += points
    elif points != 0:
        print("Player B scores %d point(s)." % points)
        B += points
    ###
###

print("Player A: %d point(s).\nPlayer B: %d point(s)." % (A, B))
