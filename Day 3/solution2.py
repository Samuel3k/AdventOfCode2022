file = open("input.txt", "r")
lines = file.readlines()
total = 0
for index in range(0, len(lines), 3):
    set1 = set(lines[index].strip())
    set2 = set(lines[index + 1].strip())
    set3 = set(lines[index + 2].strip())
    i = (set1 & set2 & set3).pop()
    if i.isupper():
        total += ord(i) - 38
    else:
        total += ord(i) - 96
print(total)
