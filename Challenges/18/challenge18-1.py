import re

def parseInput(filename):
    data = []
    with open(filename) as file:
        linenum = 0
        for line in file:
            line = line.strip('\n')
            data.append(line)
            linenum += 1
    return data


example = parseInput('example.txt')
input = parseInput('input.txt')

# print(example)
def weirdMath(mathString):
    stack = []
    queue = []
    i = 0
    while i < len(mathString):
        char = mathString[i]
        if char == ' ':
            i+= 1
            continue
        if char == '(':
            stack.append(char)
            i += 1
            continue
        if char != ')' and i < len(mathString):
            stack.append(char)
            i += 1
            continue
        # print(f'stack: {stack}')
        stackEle = stack.pop()
        while stackEle != '(' and len(stack) != 0:
            queue.insert(0, stackEle)
            stackEle =  stack.pop()
        # print(f'queue: {queue}')
        elemA = int(queue.pop(0))
        while len(queue) > 0:
            elemOp = queue.pop(0)
            elemB = int(queue.pop(0))
            if elemOp == '+':
                elemA = elemA + elemB
            elif elemOp == '-':
                elemA = elemA - elemB
            if elemOp == '*':
                elemA = elemA * elemB
        stack.append(elemA)
        i += 1

    # print(stack)
    # print(queue)
    elemA = int(stack.pop(0))
    while len(stack) > 0:
        elemOp = stack.pop(0)
        elemB = int(stack.pop(0))
        if elemOp == '+':
            elemA = elemA + elemB
        elif elemOp == '-':
            elemA = elemA - elemB
        if elemOp == '*':
            elemA = elemA * elemB
    
    return elemA

sum = 0
for row in input:
    sum += weirdMath(row)
print(sum)
            
            
        
        

            

            

                

        
    
    # for idx, char in enumerate(mathString):
    #     if idx == 0:
    #         if char.isnumeric():
    #             result += int(char)
    #         elif char == '(':
    #             stack.push('(')
    #         else:
    #             print('Invalid first char')
    #     else:
    #         if char == ' ':
    #             continue
    #         elif '+*-'.includes(char):
    #             stack.push(char)
    #         elif char.isnumeric():
    #             operation = stack.pop()
    #             if operation == '+':
    #                 result += int(char)
    #             elif operation == '-':
    #                 result -= int(char)
    #             elif operation == '*':
    #                 result *= int(char)
    #             else:
    #                 print("Expected math operator in stack")
    #         elif char == '(':
    #             stack.push(char)
    #         elif char ==')':
    #             stack.push(char)




    

# def isNumeral(string):
#     return re.ma/^[0-9]$/.test(string)


# print(myFunc)