from pprint import pprint
import functools

input = []
with open('input.txt') as reader:
    for line in reader:
        input.append(line.rstrip('\n'))

def traverseAndCountTrees(repeatingPath, stepsRight, stepsDown):
    print("Traversing:", stepsRight, stepsDown)
    treeCount = 0
    colLength = len(repeatingPath[0])
    goalRowIdx = len(repeatingPath)
    colIdx = 0
    rowIdx = 0
    while (rowIdx < goalRowIdx):
        nextColIdx = colIdx + stepsRight if colIdx + stepsRight < colLength else (colIdx + stepsRight) % colLength
        nextRowIdx = rowIdx + stepsDown
        pathMarker = repeatingPath[rowIdx][colIdx]
        if pathMarker == '#':
            treeCount += 1
        rowIdx = nextRowIdx
        colIdx = nextColIdx
        

    return treeCount

# Slope Array (stepsRight, stepsDown)
slopesList = [[1, 1], [3, 1], [5, 1], [7, 1], [1,2]]

def checkSlopes(slopesList):
    treeCounts = []
    for slope in slopesList:
        treeCount = traverseAndCountTrees(input, slope[0], slope[1])
        treeCounts.append(treeCount)
    return treeCounts
        
treeCounts = checkSlopes(slopesList)
print(treeCounts)
slopesMult = functools.reduce((lambda x, y: x * y), treeCounts)

print(slopesMult)
        


#if hit rules change to hit all trees on every step - 
# while (colIdx != nextColIdx):
#     pathMarker = repeatingPath[rowIdx][colIdx]
#     if pathMarker == '#':
#         treeCount += 1
#     colIdx = (colIdx + 1) % colLength
# while (rowIdx != nextRowIdx and rowIdx != goalRowIdx):
#     pathMarker = repeatingPath[rowIdx][colIdx]
#     if pathMarker == '#':
#         treeCount += 1
#     rowIdx += 1
