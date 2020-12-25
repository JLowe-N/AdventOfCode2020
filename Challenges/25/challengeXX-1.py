def parseInput(filename):
    data = []
    with open(filename) as file:
        linenum = 0
        for line in file:
            line = line.strip('\n')
            data.append(line)
            linenum += 1
    return data


example = (5764801, 17807724)
input = (3469259, 13170438)

def myFunc(publicKey, subjectNumber = 7):
    value = 1
    loopSize = 0
    while value != publicKey:
        value = value * subjectNumber
        value = value % 20201227
        loopSize +=1
    return loopSize

def findEncrypt(loopSize, publicKey):
    value = 1
    subjectNumber = publicKey
    i = 0
    while i < loopSize:
        value = value * subjectNumber
        value = value % 20201227
        i +=1
    return value
    
cardLoop = myFunc(input[0])
doorLoop = myFunc(input[1])

cardEncrypt = findEncrypt(cardLoop, input[1])
doorEncrypt = findEncrypt(doorLoop, input[0])


print(doorLoop)
print(cardLoop)

print(cardEncrypt)
print(doorEncrypt)





# card public key card loop size
