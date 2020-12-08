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
        if action == 'nop':
            nextPosition = currentPosition + 1
        if action == 'acc':
            nextPosition = currentPosition + 1
            accumulator += value
        if action == 'jmp':
            nextPosition = (currentPosition + value) % numInstructions
        currentPosition = nextPosition
    return accumulator

print(getAccValuePriorToLoop(input))

