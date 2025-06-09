#Para cada estrutura abaixo, implementa os métodos contido(K,L), inserir(K,L) e remover(K,L) e
#verifique as complexidades de cada método. No caso de filas e pilhas, o remover(K,L) não terá o
#argumento K, visto que filas e pilhas removem sempre quem está na extremidade.
#a) Lista duplamente encadeada: considere a inserção sempre no final da lista
#b) Fila com lista simplesmente encadeada: considere que vc tem uma variável head e uma
#tail, onde head marca a cabeça e tail o ultimo nó na cauda.
#c) Pilha com lista simplesmente encadeada
#d) Lista duplamente encadeada circular

# Nó da lista duplamente encadeada
class Node:
    def __init__(self, value):
        self.value = value       # Valor armazenado no nó
        self.prev = None         # Ponteiro para o nó anterior
        self.next = None         # Ponteiro para o próximo nó

# Lista Duplamente Encadeada com inserção no final
class ListaDuplamenteEncadeada:
    def __init__(self):
        self.head = None         # Início da lista
        self.tail = None         # Fim da lista

    def contido(self, K):
        # Verifica se o valor K está na lista
        current = self.head
        while current:
            if current.value == K:
                return True
            current = current.next
        return False  # O(n)

    def inserir(self, K):
        # Insere o valor K no final da lista
        new_node = Node(K)
        if not self.head:
            # Lista vazia: head e tail apontam para o novo nó
            self.head = self.tail = new_node
        else:
            # Liga o novo nó após o tail e atualiza o tail
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        # O(1)

    def remover(self, K):
        # Remove o primeiro nó que contém o valor K
        current = self.head
        while current:
            if current.value == K:
                if current == self.head:
                    # Remoção no início
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    # Remoção no fim
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    # Remoção no meio
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
        # O(n)