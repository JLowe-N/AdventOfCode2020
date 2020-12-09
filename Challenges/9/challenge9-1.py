from pprint import pprint
input = []
with open('input.txt') as reader:
    for line in reader:
        data = int(line.strip('\n'))
        input.append(data)

example = []
with open('example.txt') as reader2:
    for line in reader2:
        data = int(line.strip('\n'))
        example.append(data)

def parseInput(filename):
    list = []
    with open(filename) as reader:
        for line in reader:
            data = line.strip('\n')
            input.append(data)
    return list

def movingWindow25Sum(input):
    startIdx = 0
    endIdx = 24
    currentIdx = 25
    isValidNumber = True
    while currentIdx < len(input) and isValidNumber:
        isValidNumber= False
        for i in range(startIdx, endIdx + 1):
            for j in range(i + 1, endIdx + 1):
                # print(i, j, currentIdx)
                # print(input[i], input[j])
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
    

invalidNumber = movingWindow25Sum(input)
rangeData = findIdxRangeForTargetSum(input, invalidNumber)

print(rangeData["min"] + rangeData["max"])

# print(movingWindow25Sum(example))
                
