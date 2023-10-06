import time
import tracemalloc
import pandas as pd
import os
from code.generateRandomPairs import generateRandomPairs

#Importação dos algoritmos de ordenação
from code.sortAlgorithms.bubbleSort import bubbleSortByRatio
from code.sortAlgorithms.insertionSort import insertionSortByRatio
from code.sortAlgorithms.selectionSort import selectionSortByRatio
from code.sortAlgorithms.mergeSort import mergeSortByRatio
from code.sortAlgorithms.quickSort import quickSortByRatio
from code.sortAlgorithms.heapSort import heapSortByRatio



def measurePPHComplexity(algorithm, instances, sortedBy, repeat, description):
    fullStartTime = time.time()
    results = []
    
    for instance in instances:
        arr = generateRandomPairs(instance)
        execTimes = []
        allMemories = []
        
        for _ in range(repeat):
            
            tracemalloc.start()
            startTime = time.time()
            
            # Ordena o vetor de entrada
            arrSorted = sort(arr, sortedBy)
            
            # Execeução do algoritmo PPH
            algorithm(arrSorted[0], arrSorted[1:len(arrSorted)])
            
            endTime = time.time()
            execTimes.append(endTime - startTime)
            allMemories.append(tracemalloc.get_traced_memory()[1])
            tracemalloc.stop()
            tracemalloc.clear_traces()
    
        results.append(
            {
            "Instância":instance, 
            "Tempo": round((max(execTimes) + min(execTimes))/2, 3), 
            "Maior Tempo":round(max(execTimes), 3),
            "Menor Tempo":round(min(execTimes), 3),
            "Memória":max(allMemories)}
            )
    
        pd.DataFrame(results).to_csv(os.path.join(os.path.abspath(os.path.dirname(__file__)),'results',f'PPH_{description}_repeat_{repeat}.csv'), index=False)
    
    fullEndTime = time.time()
    
    print(f'Tempo Total: {(fullEndTime - fullStartTime)} s')


def sort(arr, sortedBy):
    if(sortedBy == 'bubbleSort'):
        return bubbleSortByRatio(arr)
    
    elif(sortedBy == 'insertionSort'):
         return insertionSortByRatio(arr)
    
    elif(sortedBy == 'selectionSort'):
         return selectionSortByRatio(arr)
    
    elif(sortedBy == 'mergeSort'):
        return mergeSortByRatio(arr)
    
    elif(sortedBy == 'quickSort'):
        return quickSortByRatio(arr)
    
    elif(sortedBy == 'heapSort'):
         return heapSortByRatio(arr)
    
    elif(sortedBy == 'none'):
         return arr
    
    else:
        print('Invalid orderedBy option!')
        return []