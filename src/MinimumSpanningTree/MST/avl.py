from readData import extract_graph_data

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        right_child.height = 1 + \
            max(self.height(right_child.left), self.height(right_child.right))
        return right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        left_child.height = 1 + \
            max(self.height(left_child.left), self.height(left_child.right))
        return left_child

    def insert(self, root, key):
        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance_factor(root)

        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        mst = []  # Lista que conterá as arestas da AGM
        visited = set()  # Conjunto de vértices já visitados
        # Começamos a partir do primeiro vértice
        start_vertex = list(self.graph.keys())[0]
        min_weight = float('inf')  # Inicializamos o mínimo peso como infinito
        min_edge = None  # Inicializamos a aresta mínima como nula
        for neighbor, weight in self.graph[start_vertex]:
            if weight < min_weight:
                min_weight = weight
                min_edge = (start_vertex, neighbor, weight)

        visited.add(start_vertex)
        mst.append(min_edge)

        while len(mst) < self.vertices - 1:
            min_weight = float('inf')
            min_edge = None
            for u, v, weight in mst:
                for neighbor, edge_weight in self.graph[v]:
                    if neighbor not in visited and edge_weight < min_weight:
                        min_weight = edge_weight
                        min_edge = (v, neighbor, edge_weight)

            if min_edge:
                visited.add(min_edge[1])
                mst.append(min_edge)

        return mst
def executar(numNodes, graph_data):
    g = Graph(numNodes)
    for vertice in graph_data:
        g.add_edge(vertice[0], vertice[1], vertice[2])

    g.prim_mst()

if __name__ == "__main__":
    # Para teste
    file_path = 'dmxa0628.stp'
    numNodes, graph_data, _ = extract_graph_data(file_path)
    g = Graph(numNodes)
    for vertice in graph_data:
        g.add_edge(vertice[0], vertice[1], vertice[2])

    mst = g.prim_mst()
    for u, v, weight in mst:
        print(f"Aresta ({u}-{v}) com peso {weight}")
