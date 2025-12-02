dial = 50
dirCode = {"L": -1, "R": 1}
count = 0

def rotate(direction, n, dial): 
    global count
    direction = dirCode[direction]

    while n > 0: 
        if dial == 100: dial = 0
        if dial == -1: dial = 99
        if dial == 0: count += 1

        n -= 1
        dial += direction    

    return dial

# with open("day1/testInput.txt") as f: 
with open("day1/input.txt") as f: 
    instructions = f.readlines()
    instructionsDecoded = []

    for i in instructions: 
        instructionsDecoded.append((i[0], int(i[1:].replace("\n", ""))))

for i in instructionsDecoded: 
    dial = rotate(i[0], i[1], dial)

print(count)