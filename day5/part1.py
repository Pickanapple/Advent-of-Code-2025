def checkNum(num, ranges): 
    for i in ranges: 
        if i[0] <= num <= i[1]: 
            return True
        
    return False

# with open("day5/testInput.txt") as f:
with open("day5/input.txt") as f:
    lines = [i.strip() for i in f.readlines()]

sep = lines.index("")
values = [int(i) for i in lines[sep + 1:]]
ranges = [[int(j) for j in i.split("-")] for i in lines[0:sep]]

total = 0

for i in values:
    total += checkNum(i, ranges)

print(total)