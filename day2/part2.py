# with open("day2/testInput.txt") as f:
with open("day2/input.txt") as f:
    lines = f.read().replace("\n", "").split(",")

linesExtended = []

for i in lines: 
    i = i.split("-")
    linesExtended.append([j for j in range(int(i[0]), int(i[1]) + 1)])
    
sum = 0
used = set()

for i in linesExtended:
    for j in i: 
        j = str(j)

        for k in range(0, len(j)//2 + 1):
            for l in range(k, len(j)//2 + 1):
                if j in used: continue

                if j.replace(j[k:l], "") == "":
                    used.add(j)
                    sum += int(j)

print(sum)