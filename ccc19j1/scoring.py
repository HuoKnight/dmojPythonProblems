points = []

for i in range(6):
    a = int(input())
    points.append(a)
###

applePoints = ((points[0] * 3) + (points[1] * 2) + points[2])
bananaPoints = ((points[3] * 3) + (points[4] * 2) + points[5])

if applePoints > bananaPoints:
    print("A")
elif bananaPoints > applePoints:
    print("B")
elif applePoints == bananaPoints:
    print("T")
###
