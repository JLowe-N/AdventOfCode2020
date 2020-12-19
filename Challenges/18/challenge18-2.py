import re

def parseInput(filename):
    data = []
    with open(filename) as file:
        linenum = 0
        for line in file:
            line = line.strip('\n').replace(' ', '')
            split = re.findall('[+-/*^//()]|\d+|\w+', line)
            data.append(split)
            linenum += 1
    return data


example = parseInput('example.txt')
input = parseInput('input.txt')

# print(example)
def weirdMath(opsList):
    stack = []
    queue = []
    result = []
    i = 0
    oper_priority = {'+': 2, '-': 2, '/': 1, '*': 1, '^': 3, '(': 4, ')': 4, }
    for idx, element in enumerate(opsList):

        if element == '(':
            stack.append('(')
        elif element == ')':
            parenthesesLoop = True
            while parenthesesLoop:
                if len(stack) > 0:
                    if stack[-1] != '(':
                        result.append(stack.pop())
                    else:
                        stack.pop()
                        parenthesesLoop = False
                else:
                    print("Parentheses not balanced.")
                    return None
        
        elif element.isdecimal():
            result.append(int(element))
        elif len(stack) == 0:
            stack.append(element)
        elif len(stack) > 0 and stack[-1] == '(':
            stack.append(element)
        elif oper_priority[element] > oper_priority[stack[-1]]:
            stack.append(element)
        else: 
            low_priority_op_loop = True
            while low_priority_op_loop:
                if len(stack) == 0:
                    stack.append(element)
                    low_priority_op_loop = False
                elif oper_priority[element] <= oper_priority[stack[-1]] and stack[-1] != '(':
                    result.append(stack.pop())
                else:
                    stack.append(element)
                    low_priority_op_loop = False
        
    for _ in range(len(stack)):
        element = stack.pop()
        if element == '(' or element == ')':
            print("Invalid expression")
            return None
        else:
            result.append(element)
    
    return result
    



def postfix_calc(postfixList):
    working_stack = []
    for step, element in enumerate(postfixList):
        if isinstance(element, int):
            working_stack.append(element)
        else:  # Must be an operator
            if element == '+':
                b = working_stack.pop()
                a = working_stack.pop()
                working_stack.append(a + b)
            elif element == '-':
                b = working_stack.pop()
                a = working_stack.pop()
                working_stack.append(a - b)
            elif element == '*':
                b = working_stack.pop()
                a = working_stack.pop()
                working_stack.append(a * b)
            elif element == '/':
                b = working_stack.pop()
                a = working_stack.pop()
                if b != 0:
                    working_stack.append(a // b)
                else:
                    print("Division by zero error")
                    break
            elif element == '^':
                b = working_stack.pop()
                a = working_stack.pop()
                working_stack.append(a ** b)
            else:
                print(f"Unknown operator {element} was supplied.")
    # Expression end, return top of stack
    # print(f"Final result from the calculator: {working_stack[-1]}")
    return working_stack[-1]

        
                        


  
postfix = weirdMath(input[0])
print(postfix_calc(postfix))

sum = 0
for row in input:
    postfixList = weirdMath(row)
    sum += postfix_calc(postfixList)
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