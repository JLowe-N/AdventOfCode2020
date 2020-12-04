from pprint import pprint
import re
import time

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
            isValidPassport = False
            break
        value = passport[key]
        if key == 'byr':
            try:
                byr = int(value)
            except (ValueError, TypeError):
                isValidPassport = False
                break
            if not 1920 <= byr <= 2002:
                isValidPassport = False
                break
        if key == 'iyr':
            try:
                iyr = int(value)
            except (ValueError, TypeError):
                isValidPassport = False
                break
            if not 2010 <= iyr <= 2020:
                isValidPassport = False
                break
        if key == 'eyr':
            try:
                eyr = int(value)
            except (ValueError, TypeError):
                isValidPassport = False
                break
            if not 2020 <= eyr <= 2030:
                isValidPassport = False
                break
        if key == 'hgt':
            if not (value.endswith('cm') or value.endswith('in')):
                isValidPassport = False
                break
            units = value[-2:]
            height = int(value[:-2])
            if units == 'cm':
                if not (150 <= height <= 193):
                    isValidPassport = False
                    break
            if units == 'in':
                if not (59 <= height <= 76):
                    isValidPassport = False
                    break
        if key == 'hcl':
            isHex = bool(re.match(r"^#[0-9a-fA-F]{6}$", value))
            if not isHex:
                isValidPassport = False
                break
        if key == 'ecl':
            validEyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            if value not in validEyeColors:
                isValidPassport = False
                break
        if key == 'pid':
            isNineDigits = bool(re.match(r"^0*\d{9}$", value))
            if not isNineDigits:
                isValidPassport = False
                break
        if key == 'cid':
            continue
    # if isValidPassport:
    #     print('Valid passport:')
    #     pprint(passport)
    #     # print(f'Check {key}')
    #     time.sleep(2)
    return isValidPassport

# Test cases
testCases = [
{
    'name': 'tooYoung',
    'byr': '2003',
    'iyr': '2020',
    'eyr': '2020',
    'hgt': '150cm',
    'hcl': '#000000',
    'ecl': 'amb',
    'pid': '123456789',
    'cid': 'NP',
},
{
    'name': 'tooOld',
    'byr': '1919',
    'iyr': '2020',
    'eyr': '2020',
    'hgt': '150cm',
    'hcl': '#000000',
    'ecl': 'amb',
    'pid': '123456789',
    'cid': 'NP',
},
{
    'name': 'oldPassport',
    'byr': '1988',
    'iyr': '2009',
    'eyr': '2020',
    'hgt': '150cm',
    'hcl': '#000000',
    'ecl': 'amb',
    'pid': '123456789',
    'cid': 'NP',
},
{
    'name': 'futurePassport',
    'byr': '1988',
    'iyr': '2021',
    'eyr': '2020',
    'hgt': '150cm',
    'hcl': '#000000',
    'ecl': 'amb',
    'pid': '123456789',
    'cid': 'NP',
},
{
    'name': 'expiredPassport',
    'byr': '1988',
    'iyr': '2020',
    'eyr': '2019',
    'hgt': '150cm',
    'hcl': '#000000',
    'ecl': 'amb',
    'pid': '123456789',
    'cid': 'NP',
},
{
    'name': 'longeyrPassport',
    'byr': '1988',
    'iyr': '2020',
    'eyr': '2031',
    'hgt': '150cm',
    'hcl': '#000000',
    'ecl': 'amb',
    'pid': '123456789',
    'cid': 'NP',
},
{
    'name': 'tooShortCm',
    'byr': '1988',
    'iyr': '2020',
    'eyr': '2020',
    'hgt': '149cm',
    'hcl': '#000000',
    'ecl': 'amb',
    'pid': '123456789',
    'cid': 'NP',
},
{
    'name': 'tooTallCm',
    'byr': '1988',
    'iyr': '2020',
    'eyr': '2020',
    'hgt': '149cm',
    'hcl': '#000000',
    'ecl': 'amb',
    'pid': '123456789',
    'cid': 'NP',
},
{
    'name': 'tooShortIn',
    'byr': '1988',
    'iyr': '2020',
    'eyr': '2020',
    'hgt': '58in',
    'hcl': '#000000',
    'ecl': 'amb',
    'pid': '123456789',
    'cid': 'NP',
},
{
    'name': 'tooTallIn',
    'byr': '1988',
    'iyr': '2020',
    'eyr': '2020',
    'hgt': '77in',
    'hcl': '#000000',
    'ecl': 'amb',
    'pid': '123456789',
    'cid': 'NP',
},
{
    'name': 'noHgtUnits',
    'byr': '1988',
    'iyr': '2020',
    'eyr': '2020',
    'hgt': '150',
    'hcl': '#000000',
    'ecl': 'amb',
    'pid': '123456789',
    'cid': 'NP',
}
]

for passport in testCases:
    validatePassport(passport, REQUIRED_KEYS)

validPassportCount = 0
for passport in input:
    isValidPassport = validatePassport(passport, REQUIRED_KEYS)
    if isValidPassport:
        validPassportCount += 1


print(f'Total Passports checked: {len(input)}')
print(f'Valid passports counted: {validPassportCount}')