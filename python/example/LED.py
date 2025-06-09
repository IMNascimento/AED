# Lista Duplamente Encadeada (LED) em Python
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, value):
        if self.is_empty():
            print("Lista vazia.")
            return

        current = self.head
        while current:
            if current.value == value:
                # Remoção na cabeça
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                # Remoção na cauda
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                # Remoção no meio
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next
        print(f"Valor {value} não encontrado.")

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def display_forward(self):
        current = self.head
        print("Início -> Fim:", end=" ")
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

    def display_backward(self):
        current = self.tail
        print("Fim -> Início:", end=" ")
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")


if __name__ == "__main__":
    lista = DoublyLinkedList()
    lista.insert_last(10)
    lista.insert_last(20)
    lista.insert_first(5)
    lista.display_forward()    # Início -> Fim: 5 <-> 10 <-> 20 <-> None
    lista.display_backward()   # Fim -> Início: 20 <-> 10 <-> 5 <-> None

    lista.remove(10)
    lista.display_forward()    # Início -> Fim: 5 <-> 20 <-> None

    print("Busca 20:", "Encontrado" if lista.search(20) else "Não encontrado")
    print("Busca 100:", "Encontrado" if lista.search(100) else "Não encontrado")