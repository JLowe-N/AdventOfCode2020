input = []
with open('input.txt') as reader:
    for line in reader:
        input.append(line.rstrip('\n'))

def parsePasswordValidationString(string):
    parsedString = string.split(' ')
    minCharCount, maxCharCount = [int(x) for x in parsedString[0].split('-')]
    requiredChar = parsedString[1][0]
    passwordToValidate = parsedString[2]
    return minCharCount, maxCharCount, requiredChar, passwordToValidate

# Primary Algorithm
# Complexity O(c) | time O(1) space 
# where c is the length of the password to check
def isValidTobogganPassword(minCharCount, maxCharCount, requiredChar, password):
    requiredCharCount = 0
    for char in password:
        if char == requiredChar:
            requiredCharCount += 1
    return requiredCharCount >= minCharCount and requiredCharCount <= maxCharCount

def countValidPasswords(passwordValidationList):
    validPasswordCount = 0
    for passwordValidationString in passwordValidationList:
        parsedValidation = parsePasswordValidationString(passwordValidationString)
        if isValidTobogganPassword(*parsedValidation):
            validPasswordCount += 1
    return validPasswordCount

print(countValidPasswords(input))
