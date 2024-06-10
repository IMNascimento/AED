class Node:
    def __init__(self, value):
        self.value = value  # Atribui o valor do nó
        self.left = None  # Inicializa o ponteiro para o filho à esquerda como None
        self.right = None  # Inicializa o ponteiro para o filho à direita como None
        self.height = 1  # Inicializa a altura do nó como 1

class AVLTree:
    def __init__(self):
        self.root = None  # Inicializa a raiz da árvore como None

    def insert(self, value):
        # Insere um valor na árvore
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert(self.root, value)

    def _insert(self, current_node, value):
        # Método auxiliar para inserir um valor na árvore de forma recursiva
        if not current_node:
            return Node(value)
        elif value < current_node.value:
            current_node.left = self._insert(current_node.left, value)
        else:
            current_node.right = self._insert(current_node.right, value)

        # Atualiza a altura do nó atual
        current_node.height = 1 + max(self._get_height(current_node.left), self._get_height(current_node.right))

        # Calcula o fator de balanceamento
        balance = self._get_balance(current_node)

        # Rotação à direita
        if balance > 1 and value < current_node.left.value:
            return self._right_rotate(current_node)

        # Rotação à esquerda
        if balance < -1 and value > current_node.right.value:
            return self._left_rotate(current_node)

        # Rotação esquerda-direita
        if balance > 1 and value > current_node.left.value:
            current_node.left = self._left_rotate(current_node.left)
            return self._right_rotate(current_node)

        # Rotação direita-esquerda
        if balance < -1 and value < current_node.right.value:
            current_node.right = self._right_rotate(current_node.right)
            return self._left_rotate(current_node)

        return current_node

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Realiza a rotação
        y.left = z
        z.right = T2

        # Atualiza as alturas
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Retorna o novo nó raiz
        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Realiza a rotação
        y.right = z
        z.left = T3

        # Atualiza as alturas
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Retorna o novo nó raiz
        return y

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def inorder_traversal(self):
        nodes = []
        self._inorder_traversal(self.root, nodes)
        return nodes

    def _inorder_traversal(self, current_node, nodes):
        if current_node:
            self._inorder_traversal(current_node.left, nodes)
            nodes.append(current_node.value)
            self._inorder_traversal(current_node.right, nodes)

# Exemplo de uso
if __name__ == "__main__":
    tree = AVLTree()  # Cria uma instância da árvore AVL
    tree.insert(10)  # Insere o valor 10
    tree.insert(20)  # Insere o valor 20
    tree.insert(30)  # Insere o valor 30
    tree.insert(40)  # Insere o valor 40
    tree.insert(50)  # Insere o valor 50
    tree.insert(25)  # Insere o valor 25

    # Imprime os valores em ordem crescente usando a travessia em ordem
    print("Inorder Traversal:")
    print(tree.inorder_traversal())