file = open("input.txt", "r")
lines = file.readlines()
total = 0
for line in lines:
    set1 = set(line[:len(line)//2])
    set2 = set(line[len(line)//2:])
    i = (set1 & set2).pop()
    if i.isupper():
        total += ord(i) - 38
    else:
        total += ord(i) - 96
print(total)
