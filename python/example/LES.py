#lista encadeada simples
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_last(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove(self, value):
        if self.is_empty():
            print("Lista vazia. Nada para remover.")
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        prev = self.head
        current = self.head.next
        while current:
            if current.value == value:
                prev.next = current.next
                return
            prev = current
            current = current.next

        print(f"Valor {value} não encontrado na lista.")

    def search(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def display(self):
        current = self.head
        if not current:
            print("Lista vazia.")
            return
        print("Lista:", end=" ")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

if __name__ == "__main__":
    lista = SinglyLinkedList()
    lista.insert_last(10)
    lista.insert_last(20)
    lista.insert_first(5)
    lista.display()  # 5 -> 10 -> 20 -> None

    lista.remove(10)
    lista.display()  # 5 -> 20 -> None

    print("Busca 20:", "Encontrado" if lista.search(20) else "Não encontrado")
    print("Busca 15:", "Encontrado" if lista.search(15) else "Não encontrado")