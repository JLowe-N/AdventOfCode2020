from pprint import pprint

def parseInput(filename):
    input = []
    with open(filename) as reader:
        for line in reader:
            data = line.strip('\n')
            data = data.replace('L', '#')
            data = [letter for letter in data]
            input.append(data)
    return input


example = parseInput('example.txt')
input = parseInput('input.txt')

def fillSeats(plane):
    nextPlane = []
    for i in range(len(plane)):
        nextPlane.append([])
        for j in range(len(plane[0])):
            occupiedAdj = 0
            if plane[i][j] == '.':
                nextStep = '.'
            else:
                y = 1 
                z = 1 
                while i - y >= 0:
                    
                    if plane[i - y][j] == '#':
                        occupiedAdj += 1
                        break
                    elif plane[i - y][j] == 'L':
                        break
                    y += 1 
                    z += 1 

                y = 1 
                z = 1 
                while j - z >= 0:
                    if plane[i][j - z] == '#':
                        occupiedAdj += 1
                        break
                    elif plane[i][j - z] == 'L':
                        break
                    y += 1 
                    z += 1 

                y = 1
                z = 1
                while i - y >= 0 and j - z >= 0:
                    if plane[i - y][j - z] == '#':
                        occupiedAdj += 1
                        break
                    elif plane[i - y][j - z] == 'L':
                        break
                    y += 1
                    z += 1

                y = 1 
                z = 1 
                while i + y < len(plane):

                    if plane[i + y][j] == '#':
                        occupiedAdj += 1
                        break
                    elif plane[i + y][j] == 'L':
                        break
                    y += 1 
                    z += 1 

                y = 1 
                z = 1 
                while j + z < len(plane[0]):
                    if plane[i][j + z] == '#':
                        occupiedAdj += 1
                        break
                    elif plane[i][j + z] == 'L':
                        break
                    y += 1 
                    z += 1 

                y = 1
                z = 1
                while i + y < len(plane) and j + z < len(plane[0]):
                    if plane[i + y][j + z] == '#':
                        occupiedAdj += 1
                        break
                    elif plane[i + y][j + z] == 'L':
                        break
                    y += 1
                    z += 1

                y = 1
                z = 1
                while i + y < len(plane) and j - z >= 0:
                    if plane[i + y][j - z] == '#':
                        occupiedAdj += 1
                        break
                    elif plane[i + y][j - z] == 'L':
                        break
                    y += 1
                    z += 1

                y = 1 
                z = 1 
                while i - y >= 0 and j + z < len(plane[0]):
                    if plane[i - y][j + z] == '#':
                        occupiedAdj += 1
                        break
                    elif plane[i - y][j + z] == 'L':
                        break
                    y += 1 
                    z += 1 

                if plane[i][j] == '#':
                    if occupiedAdj >= 5:
                        nextStep = 'L'
                    else:
                        nextStep = '#'
                if plane[i][j] == 'L':
                    if occupiedAdj == 0:
                        nextStep = '#'
                    else:
                        nextStep = 'L'
            # print(f'occupied {occupiedAdj} for {i} {j}: {nextStep}')
            nextPlane[i].append(nextStep)
    # pprint(nextPlane)
    return nextPlane

# def emptySeats(plane):
#     nextPlane = None
    
#     if nextPlane:
#         plane = nextPlane
#     nextPlane = []
#     for i in range(len(plane)):
#         nextPlane.append([])
#         for j in range(len(plane[0])):
#             occupiedAdj = 0
#             if plane[i][j] == '.':
#                 nextStep = '.'
#             else:
#                 if i - 1 > 0:
#                     if plane[i - 1][j] == '#':
#                         occupiedAdj += 1
#                 if j - 1 > 0:
#                     if plane[i][j - 1] == '#':
#                         occupiedAdj += 1
#                 if i - 1 > 0 and j - 1 > 0:
#                     if plane[i - 1][j - 1] == '#':
#                         occupiedAdj += 1
#                 if i + 1 < len(plane):
#                     if plane[i + 1][j] == '#':
#                         occupiedAdj += 1
#                 if j + 1 < len(plane[0]):
#                     if plane[i][j + 1] == '#':
#                         occupiedAdj += 1
#                 if i + 1 < len(plane) and j + 1 < len(plane[0]):
#                     if plane[i + 1][j + 1] == '#':
#                         occupiedAdj += 1
#                 if i + 1 < len(plane) and j - 1 > 0:
#                     if plane[i + 1][j - 1] == '#':
#                         occupiedAdj += 1
#                 if i - 1 > 0 and j + 1 < len(plane[0]):
#                     if plane[i - 1][j + 1] == '#':
#                         occupiedAdj += 1
#                 if occupiedAdj < 4:
#                     nextStep = '#'
#                 else:
#                     nextStep = 'L'
#             print(f'occupied {occupiedAdj} for {i} {j}: {nextStep}')
#             nextPlane[i].append(nextStep)
#     pprint(nextPlane)
#     return nextPlane

def cycleSeats(plane):
    currentPlane = plane
    for _ in range(1):
        # print('fill')
        filledPlane = fillSeats(currentPlane)
        currentPlane = filledPlane
    return currentPlane

def countOccSeats(plane):
    occupied = 0
    for row in plane:
        for seat in row:
            if seat == '#':
                occupied += 1
    return occupied

prevSeats = 0
nextSeats = None
currentPlane = input
while prevSeats != nextSeats:
    currentPlane = cycleSeats(currentPlane)
    prevSeats = nextSeats
    nextSeats = countOccSeats(currentPlane)
print(nextSeats)
    