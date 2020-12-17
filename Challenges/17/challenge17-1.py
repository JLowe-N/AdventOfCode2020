from pprint import pprint
import copy

def parseInput(filename):
    activeHash = {}
    with open(filename) as file:
        linenum = 0
        for line in file:
            for idx, char in enumerate(line.strip('\n')):
                if char == '#':
                    activeHash[(linenum, idx, 0)] = True
            linenum += 1
        # pprint(activeHash)
    return activeHash


example = parseInput('example.txt')
input = parseInput('input.txt')

def countActiveNeighbors(activeHash, xyzTuple):
    activeNeighbors = 0
    for xOffset in range(-1, 2):
        for yOffset in range(-1, 2):
            for zOffset in range(-1, 2):
                if (xOffset, yOffset, zOffset) == (0, 0, 0):
                    continue
                neighborXYZ = (xyzTuple[0] + xOffset, xyzTuple[1] + yOffset, xyzTuple[2] + zOffset,)
                if neighborXYZ in activeHash:
                    activeNeighbors += 1
    return activeNeighbors


def pocketDimensionCycle(activeHash, numCycles):
    minX = minY = minZ = float("inf")
    maxX = maxY = maxZ = float("-inf")
    for xyz in activeHash.keys():
        if xyz[0] < minX:
            minX = xyz[0]
        if xyz[1] < minY:
            minY = xyz[1]
        if xyz[2] < minZ:
            minZ = xyz[2]
        if xyz[0] > maxX:
            maxX = xyz[0]
        if xyz[1] > maxY:
            maxY = xyz[1]
        if xyz[2] > maxZ:
            maxZ = xyz[2]
    currentHash = copy.copy(activeHash)
    
    for _ in range(numCycles):
        workingHash = copy.copy(currentHash)
        for x in range(minX - 1, (maxX + 1) + 1):
            for y in range(minY - 1, (maxY + 1) + 1):
                for z in range(minZ - 1, (maxZ + 1) + 1):
                    activeNeighborCount = countActiveNeighbors(currentHash, (x, y, z))
                    wasActive = False if (x, y, z) not in currentHash.keys() else True
                    if wasActive:
                        if activeNeighborCount == 2 or activeNeighborCount == 3:
                            workingHash[(x, y, z)] = True
                        else:
                            workingHash.pop((x, y, z), None)
                    else:
                        if activeNeighborCount == 3:
                            workingHash[(x, y, z)] = True
                        else:
                            workingHash.pop((x, y, z), None)
        minX, minY, minZ = (minX - 1, minY - 1, minZ - 1)
        maxX, maxY, maxZ = (maxX + 1, maxY + 1, maxZ + 1)
        currentHash = workingHash
    return currentHash
                            

print(len(pocketDimensionCycle(input, 6)))