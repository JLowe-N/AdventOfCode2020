from pprint import pprint
import copy

def parseInput(filename):
    activeHash = {}
    with open(filename) as file:
        linenum = 0
        for line in file:
            for idx, char in enumerate(line.strip('\n')):
                if char == '#':
                    activeHash[(linenum, idx, 0, 0)] = True
            linenum += 1
        # pprint(activeHash)
        # activeHash[(x, y, z, w)] = True | null
    return activeHash


example = parseInput('example.txt')
input = parseInput('input.txt')

def countActiveNeighbors(activeHash, xyzwTuple):
    # Currently counting neighbors more than once for adjacent elements
    # May be more efficient way to implement
    activeNeighbors = 0
    for xOffset in range(-1, 2):
        for yOffset in range(-1, 2):
            for zOffset in range(-1, 2):
                for wOffset in range(-1, 2):
                    if (xOffset, yOffset, zOffset, wOffset) == (0, 0, 0, 0):
                        continue
                    neighborXYZW = (xyzwTuple[0] + xOffset, xyzwTuple[1] + yOffset, xyzwTuple[2] + zOffset, xyzwTuple[3] + wOffset)
                    if neighborXYZW in activeHash:
                        activeNeighbors += 1
    return activeNeighbors


def pocketDimensionCycle(activeHash, numCycles):
    # Likely can use a map/reduce here to consolidate
    # or helper function to improve readability
    # min/max for z and w irrelevant, since always initialize with (0, 0) z, w input
    minX = minY = minZ = minW = float("inf")
    maxX = maxY = maxZ = maxW = float("-inf")
    for xyzw in activeHash.keys():
        if xyzw[0] < minX:
            minX = xyzw[0]
        if xyzw[1] < minY:
            minY = xyzw[1]
        if xyzw[2] < minZ:
            minZ = xyzw[2]
        if xyzw[3] < minW:
            minW = xyzw[3]
        if xyzw[0] > maxX:
            maxX = xyzw[0]
        if xyzw[1] > maxY:
            maxY = xyzw[1]
        if xyzw[2] > maxZ:
            maxZ = xyzw[2]
        if xyzw[3] > maxW:
            maxW = xyzw[3]
    currentHash = copy.copy(activeHash)
    
    for _ in range(numCycles):
        workingHash = copy.copy(currentHash)
        for x in range(minX - 1, (maxX + 1) + 1):
            for y in range(minY - 1, (maxY + 1) + 1):
                for z in range(minZ - 1, (maxZ + 1) + 1):
                    for w in range(minW - 1, (maxW + 1) + 1):
                        activeNeighborCount = countActiveNeighbors(currentHash, (x, y, z, w))
                        wasActive = False if (x, y, z, w) not in currentHash.keys() else True
                        if wasActive:
                            if activeNeighborCount == 2 or activeNeighborCount == 3:
                                workingHash[(x, y, z, w)] = True
                            else:
                                workingHash.pop((x, y, z, w), None)
                        else:
                            if activeNeighborCount == 3:
                                workingHash[(x, y, z, w)] = True
                            else:
                                workingHash.pop((x, y, z, w), None)
        minX, minY, minZ, minW = (minX - 1, minY - 1, minZ - 1, minW - 1)
        maxX, maxY, maxZ, maxW = (maxX + 1, maxY + 1, maxZ + 1, maxW + 1)
        currentHash = workingHash
    return currentHash
                            

print(len(pocketDimensionCycle(example, 6)))