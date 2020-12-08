from pprint import pprint
input = []
with open('input.txt') as reader:
    for line in reader:
        instruction = line.strip('\n')
        action, value = instruction.split()
        value = int(value)
        input.append((action, value))
# pprint(input)

def getAccValuePriorToLoop(instructions):
    numInstructions = len(instructions)
    accumulator = 0
    visited = {}
    currentPosition = 0
    nextPosition = None
    while currentPosition not in visited:
        visited[currentPosition] = True
        action, value = instructions[currentPosition]
        if currentPosition + value == numInstructions:
            break
        if action == 'nop':
            nextPosition = currentPosition + 1
        if action == 'acc':
            nextPosition = currentPosition + 1
            accumulator += value
        if action == 'jmp':
            nextPosition = (currentPosition + value)

        if nextPosition == numInstructions:
            break

        nextPosition = nextPosition % numInstructions
        currentPosition = nextPosition
    return accumulator

def getInstructionSequence(instructions):
    numInstructions = len(instructions)
    accumulator = 0
    instructionSeq = []
    visited = {}
    currentPosition = 0
    nextPosition = None
    while currentPosition not in visited:
        visited[currentPosition] = True
        instructionSeq.append(currentPosition)
        action, value = instructions[currentPosition]
        if action == 'nop':
            nextPosition = currentPosition + 1
        if action == 'acc':
            nextPosition = currentPosition + 1
            accumulator += value
        if action == 'jmp':
            nextPosition = (currentPosition + value)
        
        if nextPosition == numInstructions:
            instructionSeq.append(nextPosition)
            break

        nextPosition = nextPosition % numInstructions
        currentPosition = nextPosition
    return instructionSeq

def rewriteInstructions(instructions, sequence):
    newInstructions = instructions[:]
    lastPosition = None
    lastAction = None
    lastValue = None
    while lastAction is None or lastAction == 'acc':
        lastPosition = sequence.pop()
        lastAction, lastValue = instructions[lastPosition]
    newAction = 'nop' if lastAction == 'jmp' else 'jmp'
    newInstructions[lastPosition] = (newAction, lastValue)
    print(f'Changing instruction at {lastPosition} to {lastAction} {lastValue}')
    return newInstructions

def isValidInstructions(instructions, sequence):
    return sequence[-1] == len(instructions)

originalSequence = getInstructionSequence(input)
currentTestSequence = originalSequence
currentInstructions = input
while not isValidInstructions(currentInstructions, currentTestSequence):
    print('testing new instruction set')
    currentInstructions = rewriteInstructions(input, originalSequence)
    currentTestSequence = getInstructionSequence(currentInstructions)
print(getAccValuePriorToLoop(currentInstructions))

