class Node:
    def __init__(self, value):
        self.value = value  # Atribui o valor do nó
        self.children = []  # Inicializa a lista de filhos como vazia

class NaryTree:
    def __init__(self):
        self.root = None  # Inicializa a raiz da árvore como None

    def insert(self, parent_value, value):
        # Insere um valor na árvore, buscando o nó pai com parent_value
        if self.root is None:
            # Se a árvore estiver vazia, o novo valor se torna a raiz
            self.root = Node(value)
        else:
            # Caso contrário, chama o método _insert para encontrar o nó pai
            parent_node = self._search(self.root, parent_value)
            if parent_node:
                # Adiciona o novo nó como filho do nó pai
                parent_node.children.append(Node(value))
            else:
                print(f"Nó pai com valor {parent_value} não encontrado.")

    def _search(self, current_node, value):
        # Método auxiliar para buscar um nó com valor específico de forma recursiva
        if current_node.value == value:
            return current_node
        for child in current_node.children:
            result = self._search(child, value)
            if result:
                return result
        return None

    def pre_order_traversal(self):
        # Retorna uma lista com os valores dos nós em ordem pre-order
        nodes = []
        self._pre_order_traversal(self.root, nodes)
        return nodes

    def _pre_order_traversal(self, current_node, nodes):
        # Método auxiliar para fazer a travessia pre-order de forma recursiva
        if current_node:
            # Adiciona o valor do nó atual à lista
            nodes.append(current_node.value)
            # Visita cada filho recursivamente
            for child in current_node.children:
                self._pre_order_traversal(child, nodes)

# Exemplo de uso
if __name__ == "__main__":
    tree = NaryTree()  # Cria uma instância da árvore N-ária
    tree.insert(None, 1)  # Insere o valor 1 como raiz
    tree.insert(1, 2)  # Insere o valor 2 como filho do nó com valor 1
    tree.insert(1, 3)  # Insere o valor 3 como filho do nó com valor 1
    tree.insert(1, 4)  # Insere o valor 4 como filho do nó com valor 1
    tree.insert(2, 5)  # Insere o valor 5 como filho do nó com valor 2
    tree.insert(2, 6)  # Insere o valor 6 como filho do nó com valor 2
    tree.insert(3, 7)  # Insere o valor 7 como filho do nó com valor 3
    tree.insert(3, 8)  # Insere o valor 8 como filho do nó com valor 3

    # Imprime os valores em ordem pre-order
    print("Pre-order Traversal:")
    print(tree.pre_order_traversal())