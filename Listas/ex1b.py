class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def contido(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def inserir(self, value):
        new_node = QueueNode(value)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

    def remover(self):
        if not self.head:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return removed_value
    



# Fila com Lista Simplesmente Encadeada
queue = Queue()
queue.inserir(1)
queue.inserir(2)
queue.inserir(3)
removed = queue.remover()
print("Valor removido da fila:", removed)  # 1
print("Contido '1' após remoção:", queue.contido(1))  # False