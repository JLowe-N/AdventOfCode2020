'''
Review your expense reports for the elves!
Find 2 expense items in the expense report that add up to
2020, then return the multiplication result of those two expense items.
There will only be two unique expense amounts that add up to 2020.
'''
input = []
with open('input.txt') as reader:
    for line in reader:
        input.append(int(line.rstrip('\n')))

# Hash Solution
def findTwentyTwentyElementsAndMultiply(expenseList):
    potentialMatchesHash = {}
    potentialMatch = 2020 - expenseList[0]
    potentialMatchesHash[potentialMatch] = expenseList[0]
    for i in range(1, len(expenseList)):
        currentExpense = expenseList[i]
        if currentExpense in potentialMatchesHash:
            return currentExpense * potentialMatchesHash[currentExpense]
        else:
            potentialMatch = 2020 - currentExpense
            potentialMatchesHash[potentialMatch] = currentExpense
    print("No two expenses sum to 2020!")


# Naive Solution
# Complexity O(n^2) Time | O(n) Space
# No hash
# def findTwentyTwentyElementsAndMultiply(expenseList):
#     for i in range(len(expenseList) - 1):
#         for j in range(i + 1, len(expenseList)):
#             expenseSum = expenseList[i] + expenseList[j]
#             if expenseSum == 2020:
#                 return expenseList[i] * expenseList[j]

print(findTwentyTwentyElementsAndMultiply(input))
# 787776

            


