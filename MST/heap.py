import networkx as nx
from readData import extract_graph_data

# Crie um grafo vazio
G = nx.Graph()

# Função para adicionar um vértice ao grafo
def adicionar_vertice(grafo, vertice):
    grafo.add_node(vertice)

# Função para adicionar uma aresta ao grafo
def adicionar_aresta(grafo, vertice1, vertice2, peso):
    grafo.add_edge(vertice1, vertice2, weight=peso)
    
def executar(numNodes, graph_data):
    for i in range(numNodes):
        adicionar_vertice(G, i)
    for vertice in graph_data:
        adicionar_aresta(G, vertice[0], vertice[1], vertice[2])
    nx.minimum_spanning_tree(G)


if __name__ == "__main__":
    file_path = 'dmxa0628.stp'
    numNodes, graph_data, _ = extract_graph_data(file_path)
    for i in range(numNodes):
        adicionar_vertice(G, i)
    for vertice in graph_data:
        # print(vertice)
        adicionar_aresta(G, vertice[0], vertice[1], vertice[2])
    # Algoritmo de Prim para criar a Árvore Geradora Mínima
    mst = nx.minimum_spanning_tree(G)

    # Visualize a AGM
    print("Árvore Geradora Mínima:")
    print(mst.edges(data=True))
