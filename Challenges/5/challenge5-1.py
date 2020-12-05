'''
Binary Boarding Passes
Scan through all the tickets in the input, and find an available seat.
Plane has 128 rows (numbered 0 through 127) and 8 columns (0 through 7).
Boarding pass of format FBFBBFFRLR, whhere:
Each letter splits the remaining rows to the front or back
and splits the remaining columns to left or right
until only 1 seat remains - this is the seat for that boarding pass.

F for lower indexes closer to 0, B means higher indexes towards the end of the array.

Each seat corresponds to a unique seat ID:
Multiply row by 8, then add the column
'''
import math

input = []
with open('input.txt') as reader:
    for line in reader:
        input.append(line.rstrip('\n'))

def getSeatId(binaryBoardingPass):
    minRow = 1
    maxRow = 128
    minCol = 1
    maxCol = 8
    for seatCode in binaryBoardingPass:
        # print(f'minRow {minRow} maxRow {maxRow} minCol {minCol} maxCol {maxCol} pass {binaryBoardingPass}')
        if seatCode == 'F':
            maxRow = math.floor(maxRow - (maxRow - minRow) / 2) 
        elif seatCode == 'B':
            minRow = math.ceil((maxRow - minRow) / 2 + minRow)
        elif seatCode == 'L':
            maxCol = math.floor(maxCol - (maxCol - minCol) / 2)
        elif seatCode == 'R':
            minCol = math.ceil((maxCol - minCol) / 2 + minCol)
        else:
            print('Invalid Seat Code!')
    # print(f'Final: minRow {minRow} maxRow {maxRow} minCol {minCol} maxCol {maxCol} pass {binaryBoardingPass}')
    if minRow == maxRow and minCol == maxCol:
        rowIdx = maxRow - 1
        colIdx = maxCol - 1
        seatId = rowIdx * 8 + colIdx
        return seatId
    else:
        ('Something went wrong!')

maxSeatId = float("-inf")
for binaryBoardingPass in input:
    currentSeatId = getSeatId(binaryBoardingPass)
    if currentSeatId > maxSeatId:
        maxSeatId = currentSeatId
print(maxSeatId)



