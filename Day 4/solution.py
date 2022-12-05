file = open("input.txt", "r")
lines = file.readlines()
total = 0
for line in lines:
    ranges = line.strip().split(",")
    range1 = ranges[0].split("-")
    range2 = ranges[1].split("-")
    range11 = int(range1[0])
    range12 = int(range1[1])
    range21 = int(range2[0])
    range22 = int(range2[1])
    if (range11 <= range21 and range12 >= range22) or (range21 <= range11 and range22 >= range12):
        total += 1
print(total)
