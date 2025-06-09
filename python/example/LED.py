# Lista Duplamente Encadeada (LED) em Python
# Classe que representa um nó da lista duplamente encadeada
class Node:
    def __init__(self, value):
        self.value = value    # Valor armazenado no nó
        self.prev = None      # Ponteiro para o nó anterior
        self.next = None      # Ponteiro para o próximo nó


# Classe que representa a lista duplamente encadeada
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Ponteiro para o primeiro nó da lista
        self.tail = None  # Ponteiro para o último nó da lista

    def is_empty(self):
        # Verifica se a lista está vazia
        return self.head is None

    def insert_first(self, value):
        # Insere um novo nó no início da lista
        new_node = Node(value)
        if self.is_empty():
            # Se a lista estiver vazia, head e tail apontam para o novo nó
            self.head = self.tail = new_node
        else:
            # Conecta o novo nó ao antigo head
            new_node.next = self.head
            self.head.prev = new_node
            # Atualiza o head para o novo nó
            self.head = new_node

    def insert_last(self, value):
        # Insere um novo nó no final da lista
        new_node = Node(value)
        if self.is_empty():
            # Se a lista estiver vazia, head e tail apontam para o novo nó
            self.head = self.tail = new_node
        else:
            # Conecta o novo nó ao antigo tail
            new_node.prev = self.tail
            self.tail.next = new_node
            # Atualiza o tail para o novo nó
            self.tail = new_node


    def remove(self, value):
        # Remove o primeiro nó que contém o valor especificado
        if self.is_empty():
            print("Lista vazia.")
            return

        current = self.head
        while current:
            if current.value == value:
                # Caso o nó a ser removido seja o head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        # Se a lista ficou vazia após a remoção
                        self.tail = None
                # Caso o nó seja o tail
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                # Caso o nó esteja no meio da lista
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return  # Sai após remover o primeiro nó com valor correspondente
            current = current.next

        print(f"Valor {value} não encontrado.")  # Se não encontrar o valor


    def search(self, value):
        # Busca por um valor na lista e retorna o nó, se encontrado
        current = self.head
        while current:
            if current.value == value:
                return current  # Retorna o nó se encontrado
            current = current.next
        return None  # Valor não encontrado

    def display_forward(self):
        # Exibe os valores da lista do início ao fim
        current = self.head
        print("Início -> Fim:", end=" ")
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")  # Indica o fim da lista


    def display_backward(self):
        # Exibe os valores da lista do fim ao início
        current = self.tail
        print("Fim -> Início:", end=" ")
        while current:
            print(current.value, end=" <-> ")
            current = current.prev
        print("None")  # Indica o início da lista (fim da exibição invertida)



if __name__ == "__main__":
    lista = DoublyLinkedList()       # Cria uma nova lista duplamente encadeada

    lista.insert_last(10)            # Insere 10 no final
    lista.insert_last(20)            # Insere 20 no final
    lista.insert_first(5)            # Insere 5 no início
    lista.display_forward()          # Deve exibir: 5 <-> 10 <-> 20 <-> None
    lista.display_backward()         # Deve exibir: 20 <-> 10 <-> 5 <-> None

    lista.remove(10)                 # Remove o nó com valor 10
    lista.display_forward()          # Agora: 5 <-> 20 <-> None

    # Busca por elementos
    print("Busca 20:", "Encontrado" if lista.search(20) else "Não encontrado")
    print("Busca 100:", "Encontrado" if lista.search(100) else "Não encontrado")
