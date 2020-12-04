from pprint import pprint

def getPassportDict(passportStr):
    passport = {}
    finalPassportString = passportString.rstrip(' ')
    kvPairList = finalPassportString.split(' ')
    while len(kvPairList) > 0:
        (key, value) = kvPairList.pop().split(':')
        passport[key] = value
    return passport

input = []
with open('input.txt') as reader:
    passportString = ''
    for line in reader:
        if line.isspace():
            passport = getPassportDict(passportString)
            passportString = ''
            input.append(passport)
        else:
            passportString += line.rstrip('\n') + ' '
    if len(passportString) > 0:
        passport = getPassportDict(passportString)
        passportString = ''
        input.append(passport)




REQUIRED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] # not required - cid

def validatePassport(passport, requiredKeys):
    isValidPassport = True
    for key in requiredKeys:
        if key not in passport.keys():
            # print('missing:', key)
            isValidPassport = False
    # if not isValidPassport:
    #     print("Invalid:")
    #     pprint(passport)
    return isValidPassport

validPassportCount = 0
for passport in input:
    isValidPassport = validatePassport(passport, REQUIRED_KEYS)
    if isValidPassport:
        validPassportCount += 1


print(f'Total Passports checked: {len(input)}')
print(f'Valid passports counted: {validPassportCount}')