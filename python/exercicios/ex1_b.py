# Nó da lista simplesmente encadeada
class Node:
    def __init__(self, value):
        self.value = value       # Valor do nó
        self.next = None         # Próximo nó

# Fila com head (saída) e tail (entrada)
class Fila:
    def __init__(self):
        self.head = None         # Início da fila (de onde sai)
        self.tail = None         # Fim da fila (onde entra)

    def contido(self, K):
        # Verifica se o valor K está na fila
        current = self.head
        while current:
            if current.value == K:
                return True
            current = current.next
        return False  # O(n)

    def inserir(self, K):
        # Enfileira o valor K no final
        new_node = Node(K)
        if not self.head:
            # Fila vazia: head e tail apontam para o novo nó
            self.head = self.tail = new_node
        else:
            # tail aponta para o novo e o novo se torna o novo tail
            self.tail.next = new_node
            self.tail = new_node
        # O(1)

    def remover(self):
        # Remove o valor do início da fila
        if not self.head:
            print("Fila vazia.")
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None  # Se ficou vazia, tail também zera
        return value
        # O(1)