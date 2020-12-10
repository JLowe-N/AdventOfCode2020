from pprint import pprint


def parseInput(filename):
    input = []
    with open(filename) as reader:
        for line in reader:
            data = int(line.strip('\n'))
            input.append(data)
    input.sort()
    return input


example = parseInput('example.txt')
input = parseInput('input.txt')


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


print(myFunc(input))
print(66 * 29)
