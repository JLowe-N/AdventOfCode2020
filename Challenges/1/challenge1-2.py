'''
Review your expense reports for the elves!
For Part 2:
Find 3 expense items in the expense report that add up to
2020, then return the multiplication result of those two expense items.
There is only 1 triplet that sums up to 2020 in the input.
'''
input = []
with open('input.txt') as reader:
    for line in reader:
        input.append(int(line.rstrip('\n')))

# Hash Solution
# Complexity
def findTwentyTwentyElementsAndMultiply(inputs):

# Naive Solution
# Complexity O(n^3) time | O(1) space
# def findTwentyTwentyElementsAndMultiply(expenseList):
#     for i in range(1, len(expenseList) - 2):
#         for j in range(i + 1, len(expenseList) - 1):
#             for k in range(j + 1, len(expenseList)):
#                 currentSum = expenseList[i] + expenseList[j] + expenseList[k]
#                 if currentSum == 2020:
#                     return expenseList[i] * expenseList[j] * expenseList[k]  
#     print('No triplet of expenses adds to 2020!') 
     
print(findTwentyTwentyElementsAndMultiply(input))


            


