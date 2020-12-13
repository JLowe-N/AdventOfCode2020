def parseInput(filename):
    startTime = 0
    busList = []
    with open(filename) as reader:
        lineNum = 0
        for line in reader:
            lineNum += 1
            data = (line.strip('\n'))
            if lineNum == 1:
                startTime = int(data)
            if lineNum == 2:
                busList = data.split(',')
                busList = [int(element) for element in busList if element != 'x']
    return (startTime, busList)


example = parseInput('example.txt')
input = parseInput('input.txt')

def myFunc(startTime, busList):
    closestArrivalTimes = [element - startTime % element for element in busList]
    waitingTime = min(closestArrivalTimes)
    targetBusIdx = closestArrivalTimes.index(waitingTime)
    targetBus = busList[targetBusIdx]
    return targetBus * waitingTime


print(myFunc(input[0], input[1]))
print(myFunc(example[0], example[1]))
print(input)