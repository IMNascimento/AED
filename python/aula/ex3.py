
class Queue:
    def __init__(self, items=None):
        items = items or []
        self._items = items

    def enqueue(self, item):
        """Adiciona um elemento no final da fila"""
        self._items.append(item)

    def dequeue(self):
        """Remove e retorna o elemento da frente"""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def peek(self):
        """Retorna o elemento da frente sem remover"""
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self):
        """Verifica se a fila está vazia"""
        return len(self._items) == 0

    def size(self):
        """Retorna o número de elementos na fila"""
        return len(self._items)

    def __repr__(self):
        return f"Queue({self._items})"

def merge_queues(q1, q2):
    merged = Queue()
    while not q1.is_empty() or not q2.is_empty():
        if not q1.is_empty():
            merged.enqueue(q1.dequeue())
        if not q2.is_empty():
            merged.enqueue(q2.dequeue())
    return merged

if __name__ == "__main__":
    
    q1 = Queue(['a', 'b', 'c'])
    q2 = Queue(['d', 'e', 'f'])

    merged_queue = merge_queues(q1, q2)
    print("Fila resultado:", merged_queue._items)

    q1 = Queue(['a'])
    q2 = Queue(['d', 'e', 'f'])

    merged_queue = merge_queues(q1, q2)
    print("Fila resultado:", merged_queue._items)
