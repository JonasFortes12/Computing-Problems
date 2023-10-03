import time
import tracemalloc
import pandas as pd
import os

def measureFBComplexity(algorithm, instances, repeat, description):
    
    results = []
    
    for instance in instances:
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'instancias',f'instancia_{instance}.txt' )
        file = open(path, "r")
        content = file.read()
        file.close()
        arr = eval(content)
        
        execTimes = []
        allMemories = []
        
        for _ in range(repeat):
          
            tracemalloc.start()
            startTime = time.time()
            
            # Execeução do algoritmos da Mochila
            algorithm(arr, 50)
            
            endTime = time.time()
            execTimes.append(endTime - startTime)
            allMemories.append(tracemalloc.get_traced_memory()[1])
            tracemalloc.stop()
            tracemalloc.clear_traces()
    
        results.append(
            {
            "Instância":int(instance), 
            "Tempo":max(execTimes), 
            "Memória":max(allMemories)}
            )
 
    pd.DataFrame(results).to_csv(os.path.join(os.path.abspath(os.path.dirname(__file__)),'results',f'MF_{description}_repeat_{repeat}.csv'), index=False)
        
        
