file = open("input.txt", "r")
crates = open("input2.txt", "r")
stacks = [[], [], [], [], [], [], [], [], []]
cratelines = crates.readlines()
cratelines.reverse()
for line in cratelines:
    for i in range(9):
        index = i * 4 + 1
        if len(line) > index:
            character = line[index]
            if character != " ":
                stacks[i].append(character)
filelines = file.readlines()
for line in filelines:
    lineparts = line.split(" ")
    buffer = []
    for i in range(int(lineparts[1])):
        buffer.append(stacks[int(lineparts[3]) - 1].pop())
    for j in range(int(lineparts[1])):
        stacks[int(lineparts[5]) - 1].append(buffer.pop())
for a in range(9):
    print(stacks[a].pop(), end = '')

        
