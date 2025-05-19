class Node:
    def __init__(self, value):
        self.value = value  # Atribui o valor do nó
        self.left = None  # Inicializa o ponteiro para o filho à esquerda como None
        self.right = None  # Inicializa o ponteiro para o filho à direita como None

class BinaryTree:
    def __init__(self):
        self.root = None  # Inicializa a raiz da árvore como None

    def insert(self, value):
        # Insere um valor na árvore
        if self.root is None:
            # Se a árvore estiver vazia, o novo valor se torna a raiz
            self.root = Node(value)
        else:
            # Caso contrário, chama o método _insert para encontrar a posição correta
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        # Método auxiliar para inserir um valor na árvore de forma recursiva
        if value < current_node.value:
            # Se o valor a ser inserido é menor que o valor do nó atual
            if current_node.left is None:
                # Se o filho à esquerda estiver vazio, insere o novo valor lá
                current_node.left = Node(value)
            else:
                # Caso contrário, continua a busca recursivamente no filho à esquerda
                self._insert(current_node.left, value)
        elif value > current_node.value:
            # Se o valor a ser inserido é maior que o valor do nó atual
            if current_node.right is None:
                # Se o filho à direita estiver vazio, insere o novo valor lá
                current_node.right = Node(value)
            else:
                # Caso contrário, continua a busca recursivamente no filho à direita
                self._insert(current_node.right, value)

    def search(self, value):
        # Busca um valor na árvore
        return self._search(self.root, value)

    def _search(self, current_node, value):
        # Método auxiliar para buscar um valor na árvore de forma recursiva
        if current_node is None:
            # Se o nó atual é None, o valor não foi encontrado
            return None
        elif current_node.value == value:
            # Se o valor do nó atual é igual ao valor procurado, retorna o nó atual
            return current_node
        elif value < current_node.value:
            # Se o valor procurado é menor, continua a busca no filho à esquerda
            return self._search(current_node.left, value)
        else:
            # Se o valor procurado é maior, continua a busca no filho à direita
            return self._search(current_node.right, value)

    def remove(self, value):
        # Remove um valor da árvore
        self.root = self._remove(self.root, value)

    def _remove(self, current_node, value):
        # Método auxiliar para remover um valor da árvore de forma recursiva
        if current_node is None:
            # Se o nó atual é None, o valor não foi encontrado
            return current_node
        if value < current_node.value:
            # Se o valor a ser removido é menor, continua a busca no filho à esquerda
            current_node.left = self._remove(current_node.left, value)
        elif value > current_node.value:
            # Se o valor a ser removido é maior, continua a busca no filho à direita
            current_node.right = self._remove(current_node.right, value)
        else:
            # Se o nó atual é o nó a ser removido
            if current_node.left is None:
                # Caso 1: nó com apenas um filho à direita ou nenhum filho
                return current_node.right
            elif current_node.right is None:
                # Caso 2: nó com apenas um filho à esquerda
                return current_node.left
            # Caso 3: nó com dois filhos
            temp = self._min_value_node(current_node.right)
            current_node.value = temp.value
            current_node.right = self._remove(current_node.right, temp.value)
        return current_node

    def _min_value_node(self, node):
        # Método auxiliar para encontrar o nó com o menor valor
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        # Retorna uma lista com os valores dos nós em ordem crescente
        nodes = []
        self._inorder_traversal(self.root, nodes)
        return nodes

    def _inorder_traversal(self, current_node, nodes):
        # Método auxiliar para fazer a travessia em ordem (in-order) de forma recursiva
        if current_node:
            # Primeiro, visita o filho à esquerda
            self._inorder_traversal(current_node.left, nodes)
            # Depois, adiciona o valor do nó atual à lista
            nodes.append(current_node.value)
            # Por último, visita o filho à direita
            self._inorder_traversal(current_node.right, nodes)

# Exemplo de uso
if __name__ == "__main__":
    tree = BinaryTree()  # Cria uma instância da árvore binária
    tree.insert(10)  # Insere o valor 10
    tree.insert(5)  # Insere o valor 5
    tree.insert(15)  # Insere o valor 15
    tree.insert(3)  # Insere o valor 3
    tree.insert(7)  # Insere o valor 7
    tree.insert(12)  # Insere o valor 12
    tree.insert(17)  # Insere o valor 17

    # Imprime os valores em ordem crescente usando a travessia em ordem
    print("Inorder Traversal:")
    print(tree.inorder_traversal())

    # Busca por um valor na árvore
    value_to_search = 7
    result = tree.search(value_to_search)
    if result:
        print(f"Valor {value_to_search} encontrado na árvore. {result}")
    else:
        print(f"Valor {value_to_search} não encontrado na árvore. {result}")

    # Remove um valor da árvore
    value_to_remove = 15
    tree.remove(value_to_remove)
    print(f"Inorder Traversal após remover {value_to_remove}:")
    print(tree.inorder_traversal())