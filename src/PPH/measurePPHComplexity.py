import time
import tracemalloc
import pandas as pd
import os
from code.loadpphData import loadpphData

def measurePPHComplexity(algorithm, instances, repeat, description):
    
    results = []
    
    for instance in instances:
        arr = loadpphData(os.path.join(os.path.dirname(__file__), 'data', f'pph_{instance}_01.dat'))
        execTimes = []
        allMemories = []
        
        for _ in range(repeat):
          
            tracemalloc.start()
            startTime = time.time()
            
            # Execeução do algoritmos da Mochila
            algorithm(arr[0], arr[1:len(arr)])
            
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
        
        