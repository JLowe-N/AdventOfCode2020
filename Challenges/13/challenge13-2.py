def parseInput(filename):
    with open(filename) as file:
        linenum = 1
        for line in file:
            if linenum == 2:
                return [int(x) if x.isdigit() else x for x in line.split(',')]
            linenum += 1


example = parseInput('example.txt')
input = parseInput('input.txt')

def myFunc(data):
    print(data)
    buses = [x for x in data if type(x) is int]
    mods = [-i%v for i, v in enumerate(data) if v != 'x']
    x, step = 0, 1
    for d, r  in zip(buses, mods):
        while x % d != r:
            x += step
        step *= d
    return x

print(myFunc(input))
                
    

    