'''
The interpretation of the password security rule/validation has changed.
Example: '1-3 a: abcde'
The required character 'a' must appear in the password 'abcde' at either
position 1 or position 3, but not both!  Also, this notation is 1-indexed and not
0-indexed.
'''
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
def isValidTobogganPassword(position1, position2, requiredChar, password):
    if position1 > len(password) or position2 > len(password):
        return False
    # position rule is 1-indexed, convert to 0-index
    firstChar = password[position1 - 1]
    secondChar = password[position2 - 1]
    return (firstChar == requiredChar or secondChar == requiredChar) and (firstChar != secondChar)

def countValidPasswords(passwordValidationList):
    validPasswordCount = 0
    for passwordValidationString in passwordValidationList:
        parsedValidation = parsePasswordValidationString(passwordValidationString)
        if isValidTobogganPassword(*parsedValidation):
            validPasswordCount += 1
    return validPasswordCount

print(countValidPasswords(input))
