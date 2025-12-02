# with open("day2/testInput.txt") as f:
with open("day2/input.txt") as f:
    lines = f.read().replace("\n", "").split(",")

linesExtended = []

for i in lines: 
    i = i.split("-")
    linesExtended.append([j for j in range(int(i[0]), int(i[1]) + 1)])
    
sum = 0

for i in linesExtended:
    for j in i: 
        j = str(j)

        if len(j) % 2 == 1: continue

        if j[len(j)//2:] == j[:len(j)//2]:
            print(j)
            sum += int(j)

print(sum)