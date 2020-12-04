from pprint import pprint
input = []
with open('input.txt') as reader:
    for line in reader:
        input.append(line.rstrip('\n'))

def traverseAndCountTrees(repeatingPath, stepsRight, stepsDown):
    treeCount = 0
    colLength = len(repeatingPath[0])
    goalRowIdx = len(repeatingPath)
    print(colLength, goalRowIdx)
    colIdx = 0
    rowIdx = 0
    while (rowIdx != goalRowIdx):
        nextColIdx = colIdx + stepsRight if colIdx + stepsRight < colLength else (colIdx + stepsRight) % colLength
        nextRowIdx = rowIdx + stepsDown
        pathMarker = repeatingPath[rowIdx][colIdx]
        print(rowIdx, colIdx, pathMarker)
        if pathMarker == '#':
            treeCount += 1
        rowIdx = nextRowIdx
        colIdx = nextColIdx
        

    return treeCount

print(traverseAndCountTrees(input, 3, 1))
        


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
