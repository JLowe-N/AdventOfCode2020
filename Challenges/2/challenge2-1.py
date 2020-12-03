'''
Count the number of valid passwords based on the security policy and password
provided in the input strings.  The Toboggan Company Rep thinks the security
policy is as follows:
Example String: '1-3 a: abcde'
    <requiredCharCountLimits requiredChar passwordToValidate>
The security policy has changed over time, and is represented with each password
needing to be validated.  In this example, the required character 'a' must appear
in the password at minimum 1 time, and at maximum 3 times.
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
