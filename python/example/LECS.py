# Lista Encadeada Cricular Simples (LECS) em Python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            new_node.next = new_node  # aponta para si mesmo
            self.head = new_node
        else:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            new_node.next = self.head
            tail.next = new_node
            self.head = new_node

    def insert_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            new_node.next = new_node
            self.head = new_node
        else:
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            tail.next = new_node
            new_node.next = self.head

    def remove(self, value):
        if self.is_empty():
            print("Lista vazia.")
            return

        current = self.head
        prev = None

        while True:
            if current.value == value:
                if prev:  # não é o primeiro
                    prev.next = current.next
                else:  # é o primeiro
                    if current.next == self.head:
                        # só um elemento
                        self.head = None
                        return
                    # múltiplos elementos
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    self.head = self.head.next
                    tail.next = self.head
                return

            prev = current
            current = current.next
            if current == self.head:
                break

        print(f"Valor {value} não encontrado.")

    def search(self, value):
        if self.is_empty():
            return None

        current = self.head
        while True:
            if current.value == value:
                return current
            current = current.next
            if current == self.head:
                break
        return None

    def display(self):
        if self.is_empty():
            print("Lista vazia.")
            return

        current = self.head
        print("Lista circular:", end=" ")
        while True:
            print(current.value, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(volta ao início)")


if __name__ == "__main__":
    lista = CircularSinglyLinkedList()
    lista.insert_last(10)
    lista.insert_last(20)
    lista.insert_first(5)
    lista.display()  # 5 -> 10 -> 20 -> (volta ao início)

    lista.remove(10)
    lista.display()  # 5 -> 20 -> (volta ao início)

    print("Busca 20:", "Encontrado" if lista.search(20) else "Não encontrado")
    print("Busca 100:", "Encontrado" if lista.search(100) else "Não encontrado")
