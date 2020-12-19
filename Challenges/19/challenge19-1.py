from pprint import pprint
import re

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
                hashRules[key] = values
            elif sectionNum == 1:
                line = line.strip('\n')
                data.append(line)
                linenum += 1
            else:
                print('unexpected sections in input')
    # pprint(data)
    # pprint(hashRules)
    refsRemain = True
    while refsRemain:
        refsRemain = False
        for key, rule in hashRules.items():
            updatedRule = []
            for char in rule:
                if char.isnumeric():
                    innerRule = hashRules[char]
                    if innerRule.isalpha():
                        updatedRule.append(innerRule)
                    else:
                        refsRemain = True
                        updatedRule.append(f'({hashRules[char]})')
                elif char.isspace():
                    continue
                else:
                    updatedRule.append(char)
            hashRules[key] = "".join(updatedRule)
        # pprint(hashRules)
    return (data, hashRules)


example = parseInput('example.txt')
input = parseInput('input.txt')


# def convertToRegex(rulesHash):
#     for key, rule in rulesHash.items():
        
#     return rulesHash                

# flattenHash = flattenRules(example[1])

def validateAgainstRule0(rule, message):
    pattern = f'^{rule}$'
    result = re.match(pattern, message)
    if result:
        return True
    else:
        return False
            
validMessages = 0
for message in example[0]:
    if validateAgainstRule0(input[1]['0'], message):
        validMessages += 1
        
    

print(validMessages)
