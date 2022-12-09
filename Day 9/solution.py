#
def move(x, y, vector):
    x[0] += vector[0]
    y[0] += vector[1]
    # Copied this part from the internet, turns out my own code was fine but now I can't get it back.
    for i in range(1, len(x)):
        dx = x[i] - x[i - 1]
        dy = y[i] - y[i - 1]
        if abs(dx) == 2 or abs(dy) == 2:
            x[i] = x[i - 1] + int(dx / 2)
            y[i] = y[i - 1] + int(dy / 2)

def positions(ropesize):
    x = [0] * ropesize
    y = [0] * ropesize
    file = open("input.txt", "r")
    lines = file.readlines()
    positionset = {(0, 0)}
    for line in lines:
        direction = line[0]
        steps = int(line[1:])
        match direction:
            case 'U':
                vector = (0, 1)
            case 'D':
                vector = (0, -1)
            case 'R':
                 vector = (1, 0)
            case 'L':
                vector = (-1, 0)
            case other:
                vector = (0, 0)
        for _ in range(steps):
            move(x, y, vector)
            positionset.add((x[-1], y[-1]))
    return positionset


def visualize(positionset):
    result = ""
    for i in range(-100, 100):
        for j in range(-100, 100):
            if(j, -i) in positionset:
                result += '#'
            else:
                result += '.'
        result += '\n'
    return result


#print(visualize(positions(2)))
print(len(positions(2)))
print(len(positions(10)))
