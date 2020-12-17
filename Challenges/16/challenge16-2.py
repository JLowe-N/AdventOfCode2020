import re

def parseInput(filename):
    data = []
    with open(filename) as file:
        lineNum = 1
        dataSection = 1
        ticketFieldBounds = []
        yourTicket = None
        nearbyTickets = []
        for line in file:
            if line.isspace():
                dataSection += 1
                continue

            line = line.rstrip('\n')
            if dataSection == 1:
                data = re.split(':| or ', line)
                for idx, element in enumerate(data):
                    if idx == 0:
                        data[idx] = element.replace(' ', '_')
                    else:
                        data[idx] = [int(x) for x in element.replace(' ', '').split('-')]
                # print(data)
                ticketFieldBounds.append(data)
            elif dataSection == 2:
                if line.startswith('your ticket:'):
                    continue
                yourTicket = [int(x) for x in line.split(',')]
            elif dataSection == 3:
                if line.startswith('nearby tickets:'):
                    continue
                nearbyTickets.append([int(x) for x in line.split(',')])
            else:
                print(f"Too many data sections in file! Extra data at line {lineNum}")
                break
            lineNum += 1
    return (ticketFieldBounds, yourTicket, nearbyTickets)


example = parseInput('example.txt')
example2 = parseInput('example2.txt')
input = parseInput('input.txt')

def sumInvalidTicketFields(ticketFieldRules, myTicket, nearbyTickets):
    invalidValues = []
    for ticket in nearbyTickets:
        for value in ticket:
            valueWasFound = False
            for rule in ticketFieldRules:
                for idx, element in enumerate(rule):
                    if idx == 0:
                        continue # field name
                    else:
                        minVal, maxVal = element
                        if value >= minVal and value <= maxVal:
                            valueWasFound = True
            if not valueWasFound:
                invalidValues.append(value)
    return sum(invalidValues)

def getValidTickets(ticketFieldRules, myTicket, nearbyTickets):
    validTickets = []
    for ticket in nearbyTickets:
        allValuesValid = True
        for value in ticket:
            valueWasFound = False
            for rule in ticketFieldRules:
                for idx, element in enumerate(rule):
                    if idx == 0:
                        continue # field name
                    else:
                        minVal, maxVal = element
                        if value >= minVal and value <= maxVal:
                            valueWasFound = True
            if not valueWasFound:
                allValuesValid = False
                break
        if allValuesValid:
            validTickets.append(ticket)

    return validTickets

def getPossibleColsForFields(ticketFieldRules, myTicket, validTickets):
    possibleMatches = {}
    for fieldRule in ticketFieldRules:
        key = fieldRule[0]
        possibleMatches[key] = []
        validRanges = fieldRule[1:]
        for colIdx in range(len(myTicket)):
            # print(colIdx)
            isPossibleIdxMatch = True
            for ticket in validTickets:
                # print(ticket)
                value = ticket[colIdx]
                for rangeIdx, (minVal, maxVal) in enumerate(validRanges):
                    if value >= minVal and value <= maxVal:
                        break

                    if rangeIdx == len(validRanges) - 1:
                        isPossibleIdxMatch = False

                if isPossibleIdxMatch == False:
                    break
            if isPossibleIdxMatch:
                # print(f'{key} {colIdx} {ticket} {isPossibleIdxMatch}')
                possibleMatches[key].append(colIdx)
    return possibleMatches

def getFieldOrder(possibleMatches):
    matchesToNarrow = [[key, possibleMatches[key]] for key in sorted(possibleMatches, key=lambda k: len(possibleMatches[k]))]
    finalMapping = {}
    for _ in matchesToNarrow:
        key, value = matchesToNarrow[0]
        value = value[0]
        finalMapping[key] = value
        matchesToNarrow = matchesToNarrow[1:]
        for _, values in matchesToNarrow:
            values.remove(value)
    return finalMapping
   
    
def multiplyDepartureValues(ticket, mapping):
    product = 1
    print(mapping)
    for field, idx in mapping.items():
        if field.startswith('departure'):
            print(ticket[idx])
            product *= ticket[idx]
    return product

                
                
validTickets = getValidTickets(*input)
possibleMatches = getPossibleColsForFields(input[0], input[1], validTickets)
fieldOrder = getFieldOrder(possibleMatches)
print(fieldOrder)
print(multiplyDepartureValues(input[1], fieldOrder))

