file = open("input.txt", "r")
lines = file.readlines()
matrix = []
for line in lines:
    row = []
    for i in line.strip():
        row.append(int(i))
    matrix.append(row)

def part1():
    visible = len(matrix) * 2 + len(matrix[0]) * 2 - 4
    for row in range(1, len(matrix) - 1):
        for column in range(1, len(matrix[row]) - 1):
            if check_visible(row, column):
                visible += 1
    return visible
                


def check_visible(y, x):
    treevalue = matrix[y][x]
    highest = 0 
    for i in range(y):
        if matrix[i][x] > highest:
            highest = matrix[i][x]
    if highest < treevalue:
        return True
    highest = 0
    for i in range(x):
        if matrix[y][i] > highest:
            highest = matrix[y][i]
    if highest < treevalue:
        return True
    highest = 0
    for i in range(y+1, len(matrix)):
        if matrix[i][x] > highest:
            highest = matrix[i][x]
    if highest < treevalue:
        return True
    highest = 0
    for i in range(x + 1, len(matrix)):
        if matrix[y][i] > highest:
            highest = matrix[y][i]
    if highest < treevalue:
        return True
    return False

def part2():
    highest = 0
    for y in range(len(matrix)):
        for x in range(len(matrix)):
            treeheight = matrix[y][x]
            scenery = 1
            total = 0
            for i in range(y - 1, -1, -1):
                total += 1
                if matrix[i][x] >= treeheight:
                    break
            scenery *= total
            total = 0
            for i in range(y + 1, len(matrix)):
                total += 1
                if matrix[i][x] >= treeheight:
                    break
            scenery *= total
            total = 0
            for i in range(x - 1, -1, -1):
                total += 1
                if matrix[y][i] >= treeheight:
                    break
            scenery *= total
            total = 0
            for i in range(x + 1, len(matrix)):
                total += 1
                if matrix[y][i] >= treeheight:
                    break
            scenery *= total

            if scenery > highest:
                highest = scenery
    return highest
print(part1())
print(part2())


