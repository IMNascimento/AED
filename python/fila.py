class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        """Adiciona um elemento ao topo da pilha"""
        self._items.append(item)

    def pop(self):
        """Remove e retorna o elemento do topo"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Retorna o elemento do topo sem remover"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Verifica se a pilha está vazia"""
        return len(self._items) == 0

    def size(self):
        """Retorna o número de elementos na pilha"""
        return len(self._items)

    def __repr__(self):
        return f"Stack({self._items})"


class Queue:
    def __init__(self):
        self._items = []

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


if __name__ == "__main__":
    # Teste da pilha
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Pilha após pushes:", stack)
    print("pop():", stack.pop())
    print("peek():", stack.peek())
    print("Está vazia?", stack.is_empty())
    print("Tamanho:", stack.size())
    print()

    # Teste da fila
    queue = Queue()
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    print("Fila após enqueues:", queue)
    print("dequeue():", queue.dequeue())
    print("peek():", queue.peek())
    print("Está vazia?", queue.is_empty())
    print("Tamanho:", queue.size())
