# import os
# from code.loadpphData import loadpphData
from code.maximizeRatioPPH import solve_PPH
from code.sortAlgorithms.bubbleSort import bubbleSortByRatio
from measurePPHComplexity import measurePPHComplexity
from code.generateRandomPairs import generateRandomPairs



# data = generateRandomPairs(100)
# print(data)

# print("___________________________________")

# S_asterisk = solve_PPH(data[0], data[1:len(data)])
# print(S_asterisk)

# print("___________________________________")

# S_asterisk = solve_PPH(data[0], bubbleSortByRatio(data[1:len(data)]))
# print(S_asterisk)


instances = [100, 200, 1000, 2000, 5000, 10000, 50000, 100000, 1000000, 5000000, 10000000]
# instances = [100, 200, 1000, 2000]
repeat = 3

measurePPHComplexity(solve_PPH, instances, repeat, 'item01_allNight')


