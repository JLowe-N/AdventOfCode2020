from pprint import pprint

memHash = {}
def myFunc(mask, data):
    # print(mask)
    for memIdx, value in data:
        if memIdx in memHash.keys():
            print(f'Overwriting {memIdx} with {value}')
        binaryStr = '{:036b}'.format(value)
        # print(binaryStr)
        maskedVal = ''
        for i in range(len(mask)):
            if mask[i] == 'X':
                maskedVal += binaryStr[i]
            elif mask[i] == '1' or mask[i] == '0':
                maskedVal += mask[i]
            else:
                print(mask[i])
                print("oh no!")
        # print(mask)
        # print(binaryStr)
        # print(maskedVal)
        # print(int(maskedVal, 2))
        memHash[memIdx] = int(maskedVal, 2)
        # print(memHash[memIdx])
        
def sumDict(dict):
    sum = 0
    for value in dict.values():
        sum += value
    return sum


def parseInput(filename):
    data = []
    with open(filename) as file:
        mask = None
        linenum = 0
        for line in file:
            if line.startswith('mask'):
                # print(f'mask at {linenum}')
                if len(data) > 0:
                    # print(mask, data)
                    myFunc(mask, data)
                _, mask = line.strip('\n').split(' = ')
                data = []
            else:
                # print(f'data at {linenum}')
                line = line.strip('\n')
                memIdx, value = line.split(' = ')
                memIdx = memIdx.lstrip('mem[')
                memIdx = int(memIdx.rstrip(']'))
                value = int(value)
                data.append((memIdx, value))
            linenum += 1
        if len(data) > 0:
            myFunc(mask, data)
            data = []

    return (mask, data)


parseInput('input.txt')
# input = parseInput('input.txt')
# pprint(memHash)
print(sumDict(memHash))