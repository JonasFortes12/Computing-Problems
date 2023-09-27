from readData import extract_graph_data


class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = []
        self.adjacencias = {}
    
    def adicionar_vertice(self, vertice):
        self.vertices.add(vertice)
        if vertice not in self.adjacencias:
            self.adjacencias[vertice] = []

    def adicionar_aresta(self, v1, v2, peso):
        self.arestas.append((peso, v1, v2))
        self.adjacencias[v1].append((peso, v2))
        self.adjacencias[v2].append((peso, v1))

def encontrar_aresta_menor_peso(grafo, visitados):
    menor_peso = float('inf')
    aresta_menor_peso = None
    for v1 in visitados:
        for peso, v2 in grafo.adjacencias[v1]:
            if v2 not in visitados and peso < menor_peso:
                menor_peso = peso
                aresta_menor_peso = (peso, v1, v2)
    return aresta_menor_peso

def arvore_prim(grafo):
    arvore_minima = Grafo()
    vertice_inicial = next(iter(grafo.vertices))
    visitados = set([vertice_inicial])

    while len(visitados) < len(grafo.vertices):
        aresta = encontrar_aresta_menor_peso(grafo, visitados)
        if aresta is None:
            break
        peso, v1, v2 = aresta
        visitados.add(v2)
        arvore_minima.adicionar_vertice(v1)
        arvore_minima.adicionar_vertice(v2)
        arvore_minima.adicionar_aresta(v1, v2, peso)

    return arvore_minima
def executar(numNodes, graph_data):
    # Exemplo de uso
    grafo = Grafo()
    for i in range(numNodes):
        grafo.adicionar_vertice(i)
    for vertice in graph_data:
        # print(vertice)
        grafo.adicionar_aresta(vertice[0], vertice[1], vertice[2])
    # Algoritmo de Prim para criar a Árvore Geradora Mínima
    arvore_prim(grafo)

if __name__ == "__main__":
    # Exemplo de uso
    grafo = Grafo()

    file_path = 'dmxa0628.stp'
    numNodes, graph_data, _= extract_graph_data(file_path)
    for i in range(numNodes):
        grafo.adicionar_vertice(i)
    for vertice in graph_data:
        # print(vertice)
        grafo.adicionar_aresta(vertice[0], vertice[1], vertice[2])
    # Algoritmo de Prim para criar a Árvore Geradora Mínima
    arvore_minima = arvore_prim(grafo)
    print("Árvore mínima:")
    for aresta in arvore_minima.arestas:
        print(aresta)