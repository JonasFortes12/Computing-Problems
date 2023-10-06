from code.maximizeRatioPPH import solve_PPH
from measurePPHComplexity import measurePPHComplexity
from code.generateRandomPairs import generateRandomPairs 

# data = generateRandomPairs(10)
# print(data)

# print("___________________________________")
# S_asterisk = solve_PPH(data[0], data[1:len(data)])
# print(S_asterisk)

# print("______________________________________")
# S_asterisk = solve_PPH(data[0], bubbleSortByRatio(data[1:len(data)]))
# print(S_asterisk)

# print("______________________________________")
# S_asterisk = solve_PPH(data[0], insertionSortByRatio(data[1:len(data)]))
# print(S_asterisk)


# instances = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 1000000, 5000000, 10000000]
instances = [100, 200, 1000, 2000, 5000, 10000, 50000]
repeat = 3
ListOrderedBy = [
    'bubbleSort',
    'insertionSort',
    'selectionSort',
]

# ListOrderedBy = [
#     'mergeSort',
#     'quickSort',
#     'heapSort',
# ]


for orderedBy in ListOrderedBy:
    measurePPHComplexity(solve_PPH, instances, orderedBy, repeat, f'item02_{orderedBy}')


