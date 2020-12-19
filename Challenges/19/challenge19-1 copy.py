from pprint import pprint

def parseInput(filename):
    data = []
    hashRules = {}
    with open(filename) as file:
        linenum = 0
        sectionNum = 0
        for line in file:
            if line.isspace():
                sectionNum += 1
                continue
            elif sectionNum == 0:
                key, values = line.strip('\n').replace('"', '').split(': ')
                if any(value.isdigit() for value in values):
                    hashRules[key] = [value.split(' ') for value in values.split(' | ')]
                else:
                    hashRules[key] = values
            elif sectionNum == 1:
                line = line.strip('\n')
                data.append(line)
                linenum += 1
            else:
                print('unexpected sections in input')
    pprint(data)
    pprint(hashRules)
    return (data, hashRules)


example = parseInput('example.txt')
# input = parseInput('input.txt')


def flattenRules(rulesHash):
    for ruleKey, rule in rulesHash.items():
        for optionIdx, ruleOption in enumerate(rule):
            for charIdx, char in enumerate(ruleOption):
                # print(f'{ruleKey} {optionIdx} {charIdx}')
                # print(char)
                if char.isalpha():
                    continue
                elif char.isnumeric():
                    nestedRules = rulesHash[char]
                    rulesHash[ruleKey][optionIdx][charIdx] = nestedRules
    pprint(rulesHash)
    return rulesHash                

flattenHash = flattenRules(example[1])

def validateAgainstRule0(rule, message, nesting=0, idx=0):
    print(f'nest: {nesting}')
    print(f'elementCount: {len(rule)}')
    if isinstance(rule, str):
        print(f'{rule} {message[idx]}')
        return rule == message[idx]
    idxOffset = 0
    results = []
    for element in rule:
        if idx + idxOffset > len(message) - 1:
            print('here')
            return False
        if isinstance(element, str):
            charMatch = element == message[idx + idxOffset]
            print(f'testChar idx {idx}, ele {element} mes[i] {message[idx]}')
            if not charMatch:
                return False
            idxOffset += 1
        else:
            results.append(validateAgainstRule0(element, message, nesting + 1, idx + idxOffset))

    if idx + idxOffset == len(message):
        results.append(True)
        
    print(f'nest {nesting} results {results}')
    return True in results
            
        
    

print(validateAgainstRule0(flattenHash['0'], example[0][0]))
