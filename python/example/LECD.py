# Lista Duplamente Encadeada Circular em Python

# Classe que representa um nó da lista
class Node:
    def __init__(self, value):
        self.value = value    # Valor armazenado no nó
        self.prev = None      # Ponteiro para o nó anterior
        self.next = None      # Ponteiro para o próximo nó

# Classe que representa a lista duplamente encadeada circular
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None      # Ponteiro para o início da lista

    def is_empty(self):
        # Retorna True se a lista estiver vazia
        return self.head is None

    def insert_first(self, value):
        # Insere um novo nó no início da lista
        new_node = Node(value)
        if self.is_empty():
            # Lista vazia: novo nó aponta para si mesmo nos dois sentidos
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            # Lista com elementos: atualiza os ponteiros do novo nó e do head/tail
            tail = self.head.prev
            new_node.next = self.head         # novo aponta para o antigo head
            new_node.prev = tail              # novo aponta para o tail
            tail.next = new_node              # tail aponta para o novo
            self.head.prev = new_node         # head aponta para o novo como anterior
            self.head = new_node              # atualiza head

    def insert_last(self, value):
        # Insere um novo nó no final da lista
        new_node = Node(value)
        if self.is_empty():
            # Lista vazia: o novo nó aponta para ele mesmo
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            # Atualiza os ponteiros do novo nó e do antigo tail/head
            tail = self.head.prev
            new_node.next = self.head         # novo aponta para o head
            new_node.prev = tail              # novo aponta para o tail
            tail.next = new_node              # tail aponta para novo
            self.head.prev = new_node         # head aponta para novo como anterior

    def remove(self, value):
        # Remove o primeiro nó que tiver o valor especificado
        if self.is_empty():
            print("Lista vazia.")
            return

        current = self.head
        while True:
            if current.value == value:
                if current.next == current:
                    # Caso só tenha um elemento na lista
                    self.head = None
                else:
                    # Atualiza os ponteiros do anterior e próximo
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    if current == self.head:
                        # Se o nó removido for o head, move o head para o próximo
                        self.head = current.next
                return
            current = current.next
            if current == self.head:
                break

        print(f"Valor {value} não encontrado.")

    def search(self, value):
        # Busca por um valor na lista e retorna o nó, se encontrado
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
        # Exibe os elementos da lista do início para o fim
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
        # Exibe os elementos da lista do fim para o início
        if self.is_empty():
            print("Lista vazia.")
            return
        print("Fim → Início:", end=" ")
        current = self.head.prev  # Começa pelo último nó (tail)
        while True:
            print(current.value, end=" <-> ")
            current = current.prev
            if current.next == self.head.prev:
                break
        print("(volta ao fim)")

# Bloco de testes da lista
if __name__ == "__main__":
    lista = CircularDoublyLinkedList()            # Cria lista vazia
    lista.insert_last(10)                         # Insere 10 no final
    lista.insert_last(20)                         # Insere 20 no final
    lista.insert_first(5)                         # Insere 5 no início
    lista.display_forward()                       # Exibe: 5 <-> 10 <-> 20 <-> (volta ao início)
    lista.display_backward()                      # Exibe: 20 <-> 10 <-> 5 <-> (volta ao fim)

    lista.remove(10)                              # Remove o valor 10
    lista.display_forward()                       # Exibe: 5 <-> 20 <-> (volta ao início)

    print("Busca 20:", "Encontrado" if lista.search(20) else "Não encontrado")   # Encontrado
    print("Busca 999:", "Encontrado" if lista.search(999) else "Não encontrado") # Não encontrado