from pprint import pprint

def parseInput(filename):
    input = []
    with open(filename) as reader:
        for line in reader:
            data = int(line.strip('\n'))
            input.append(data)
    return input

def getElementWithoutSumInMovingWindow(input, windowSize):
    startIdx = 0
    endIdx = windowSize - 1
    currentIdx = endIdx + 1
    isValidNumber = True
    while currentIdx < len(input) and isValidNumber:
        isValidNumber= False
        for i in range(startIdx, endIdx + 1):
            for j in range(i + 1, endIdx + 1):
                if input[i] + input[j] == input[currentIdx]:
                    isValidNumber = True
        if not isValidNumber:
            return input[currentIdx]
        startIdx += 1
        endIdx += 1
        currentIdx += 1
    return input[currentIdx]

def findIdxRangeForTargetSum(input, target):
    for i in range(len(input)):
        minValueInRange = input[i]
        maxValueInRange = input[i]
        currentSum = input[i]
        for j in range(i + 1, len(input)):
            currentSum += input[j]
            if input[j] < minValueInRange:
                minValueInRange = input[j]
            if input[j] > maxValueInRange:
                maxValueInRange = input[j]
            if currentSum > target:
                break
            elif currentSum == target:
                rangeData = {
                    "startIdx": i,
                    "endIdx": j,
                    "min": minValueInRange,
                    "max": maxValueInRange,
                    }
                return rangeData
    print("No range with target sum found")
    

input = parseInput('input.txt')
example = parseInput('example.txt')

invalidNumber = getElementWithoutSumInMovingWindow(input, windowSize=25)
rangeData = findIdxRangeForTargetSum(input, invalidNumber)

# Part 2 Goal - find range that sums to invalid number from Part 1
# Then return sum of min and max of that range.
print(rangeData["min"] + rangeData["max"])
                
