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
input = parseInput('input.txt')

def myFunc(ticketFieldRules, myTicket, nearbyTickets):
    print(ticketFieldRules)
    print(myTicket)
    print(nearbyTickets)
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
       
print(myFunc(*input))