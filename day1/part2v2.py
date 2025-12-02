dial = 50
count = 0
direction = {"L": -1, "R": 1}

def rotate(direction, number, dial): 
    global count
    
    if direction == "L":
        while number > 0: 
            gap = dial
            if number <= gap: 
                dial -= number
                return dial
            
            else:
                count += 1
                dial = 99
                # number -= gap + 1

    else: 
        while number > 0: 
            gap = 99 - dial
            if number <= gap: 
                dial += number
                return dial
            
            else:
                count += 1
                dial = 0
                number -= gap + 1

    count -= 1
    return 0 

# with open("day1/testInput.txt") as f: 
with open("day1/input.txt") as f: 
    instructions = f.readlines()
    instructionsDecoded = []

    for i in instructions: 
        instructionsDecoded.append((i[0], int(i[1:].replace("\n", ""))))

for i in instructionsDecoded: 
    dial = rotate(i[0], i[1], dial)
    print(dial)
    if dial == 0: count += 1

print(count)