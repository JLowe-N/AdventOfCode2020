def parseInput(filename):
    input = []
    with open(filename) as reader:
        for line in reader:
            data = (line.strip('\n'))
            direction, distance = data[0], data[1:]
            input.append((direction, distance))
    input.sort()
    return input


example = parseInput('example.txt')
input = parseInput('input.txt')

def myFunc():
    pass

print(myFunc())
print(input)