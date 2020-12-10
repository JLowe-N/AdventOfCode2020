from pprint import pprint
from math import prod, comb


def parseInput(filename):
    input = []
    with open(filename) as reader:
        for line in reader:
            data = int(line.strip('\n'))
            input.append(data)
    input.sort()
    return input


example = parseInput('example.txt')
example2 = parseInput('example2.txt')
input = parseInput('input.txt')

input.insert(0, 0)
input.append(input[-1] + 3)
example.insert(0, 0)
example.append(example[-1] + 3)
example2.insert(0, 0)
example2.append(example2[-1] + 3)

def myFunc(adapters):
    currentJolt = 0
    numOneJoltDiff = 0
    numThreeJoltDiff = 1
    for rating in adapters:
        if rating - currentJolt == 1:
            numOneJoltDiff += 1
        elif rating - currentJolt == 3:
            numThreeJoltDiff += 1
        else:
            print("oops")
        currentJolt = rating
    return (numOneJoltDiff, numThreeJoltDiff)



def isValidAdapterSeq(adapters):
    for i in range(len(adapters) - 1):
        if adapters[i + 1] - adapters[i] <= 3:
            continue
        else:
            return 0
    print(adapters)
    return 1

def testAllPaths(input, startIdx=1, seq=[0]):
    # print(seq)
    validPaths = 0
    if seq[-1] == input[-1]:
        # print(seq)
        return 1
    for i in range(startIdx, len(input)):
        if input[i] - seq[-1] <= 3:
            validAdapter = input[i]
            newSeq = seq[:]
            newSeq.append(validAdapter)
            validPaths += testAllPaths(input, i + 1, newSeq)
        else:
            break
    return validPaths

def auxArrays(input):
    leftwiseDiff = []
    for i in range(1, len(input)):
        leftwiseDiff.append(input[i] - input[i - 1])
    print(leftwiseDiff)
    return leftwiseDiff

leftwiseDiff = auxArrays(input)

def countCombos(diffArray):
    group_lengths = []
    numOnes = 0
    for number in diffArray:
        if number == 1:
            numOnes += 1
        
        if number == 3 and numOnes > 0:
            group_lengths.append(numOnes)
            numOnes = 0
    if numOnes > 0:
        group_lengths.append(numOnes)
    return group_lengths
        
group_lengths= countCombos(leftwiseDiff)
print(group_lengths)
print(prod([1 + comb(length - 1, 1) + comb(length - 1, 2) for length in group_lengths]))
