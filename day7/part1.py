def traverse(grid, row, col): 
    global count
    changed = False
    while row < len(grid): 
        row += 1
        if grid[row][col] == "^":
            try:
                if grid[row][col - 1] == ".":
                    if not changed:
                        count += 1
                        changed = True
                    grid[row][col - 1] = "|"
                    traverse(grid, row, col - 1)
                elif grid[row][col - 1] == "^":
                    pass
            except: 
                pass

            try:
                if grid[row][col + 1] == ".":
                    if not changed: 
                        count += 1
                    grid[row][col + 1] = "|"
                    traverse(grid, row, col + 1)
            except: 
                pass

            return

# with open("day7/testInput.txt") as f: 
with open("day7/input.txt") as f: 
    lines = f.readlines()

grid = [[i.strip() for i in j] for j in lines]
start = grid[0].index("S")

count = 0

traverse(grid, 0, start)

print(count)