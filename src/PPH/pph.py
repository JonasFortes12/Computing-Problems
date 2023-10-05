import os
from code.loadpphData import loadpphData
from code.maximizeRatioPPH import solve_PPH
from code.sortAlgorithms.bubbleSort import bubbleSortByRatio


data = loadpphData(os.path.join(os.path.dirname(__file__), 'data', 'pph_100_01.dat'))

print(data)

print("___________________________________")

S_asterisk = solve_PPH(data[0], data[1:len(data)])
print(S_asterisk)

print("___________________________________")

S_asterisk = solve_PPH(data[0], bubbleSortByRatio(data[1:len(data)]))
print(S_asterisk)




