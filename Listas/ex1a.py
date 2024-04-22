class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remover(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False
    



# Execução dos exemplos para cada método de cada estrutura de dados
# Lista Duplamente Encadeada
dll = DoublyLinkedList()
dll.inserir('A')
dll.inserir('B')
dll.inserir('C')
dll.remover('B')
print("Contido 'B' após remoção:", dll.contido('B'))  # False