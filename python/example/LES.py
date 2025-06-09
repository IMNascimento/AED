#lista encadeada simples
# Classe que representa um nó da lista
class Node:
    def __init__(self, value):
        self.value = value  # valor armazenado no nó
        self.next = None    # ponteiro para o próximo nó (inicialmente nenhum)

# Classe que representa a Lista Encadeada Simples
class SinglyLinkedList:
    def __init__(self):
        self.head = None  # início da lista (cabeça)

    def is_empty(self):
        # Verifica se a lista está vazia (não tem nenhum nó)
        return self.head is None

    def insert_first(self, value):
        # Insere um novo nó no início da lista
        new_node = Node(value)       # Cria novo nó com o valor
        new_node.next = self.head    # Aponta o novo nó para o antigo primeiro nó
        self.head = new_node         # Atualiza o head para ser o novo nó

    def insert_last(self, value):
        # Insere um novo nó no final da lista
        new_node = Node(value)       
        if self.is_empty():
            # Se a lista estiver vazia, o novo nó vira o head
            self.head = new_node
            return

        # Caso contrário, percorre até o último nó
        current = self.head
        while current.next:
            current = current.next

        # O último nó agora aponta para o novo nó
        current.next = new_node

    def remove(self, value):
        # Remove o primeiro nó com o valor especificado
        if self.is_empty():
            print("Lista vazia. Nada para remover.")
            return

        if self.head.value == value:
            # Se o valor estiver no primeiro nó (head), atualiza o head
            self.head = self.head.next
            return

        # Percorre a lista com dois ponteiros: prev e current
        prev = self.head
        current = self.head.next
        while current:
            if current.value == value:
                # Conecta o anterior ao próximo do atual, removendo o nó
                prev.next = current.next
                return
            prev = current
            current = current.next

        # Valor não encontrado
        print(f"Valor {value} não encontrado na lista.")


    def search(self, value):
        # Busca um nó com o valor especificado
        current = self.head
        while current:
            if current.value == value:
                return current  # Encontrado
            current = current.next
        return None  # Não encontrado

    def display(self):
        # Exibe os valores da lista
        current = self.head
        if not current:
            print("Lista vazia.")
            return
        print("Lista:", end=" ")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")  # Marca o fim da lista

if __name__ == "__main__":
    lista = SinglyLinkedList()         # Cria nova lista

    lista.insert_last(10)              # Insere 10 no final
    lista.insert_last(20)              # Insere 20 no final
    lista.insert_first(5)              # Insere 5 no início
    lista.display()                    # Exibe: 5 -> 10 -> 20 -> None

    lista.remove(10)                   # Remove o valor 10
    lista.display()                    # Exibe: 5 -> 20 -> None

    print("Busca 20:", "Encontrado" if lista.search(20) else "Não encontrado")  # Encontrado
    print("Busca 15:", "Encontrado" if lista.search(15) else "Não encontrado")  # Não encontrado