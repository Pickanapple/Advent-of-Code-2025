# with open("day6/testInput.txt") as f:
with open("day6/input.txt") as f:
    lines = f.readlines()

for i in range(len(lines)): 
    lines[i] = lines[i].strip()

splitLines = [i.split() for i in lines]

total = 0

for i in range(len(splitLines[0])):
    answer = int(splitLines[0][i])
    operation = splitLines[-1][i]

    for j in splitLines[1:len(splitLines) - 1]: 
        if operation == "+":
            answer += int(j[i])
        elif operation == "*": 
            answer *= int(j[i])

    total += answer

print(total)