class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Fila:
    def __init__(self):
        self.head = None
        self.tail = None

    def contido(self, k):
        atual = self.head
        while atual:
            if atual.val == k:
                return True
            atual = atual.next
        return False  # O(n)

    def inserir(self, k):
        novo = Node(k)
        if not self.tail:
            self.head = self.tail = novo
        else:
            self.tail.next = novo
            self.tail = novo  # O(1)

    def remover(self):
        if not self.head:
            return None
        valor = self.head.val
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return valor  # O(1)
