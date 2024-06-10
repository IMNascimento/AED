class Node:
    def __init__(self, data):
        self.data = data  # Dado armazenado no nó
        self.next = None  # Ponteiro para o próximo nó na lista

class LinkedList:
    def __init__(self):
        self.head = None  # Inicializa a lista encadeada com a cabeça como None

    def insert_at_beginning(self, data):
        # Insere um novo nó no início da lista
        new_node = Node(data)  # Cria um novo nó com o dado fornecido
        new_node.next = self.head  # O próximo nó do novo nó é a cabeça atual
        self.head = new_node  # A cabeça da lista agora é o novo nó

    def insert_at_end(self, data):
        # Insere um novo nó no final da lista
        new_node = Node(data)  # Cria um novo nó com o dado fornecido
        if self.head is None:
            self.head = new_node  # Se a lista estiver vazia, o novo nó é a cabeça
            return
        last = self.head
        while last.next:
            last = last.next  # Percorre a lista até o último nó
        last.next = new_node  # Define o próximo do último nó como o novo nó

    def delete_node(self, key):
        # Remove o primeiro nó que contém o dado fornecido
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next  # Muda a cabeça para o próximo nó
                temp = None  # Libera o nó removido
                return

        while temp is not None:
            if temp.next is not None and temp.next.data == key:
                break
            temp = temp.next

        if temp is None or temp.next is None:
            return

        next_node = temp.next.next
        temp.next = None
        temp.next = next_node

    def search(self, key):
        # Procura por um nó que contém o dado fornecido
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        # Exibe todos os elementos na lista encadeada
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("LinkedList:", elements)

# Exemplo de uso
if __name__ == "__main__":
    linked_list = LinkedList()

    linked_list.insert_at_beginning(1)
    linked_list.insert_at_beginning(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(4)
    linked_list.display()  # Exibe a lista encadeada

    print("Search for 3:", linked_list.search(3))  # Deve retornar True
    print("Search for 5:", linked_list.search(5))  # Deve retornar False

    linked_list.delete_node(2)  # Remove o nó com o dado 2
    linked_list.display()  # Exibe a lista encadeada após a remoção