dial = 50
count = 0

def rotate(direction, number, dial): 
    global count
        
    if direction == "L":
        newDial = (dial - number) % 100
        if dial - number <= 0: 
            zeroes = abs((dial - number) // 100)

            if abs(dial - number) == 100: zeroes += 1
            if dial == 0: zeroes -= 1
            if newDial == 0: zeroes -= 1

            count += max(zeroes, 0)

        return newDial
        
    else: 
        newDial = (dial + number) % 100
        if dial + number > 99: 
            zeroes = abs((dial + number) // 100)

            if abs(dial - number) == 100: zeroes += 1
            if dial == 0: zeroes -= 1
            if newDial == 0: zeroes -= 1

            count += max(zeroes, 0)

        return newDial
    
with open("day1/testInput.txt") as f: 
# with open("day1/input.txt") as f: 
    instructions = f.readlines()
    instructionsDecoded = []

    for i in instructions: 
        instructionsDecoded.append((i[0], int(i[1:].replace("\n", ""))))

for i in instructionsDecoded: 
    dial = rotate(i[0], i[1], dial)
    if dial == 0: count += 1

print(count)