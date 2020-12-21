from pprint import pprint
import re
rules = {}
messages = []
switch = False

filename = 'part2input.txt'

with open(filename) as file:
    for line in file:
        if line == '\n':
            switch = True
            continue
        if not switch:
            temp_line = (str(line.rstrip())).replace('"', '').split(' ')
            rules[temp_line[0][:-1]] = temp_line[1:]
        else:
            messages.append(str(line.rstrip()))

def build_regex(r: str):
    global rules

    if rules[r][0] in 'ab':
        return rules[r][0]
    
    rx = "("
    for this_rule in rules[r]:
        if this_rule == "|":
            rx += this_rule
        else:
            rx += build_regex(this_rule)
    rx += ")"
    return rx

rule42 = build_regex("42")
rule31 = build_regex("31")

counter_p2 = 0
for n in range(1, 10):  
    my_regex = f"^({rule42}+{rule42}{{{n}}}{rule31}{{{n}}})$"
    for this_message in messages:
        if re.match(my_regex, this_message):
            counter_p2 += 1

print(counter_p2)

# my_regex = f"^{build_regex('0')}$"
# counter_p1 = 0
# for this_message in messages:
#     if re.match(my_regex, this_message):
#         counter_p1 += 1

# print(counter_p1)

# print(rules)
# print(messages)


# def convertToRegex(rulesHash):
#     for key, rule in rulesHash.items():
        
#     return rulesHash                

# flattenHash = flattenRules(example[1])

# def validateAgainstRule0(rule, message):
#     pattern = f'^{rule}$'
#     result = re.match(pattern, message)
#     if result:
#         return True
#     else:
#         return False
            
# validMessages = 0
# for message in myinput[0]:
#     if validateAgainstRule0(myinput[1]['0'], message):
#         validMessages += 1
        
    

# print(validMessages)
