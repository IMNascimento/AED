# Lista Encadeada Cricular Simples (LECS) em Python
# Classe que representa um nó da lista
class Node:
    def __init__(self, value):
        self.value = value      # Valor armazenado no nó
        self.next = None        # Ponteiro para o próximo nó (inicialmente vazio)

# Classe principal da lista encadeada circular simples
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None        # Ponteiro para o início da lista

    def is_empty(self):
        # Verifica se a lista está vazia
        return self.head is None

    def insert_first(self, value):
        # Insere um novo nó no início da lista
        new_node = Node(value)
        if self.is_empty():
            # Se a lista estiver vazia, o nó aponta para ele mesmo (circularidade)
            new_node.next = new_node
            self.head = new_node
        else:
            # Caso já exista elementos, encontra o último nó (tail)
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            # Atualiza ponteiros: novo nó aponta para o antigo head
            new_node.next = self.head
            # Último nó aponta para o novo head
            tail.next = new_node
            # Atualiza o head para o novo nó
            self.head = new_node

    def insert_last(self, value):
        # Insere um novo nó no final da lista
        new_node = Node(value)
        if self.is_empty():
            # Lista vazia: novo nó aponta para ele mesmo
            new_node.next = new_node
            self.head = new_node
        else:
            # Encontra o último nó (tail)
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            # Novo nó aponta para o head
            new_node.next = self.head
            # Tail aponta para o novo nó
            tail.next = new_node

    def remove(self, value):
        # Remove o primeiro nó com o valor informado
        if self.is_empty():
            print("Lista vazia.")
            return

        current = self.head
        prev = None

        while True:
            if current.value == value:
                if prev:  # Nó a remover não é o head
                    prev.next = current.next
                else:  # Nó a remover é o head
                    if current.next == self.head:
                        # Só existe um elemento
                        self.head = None
                        return
                    # Mais de um elemento: precisa atualizar o tail
                    tail = self.head
                    while tail.next != self.head:
                        tail = tail.next
                    # Novo head é o próximo nó
                    self.head = self.head.next
                    # Tail aponta para o novo head
                    tail.next = self.head
                return
            prev = current
            current = current.next
            if current == self.head:
                break

        print(f"Valor {value} não encontrado.")

    def search(self, value):
        # Busca por um valor na lista e retorna o nó correspondente
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
        # Exibe os elementos da lista circular
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

# Teste da lista encadeada circular simples
if __name__ == "__main__":
    lista = CircularSinglyLinkedList()
    lista.insert_last(10)                               # Insere 10 no final
    lista.insert_last(20)                               # Insere 20 no final
    lista.insert_first(5)                               # Insere 5 no início
    lista.display()                                     # Exibe: 5 -> 10 -> 20 -> (volta ao início)

    lista.remove(10)                                    # Remove o valor 10
    lista.display()                                     # Exibe: 5 -> 20 -> (volta ao início)

    print("Busca 20:", "Encontrado" if lista.search(20) else "Não encontrado")     # Deve encontrar
    print("Busca 100:", "Encontrado" if lista.search(100) else "Não encontrado")   # Não deve encontrar