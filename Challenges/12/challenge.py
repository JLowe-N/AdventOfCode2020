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

def myFunc():
    pass

print(myFunc())