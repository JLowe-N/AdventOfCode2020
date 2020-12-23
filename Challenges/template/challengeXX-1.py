def parseInput(filename):
    data = []
    with open(filename) as file:
        linenum = 0
        for line in file:
            line = line.strip('\n')
            data.append(line)
            linenum += 1
    return data


example = parseInput('example.txt')
input = parseInput('input.txt')

def myFunc(startTime, busList):
    pass


print(myFunc)