import os
from code.loadpphData import loadpphData
from code.setMaximizeRatio import setMaximizeRatio


data = loadpphData(os.path.join(os.path.dirname(__file__), 'data', 'pph_30_01.dat'))

print(setMaximizeRatio(data))





