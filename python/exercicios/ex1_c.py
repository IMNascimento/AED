class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Pilha:
    def __init__(self):
        self.topo = None

    def contido(self, k):
        atual = self.topo
        while atual:
            if atual.val == k:
                return True
            atual = atual.next
        return False  # O(n)

    def inserir(self, k):
        novo = Node(k)
        novo.next = self.topo
        self.topo = novo  # O(1)

    def remover(self):
        if not self.topo:
            return None
        val = self.topo.val
        self.topo = self.topo.next
        return val  # O(1)
