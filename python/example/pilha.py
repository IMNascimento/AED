class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def is_empty(self):
        return self.top is None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            print("Pilha vazia.")
            return None
        value = self.top.value
        self.top = self.top.next
        self._size -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def size(self):
        return self._size

    def display(self):
        current = self.top
        print("Topo -> Base:", end=" ")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")



if __name__ == "__main__":
    pilha = Stack()
    pilha.push(10)
    pilha.push(20)
    pilha.push(30)
    pilha.display()          # Topo -> Base: 30 -> 20 -> 10 -> None

    print("Topo da pilha:", pilha.peek())  # 30

    print("Pop:", pilha.pop())             # Remove 30
    pilha.display()                        # Topo -> Base: 20 -> 10 -> None

    print("Tamanho:", pilha.size())        # 2
