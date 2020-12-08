from pprint import pprint
import re

class HandbagGraph:
    def __init__(self):
        self.handbags = {}
    
    def addHandbag(self, handbag):
        self.handbags[handbag.color] = handbag

    def getCountOfBagsThatCanHoldColor(self, targetColor):
        countOfBagsThatCanHoldColor = 0
        # visitedColors = {}
        graph = self.handbags
        for bagColor in graph:
            # if bagColor in visitedColors:
            #     continue
            # visitedColors[bagColor] = True
            innerBags = [bagRule[1] for bagRule in graph[bagColor].allowed]
            if targetColor in innerBags:
                print(f'{bagColor} has it inside!')
                countOfBagsThatCanHoldColor += 1
                continue
            while len(innerBags) > 0:
                currentBag = innerBags.pop(0)
                # if currentBag in visitedColors:
                #     continue
                # visitedColors[currentBag] = True
                for bagRule in graph[currentBag].allowed:
                    innerBags.append(bagRule[1])
                if targetColor in innerBags:
                    print(f'{bagColor} has it inside!')
                    countOfBagsThatCanHoldColor += 1
                    break
        return countOfBagsThatCanHoldColor       


class Handbag:
    def __init__(self, color, allowed):
        self.color = color
        self.allowed = []

        if allowed[0] != 'no other':
            for bag in allowed:
                number, colorAllowed = bag.split(' ', 1)
                self.allowed.append((number, colorAllowed))


handbagRuleGraph = HandbagGraph()
input = []
with open('input.txt') as reader:
    for line in reader:
        parsedRule = [element.strip(',').replace(' contain ', '').strip().strip('.') for element in re.split('bags?', line)]
        if parsedRule[-1] == '':
            parsedRule.pop()
        handbag = Handbag(parsedRule[0], parsedRule[1:])
        handbagRuleGraph.addHandbag(handbag)

print(handbagRuleGraph.getCountOfBagsThatCanHoldColor('shiny gold'))



