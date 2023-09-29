from listFiles import listFiles
from readData import extract_graph_data
import heap
import avl
import BinaryTree as BinaryTree
import tracemalloc
import threading
import time
import os
import pandas as pd

def memoryFunction(funcao):
    tracemalloc.start()  # Inicia o rastreamento
    funcao()
    _, peak = tracemalloc.get_traced_memory()
    global memoria
    memoria = peak / 10**6
    tracemalloc.stop()  # Para o rastreamento

global memory
memory = 0
arquivos = listFiles()
tasks = {"Heap": heap.executar, "AVL": avl.executar, "ArvoreBinaria": BinaryTree.executar}
for taskName, task in tasks.items():
    for tipo, instancias in arquivos.items():
        resultMem = []
        resultT = []
        numberNodesTot = []
        numberEdgesTot = []
        for instancia in instancias:
            numNodes, graph_data, numEdges = extract_graph_data(os.path.join('./AGM', tipo, instancia))
            numberNodesTot.append(numNodes)
            numberEdgesTot.append(numEdges)
            tempoInicial = time.time()
            thread = threading.Thread(target=memoryFunction,
                                    args=(lambda : task(numNodes, graph_data),))
            thread.start()
            thread.join()
            tempoFinal = time.time()
            tempoDecorrido = tempoFinal - tempoInicial
            print(f"Tempo decorrido: {tempoDecorrido} segundos\nMemória: {memoria:.2f} MB\nNúmero de Nós: {numNodes}\nUsando a instância: {instancia}\n\n\n")
            resultT.append(tempoDecorrido)
            resultMem.append(memoria)
            break
        pd.DataFrame({"Memory": resultMem, "Edges": numberEdgesTot, "Nodes": numberNodesTot}).to_csv(f"./results/{taskName}_{tipo}_memoria.csv")
        pd.DataFrame({"Memory": resultT, "Edges": numberEdgesTot, "Nodes": numberNodesTot}).to_csv(f"./results/{taskName}_{tipo}_tempo.csv")
        
