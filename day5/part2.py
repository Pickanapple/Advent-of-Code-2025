# with open("day5/testInput.txt") as f:
with open("day5/input.txt") as f:
    lines = [i.strip() for i in f.readlines()]

sep = lines.index("")
lines = [[int(j) for j in i.split("-")] for i in lines[0:sep]]
lowers = [i[0] for i in lines]
uppers = [i[1] for i in lines]

lowers.sort()
uppers.sort()

total = uppers[-1] - lowers[0]

for i in range(1, len(lowers)):
    diff = lowers[i] - uppers[i-1] - 1
    if diff > 0: total -= diff

print(total + 1) #The algorithm will miss out the final one, so we have to compensate