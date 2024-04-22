class CircularDoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def contido(self, value):
        if not self.head:
            return False
        current = self.head
        while True:
            if current.value == value:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def inserir(self, value):
        new_node = CircularDoublyLinkedListNode(value)
        if not self.head:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def remover(self, value):
        if not self.head:
            return False
        
        current = self.head
        while True:
            if current.value == value:
                if current.next == current:  # Only one node in the list
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:  # If the head is to be removed
                        self.head = current.next
                return True
            current = current.next
            if current == self.head:
                break
        return False
    
cdll = CircularDoublyLinkedList()
cdll.inserir('A')
cdll.inserir('B')
cdll.inserir('C')
exercicio_1d_contido = cdll.contido('B')  # Deve retornar True
cdll.remover('B')
exercicio_1d_contido_after_removal = cdll.contido('B')  # Deve retornar False

print(exercicio_1d_contido)
print(exercicio_1d_contido_after_removal)