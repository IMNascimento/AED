# lista duplamente encadeada circular
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_first(self, value):
        new_node = Node(value)
        if self.is_empty():
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def insert_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node

    def remove(self, value):
        if self.is_empty():
            print("Lista vazia.")
            return

        current = self.head
        while True:
            if current.value == value:
                if current.next == current:  # só um nó
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        self.head = current.next
                return
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

    def display_forward(self):
        if self.is_empty():
            print("Lista vazia.")
            return
        print("Início → Fim:", end=" ")
        current = self.head
        while True:
            print(current.value, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("(volta ao início)")

    def display_backward(self):
        if self.is_empty():
            print("Lista vazia.")
            return
        print("Fim → Início:", end=" ")
        current = self.head.prev
        while True:
            print(current.value, end=" <-> ")
            current = current.prev
            if current.next == self.head.prev:
                break
        print("(volta ao fim)")

if __name__ == "__main__":
    lista = CircularDoublyLinkedList()
    lista.insert_last(10)
    lista.insert_last(20)
    lista.insert_first(5)
    lista.display_forward()     # Início → Fim: 5 <-> 10 <-> 20 <-> (volta ao início)
    lista.display_backward()    # Fim → Início: 20 <-> 10 <-> 5 <-> (volta ao fim)

    lista.remove(10)
    lista.display_forward()     # 5 <-> 20 <-> (volta ao início)

    print("Busca 20:", "Encontrado" if lista.search(20) else "Não encontrado")
    print("Busca 999:", "Encontrado" if lista.search(999) else "Não encontrado")
