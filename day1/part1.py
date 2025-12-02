dial = 50
count = 0

def rotate(direction, number, dial): 
    if direction == "L": 
        return (dial - number) % 100
        
    else: 
        return (dial + number) % 100
    
# with open("day1/testInput.txt") as f: 
with open("day1/input.txt") as f: 
    instructions = f.readlines()
    instructionsDecoded = []

    for i in instructions: 
        instructionsDecoded.append((i[0], int(i[1:].replace("\n", ""))))

for i in instructionsDecoded: 
    dial = rotate(i[0], i[1], dial)
    if dial == 0: count += 1

print(count)