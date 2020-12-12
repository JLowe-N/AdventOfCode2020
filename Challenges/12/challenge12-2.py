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
    waypointX = 10
    waypointY = 1
    shipX = 0
    shipY = 0
    
    for instruction, distance in input:
        print(f'{waypointX} {waypointY} {shipX} {shipY}')
        if instruction == 'R':
            waypointX, waypointY = rotateWaypoint(distance, 'R', waypointX, waypointY)
            continue
        elif instruction == 'L':
            waypointX, waypointY = rotateWaypoint(distance, 'L', waypointX, waypointY)
            continue
        else:
            if instruction == 'F':
                shipX += waypointX * distance
                shipY += waypointY * distance
            else:
                direction = instruction
                if direction == 'N':
                    waypointY += distance
                if direction == 'S':
                    waypointY -= distance
                if direction == 'E':
                    waypointX += distance
                if direction == 'W':
                    waypointX -= distance
        pprint(f'instruction, distance')
    return (abs(shipX) + abs(shipY))
            
def rotateWaypoint(rotation, direction, waypointX, waypointY):
    if direction == 'L':
        if rotation == 90:
            newX = -waypointY
            newY = waypointX
        if rotation == 180:
            newX = -waypointX
            newY = - waypointY
        if rotation == 270:
            newX = waypointY
            newY = -waypointX
    elif direction == 'R':
        if rotation == 270:
            newX = -waypointY
            newY = waypointX
        if rotation == 180:
            newX = -waypointX
            newY = - waypointY
        if rotation == 90:
            newX = waypointY
            newY = -waypointX
    return (newX, newY)
     


pprint(myFunc(input))
# pprint(input)
