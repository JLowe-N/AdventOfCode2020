from pprint import pprint
import string

input = []
with open('input.txt') as reader:
    group = []
    for line in reader:
        if line.isspace():
            input.append(group)
            group = []
        else:
            group.append(line.rstrip('\n'))
    if len(group) > 0:
        input.append(group)



def myFunc(group):
    allTrueCount = 0
    d = dict.fromkeys(string.ascii_lowercase, True)

    for person in group:
        for letter in d.keys():
            if letter not in person:
                d[letter] = False
    for letter in d.keys():
        if d[letter] == True:
            allTrueCount += 1
    # print(d)
    return allTrueCount



groupsYesTotal = 0
    
for group in input:
    groupsYesTotal += myFunc(group)
print(groupsYesTotal)


# print(myFunc())