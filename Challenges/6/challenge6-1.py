from pprint import pprint
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
    # print(group)
    s = set()
    for person in group:
        for letter in person:
            s.add(letter)
    # print(s)
    return s

print(input[0])
test1 = myFunc(['a', 'a', 'a'])
print(len(test1))

groupsYesTotal = 0
    
for group in input:
    groupsYesTotal += len(myFunc(group))
print(groupsYesTotal)


# print(myFunc())