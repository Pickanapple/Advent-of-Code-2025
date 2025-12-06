total = 0

# with open("day6/testInput.txt") as f:
with open("day6/input.txt") as f:
    lines = f.readlines()

for i in range(len(lines)): 
    lines[i] = lines[i].replace("\n", "")[::-1]

splitLines = [list(i) for i in lines]

operation = ""
nums = []

for i in range(len(splitLines[0])):

    temp = ""
    for j in range(len(splitLines)): 
        temp += splitLines[j][i]

    temp = temp.replace(" ", "")

    if "*" in temp or "+" in temp: 
        operation = temp[-1]
        temp = temp[:-1]

        answer = int(temp)
        for i in nums:
            if operation == "+":
                answer += i
            else: 
                answer *= i

        total += answer
        nums = []
    elif temp != "": 
        nums.append(int(temp))

print(total)