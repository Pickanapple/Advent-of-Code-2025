def findMaxJoltage(battery): 
    maxJolt = 0

    for i in range(0, len(battery) - 1):
        for j in range(i + 1, len(battery)):
            if int(battery[i]+battery[j]) > maxJolt: maxJolt = int(battery[i]+battery[j])

    return maxJolt

# with open("day3/testInput.txt") as f:
with open("day3/input.txt") as f:
    lines = f.readlines()

sum = 0

for i in lines:
    sum += findMaxJoltage(i.replace("\n", ""))

print(sum)