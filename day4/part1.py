def findValid(grid): 
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ".": continue

            amount = 0
            for k in range(-1, 2):
                if i == 0 and k == -1: continue
                for l in range(-1, 2): 
                    if  j == 0 and l == -1: continue
                    try: 
                        if k == l == 0: continue
                        if grid[i + k][j + l] == "@": amount += 1
                    except IndexError:
                        continue

            if amount < 4: 
                total += 1

    return total

# with open("day4/testInput.txt") as f:
with open("day4/input.txt") as f:
    lines = [[i for i in line.strip()] for line in f.readlines()]

print(findValid(lines))