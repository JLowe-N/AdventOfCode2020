def parseInput(filename):
    data = []
    with open(filename) as file:
        linenum = 0
        for line in file:
            line = line.strip('\n')
            data = [int(num) for num in line.split(',')]
            
            linenum += 1
    return data


example = parseInput('example.txt')
input = parseInput('input.txt')

def myFunc(startingNums):
    targetSeqNum = 2020
    prevNum = None
    spokenNum = None
    cache = {}
    for i in range(targetSeqNum):
        turn = i + 1
        prevNum = spokenNum
        if i < len(startingNums):
            spokenNum = startingNums[i]
            cache[prevNum] = turn - 1
        else:
            if prevNum in cache.keys():
                spokenNum = turn - 1 - cache[prevNum]
                cache[prevNum] = turn - 1
            else:
                spokenNum = 0
                cache[prevNum] = turn - 1
        # print(cache)
    return spokenNum


print(myFunc(input))