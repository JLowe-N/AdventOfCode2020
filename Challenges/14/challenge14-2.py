from pprint import pprint

memHash = {}
def myFunc(mask, data):
    # print(mask)
    for memIdx, value in data:
        floatCount = 0
        floatIdx = []
        binaryIdx = '{:036b}'.format(memIdx)
        # print(binaryStr)
        maskedVal = []
        # print(mask)
        # print(binaryIdx)
        for i in range(len(mask)):
            # print(maskedVal)
            if mask[i] == 'X':
                maskedVal.append('X')
                floatCount += 1
                floatIdx.append(i)
            elif mask[i] == '0':
                maskedVal.append(binaryIdx[i])
            elif mask[i] == '1':
                maskedVal.append(mask[i])
            else:
                print(mask[i])
                print("oh no!")
        if floatCount > 0:
            replaceValue = 0
            # print()
            # print("".join(maskedVal))
            # print(range(2 ** floatCount))
            for i in range(2 ** floatCount):
                # print(i)
                replaceString = '{:036b}'.format(replaceValue)
                for j in reversed(range(floatCount)):
                    replaceIdx = floatIdx[-1 - j]
                    maskedVal[replaceIdx] = replaceString[-1 - j]
                # print("".join(maskedVal))
                newMemIdx = int("".join(maskedVal),2)
                memHash[newMemIdx] = value
                replaceValue += 1
        else:
        # print(mask)
        # print(binaryStr)
        # print(maskedVal)
        # print(int(maskedVal, 2))
            memHash[int("".join(maskedVal), 2)] = value
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