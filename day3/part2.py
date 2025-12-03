def findMaxJoltage(battery: str): 
    currectVoltage = ""
    digitsLeft = 12

    while digitsLeft > 0:
        for i in range(9, -1, -1):
            if str(i) in battery and battery.find(str(i)) < len(battery) - digitsLeft + 1:
                currectVoltage += str(i)
                digitsLeft -= 1
                battery = battery[battery.find(str(i)) + 1:]
                break
    
    return currectVoltage

# with open("day3/testInput.txt") as f: 
with open("day3/input.txt") as f:
    lines = f.readlines()

sum = 0

for i in lines:
    result = int(findMaxJoltage(i.replace("\n", "")))
    print(result)
    sum += result

print("\n------\n")
print(sum)