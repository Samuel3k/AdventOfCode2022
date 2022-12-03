largest = [0, 0, 0]
file = open("input.txt", "r")
current = 0
lines = file.readlines()
for line in lines:
    line = line.strip()
    if line == "":
        if current > largest[0]:
            largest[0] = current
            largest.sort()
        current = 0
    else:
        current += int(line)

print(sum(largest))
