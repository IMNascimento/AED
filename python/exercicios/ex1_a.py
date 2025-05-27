class NodeD:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class ListaDupla:
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
        novo = NodeD(k)
        if not self.head:
            self.head = self.tail = novo
        else:
            self.tail.next = novo
            novo.prev = self.tail
            self.tail = novo  # O(1)

    def remover(self, k):
        atual = self.head
        while atual:
            if atual.val == k:
                if atual.prev:
                    atual.prev.next = atual.next
                else:
                    self.head = atual.next
                if atual.next:
                    atual.next.prev = atual.prev
                else:
                    self.tail = atual.prev
                return True
            atual = atual.next
        return False  # O(n)
