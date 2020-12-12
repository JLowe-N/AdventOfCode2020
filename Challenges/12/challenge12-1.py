from pprint import pprint


def parseInput(filename):
    input = []
    with open(filename) as reader:
        for line in reader:
            data = (line.strip('\n'))
            direction, distance = data[0], data[1:]
            distance = int(distance)
            input.append((direction, distance))
    return input


example = parseInput('example.txt')
input = parseInput('input.txt')

def myFunc(input):
    startX = 0
    startY = 0
    map = ['N', 'E', 'S', 'W']

    currentDirection = 'E'
    for instruction, distance in input:
        if instruction == 'R':
            
            currentIdx = map.index(currentDirection)
            turnStep = distance // 90
            nextIdx = (currentIdx + turnStep) % 4
            currentDirection = map[nextIdx]
            print(f'{instruction}, {distance}')
            print(f'{currentIdx} {turnStep} {nextIdx} {currentDirection}')
            continue
        elif instruction == 'L':
            currentIdx = map.index(currentDirection)
            turnStep = distance // 90
            nextIdx = (currentIdx - turnStep) % 4
            currentDirection = map[nextIdx]
            print(f'{instruction}, {distance}')
            print(f'{currentIdx} {turnStep} {nextIdx} {currentDirection}')
            continue
        else:
            if instruction == 'F':
                direction = currentDirection
            else:
                direction = instruction
            if direction == 'N':
                startY += distance
            if direction == 'S':
                startY -= distance
            if direction == 'E':
                startX += distance
            if direction == 'W':
                startX -= distance
    return (abs(startX) + abs(startY))
            
        


pprint(myFunc(input))
# pprint(input)
