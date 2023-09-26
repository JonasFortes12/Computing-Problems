import time
import tracemalloc

def measureComplexity(algorithm, description):
    tracemalloc.start()
    startTime = time.time()
    
    algorithm()
    
    memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tracemalloc.clear_traces()
    endTime = time.time()
    meddleTime = (endTime - startTime) / 2
    
    return [str(f'{meddleTime:.7f}'), (memory[1]), str(description) + '.txt']