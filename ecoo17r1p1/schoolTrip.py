a = {"costs": [], "numS": []}

for i in range(2):
    a["costs"].append(int(input()))
    a["pcnt%d"%i] = [float(i) for i in input().split(" ")]
    a["numS"].append(int(input()))
###

for p in range(2):
    a["numDudes"] = []
    earned = 0
    for c in range(4):
        dudes = int(a["pcnt%d"%p][c] * a["numS"][p])

        a["numDudes"].append(dudes)
    ###

    extraDudes = a["numS"][p] - sum(a["numDudes"])

    a["numDudes"][a["numDudes"].index(max(a["numDudes"]))] = a["numDudes"][a["numDudes"].index(max(a["numDudes"]))] + extraDudes

    earned = (a["numDudes"][0] * 12) + (a["numDudes"][1] * 10) + (a["numDudes"][2] * 7) + (a["numDudes"][3] * 5)
    
    avail = earned/2
    if avail >= a["costs"][p]:
        print("NO")
    elif avail < a["costs"][p]:
        print("YES")
    ###
###

