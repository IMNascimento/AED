class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # Início da fila (saída)
        self.rear = None   # Final da fila (entrada)
        self._size = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            print("Fila vazia.")
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None  # Fila ficou vazia
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.front.value

    def size(self):
        return self._size

    def display(self):
        current = self.front
        print("Início -> Fim:", end=" ")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    fila = Queue()
    fila.enqueue(10)
    fila.enqueue(20)
    fila.enqueue(30)
    fila.display()  # Início -> Fim: 10 -> 20 -> 30 -> None

    print("Frente da fila:", fila.peek())  # 10

    print("Removido:", fila.dequeue())     # Remove 10
    fila.display()                         # Início -> Fim: 20 -> 30 -> None

    print("Tamanho:", fila.size())         # 2
