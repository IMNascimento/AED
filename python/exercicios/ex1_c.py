# Nó para a pilha
class Node:
    def __init__(self, value):
        self.value = value       # Valor no topo
        self.next = None         # Próximo abaixo na pilha

# Pilha com inserção e remoção no topo
class Pilha:
    def __init__(self):
        self.top = None          # Topo da pilha

    def contido(self, K):
        # Verifica se o valor K está na pilha
        current = self.top
        while current:
            if current.value == K:
                return True
            current = current.next
        return False  # O(n)

    def inserir(self, K):
        # Empilha o valor K no topo
        new_node = Node(K)
        new_node.next = self.top
        self.top = new_node
        # O(1)

    def remover(self):
        # Desempilha o valor do topo
        if not self.top:
            print("Pilha vazia.")
            return None
        value = self.top.value
        self.top = self.top.next
        return value
        # O(1)