from readData import extract_graph_data
from BinaryTree import AVLTree, Aresta
from random import randint
class Vertice:
    def __init__(self, id, peso):
        self.id = id
        self.peso = peso
        self.pai = None

class Aresta:
    def __init__(self, u, v, peso):
        self.u = u
        self.v = v
        self.peso = peso
    def __str__(self):
        return f"{self.u}, {self.v}, {self.peso}"

def prim(grafo, s, numNodes):
    resultado = []
    arvore = AVLTree()
    for i in range(numNodes):
        arvore.insert_aresta(Aresta(i, None, 1000))
    arvore.change_value(Aresta(0, None, 1000), Aresta(0, None, 0))
    while arvore.root!=None:
        aresta_minima = arvore.find_min(arvore.root).aresta
        resultado.append(aresta_minima)
        arvore.delete_aresta(aresta_minima)
        for arestaParaTeste in grafo[aresta_minima.u]: 
            arestaNaFila = arvore.find_node_by_u(arestaParaTeste.v)
            if arestaNaFila != None:
                if arestaParaTeste.peso < arestaNaFila.aresta.peso:
                    arvore.change_value(Aresta(arestaParaTeste.v, None, None), Aresta(arestaParaTeste.v, aresta_minima.u, arestaParaTeste.peso))
    return resultado

def print_mst(mst):
    for mstb in mst:
        print(mstb.u, mstb.v, mstb.peso)
    
def executar(numNodes, graph_data):
    grafo = [[] for _ in range(numNodes)]
    for vertice in graph_data:
        if vertice[0]<numNodes and vertice[1]<numNodes:
            grafo[vertice[0]].append(Aresta(vertice[0], vertice[1], vertice[2]))
    prim(grafo, 0, numNodes)

# Exemplo de uso com o seu grafo personalizado:
if __name__ == "__main__":
    # Exemplo de uso

    file_path = 'dmxa0628.stp'
    numNodes, graph_data, _= extract_graph_data(file_path)
    grafo = [[] for _ in range(numNodes)]
    for vertice in graph_data:
        if vertice[0]<numNodes and vertice[1]<numNodes:
            grafo[vertice[0]].append(Aresta(vertice[0], vertice[1], vertice[2]))
    arvore = prim(grafo, 0, numNodes)
    for i in range(0, len(arvore)):
        print(arvore[i])
