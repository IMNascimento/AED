# Nó da lista circular
class Node:
    def __init__(self, value):
        self.value = value       # Valor do nó
        self.prev = None         # Nó anterior
        self.next = None         # Próximo nó

# Lista Duplamente Encadeada Circular
class ListaDuplamenteCircular:
    def __init__(self):
        self.head = None         # Início da lista

    def contido(self, K):
        # Verifica se K está na lista circular
        if not self.head:
            return False
        current = self.head
        while True:
            if current.value == K:
                return True
            current = current.next
            if current == self.head:
                break
        return False  # O(n)

    def inserir(self, K):
        # Insere K no final da lista
        new_node = Node(K)
        if not self.head:
            # Lista vazia: aponta para si mesmo nos dois sentidos
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            # Insere entre tail e head
            tail = self.head.prev
            new_node.prev = tail
            new_node.next = self.head
            tail.next = new_node
            self.head.prev = new_node
        # O(1)

    def remover(self, K):
        # Remove o primeiro nó com valor K
        if not self.head:
            return
        current = self.head
        while True:
            if current.value == K:
                if current.next == current:
                    # Só 1 elemento
                    self.head = None
                else:
                    # Remove atualizando os vizinhos
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                return
            current = current.next
            if current == self.head:
                break
        # O(n)