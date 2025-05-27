class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



class ListaCircular:
    def __init__(self):
        self.head = None

    def contido(self, k):
        if not self.head:
            return False
        atual = self.head
        while True:
            if atual.val == k:
                return True
            atual = atual.next
            if atual == self.head:
                break
        return False  # O(n)

    def inserir(self, k):
        novo = NodeD(k)
        if not self.head:
            novo.next = novo.prev = novo
            self.head = novo
        else:
            tail = self.head.prev
            tail.next = novo
            novo.prev = tail
            novo.next = self.head
            self.head.prev = novo  # O(1)

    def remover(self, k):
        if not self.head:
            return False
        atual = self.head
        while True:
            if atual.val == k:
                if atual.next == atual:  # único elemento
                    self.head = None
                else:
                    atual.prev.next = atual.next
                    atual.next.prev = atual.prev
                    if atual == self.head:
                        self.head = atual.next
                return True
            atual = atual.next
            if atual == self.head:
                break
        return False  # O(n)
