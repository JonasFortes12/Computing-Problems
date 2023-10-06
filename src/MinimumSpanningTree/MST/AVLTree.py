class Aresta:
    def __init__(self, u, v, peso):
        self.u = u
        self.v = v
        self.peso = peso

    def __str__(self):
        return f"{self.u}, {self.v}, {self.peso}"

class Node:
    def __init__(self, aresta):
        self.aresta = aresta
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

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_left(self, y):
        x = y.right
        if x is None:
            return y

        T2 = x.left

        x.left = y
        y.right = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_right(self, x):
        y = x.left
        if y is None:
            return x

        T2 = y.right

        y.right = x
        x.left = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, node, aresta):
        if node is None:
            return Node(aresta)

        if aresta.peso < node.aresta.peso:
            node.left = self.insert(node.left, aresta)
        else:
            node.right = self.insert(node.right, aresta)

        self.update_height(node)

        balance = self.balance(node)

        # Rotações para balancear a árvore
        if balance > 1:
            if aresta.peso < node.left.aresta.peso:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            if aresta.peso > node.right.aresta.peso:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def insert_aresta(self, aresta):
        self.root = self.insert(self.root, aresta)

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_min(self, node):
        if node is None:
            return node

        if node.left is None:
            return node.right

        node.left = self.delete_min(node.left)
        self.update_height(node)
        return node

    def delete(self, node, aresta):
        if node is None:
            return node

        if node.left!=None:
            node.left = self.delete(node.left, aresta)
        if node.right!=None:
            node.right = self.delete(node.right, aresta)
        if node.aresta.u == aresta.u:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.aresta = self.find_min(node.right).aresta
            node.right = self.delete_min(node.right)
        
        self.update_height(node)

        balance = self.balance(node)

        # Rotações para balancear a árvore após a exclusão
        if balance > 1:
            if self.balance(node.left) >= 0:
                return self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

        if balance < -1:
            if self.balance(node.right) <= 0:
                return self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def delete_aresta(self, aresta):
        if self.root is not None:
            self.root = self.delete(self.root, aresta)

    def change_value(self, old_aresta, new_aresta):
        self.delete_aresta(old_aresta)
        self.insert_aresta(new_aresta)

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.aresta)
            self.inorder_traversal(node.right)

    def display(self):
        self.inorder_traversal(self.root)
    def find_node_by_u(self, u, node=1):
        if node==1:
            node = self.root

        if node is None:
            return None
        if node.aresta.u == u:
            return node
        left = self.find_node_by_u(u, node.left)
        if left != None:
            return left
        right = self.find_node_by_u(u, node.right)
        if right != None:
            return right
# Exemplo de uso
if __name__ == "__main__":
    avl_tree = AVLTree()
    avl_tree.insert_aresta(Aresta(1, 2, 5))
    avl_tree.insert_aresta(Aresta(2, 3, 10))
    avl_tree.insert_aresta(Aresta(3, 4, 8))
    avl_tree.insert_aresta(Aresta(4, 5, 3))

    print("Árvore AVL:")
    avl_tree.display()

    min_aresta = avl_tree.find_min(avl_tree.root).aresta
    print("\nMenor aresta:", min_aresta)
    
    avl_tree.delete_aresta(min_aresta)
    print("\nÁrvore AVL após a exclusão do menor valor:")
    avl_tree.display()

    avl_tree.insert_aresta(Aresta(5, 6, 7))
    print("\nÁrvore AVL após a inserção:")
    avl_tree.display()
    
    avl_tree.delete_aresta(Aresta(1, None, 1000))
    print("\nÁrvore AVL depois da deleção:")
    avl_tree.display()
    
    avl_tree.change_value(Aresta(3, 4, 8), Aresta(3, 4, 15))
    print("\nÁrvore AVL após a alteração do valor:")
    avl_tree.display()
    
    u = 3
    found_node = avl_tree.find_node_by_u(u)
    if found_node is not None:
        print(f"Nó com 'u' igual a {u}: {found_node.aresta}")
    else:
        print(f"Nó com 'u' igual a {u} não encontrado.")
