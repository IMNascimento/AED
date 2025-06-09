# Classe que representa um nó da fila
class Node:
    def __init__(self, value):
        self.value = value    # Valor armazenado no nó
        self.next = None      # Ponteiro para o próximo nó

# Classe que representa a fila (estrutura FIFO)
class Queue:
    def __init__(self):
        self.front = None     # Ponteiro para o início da fila (onde os elementos saem)
        self.rear = None      # Ponteiro para o fim da fila (onde os elementos entram)
        self._size = 0        # Contador de elementos na fila

    def is_empty(self):
        # Retorna True se a fila estiver vazia
        return self.front is None

    def enqueue(self, value):
        # Adiciona um novo valor ao final da fila
        new_node = Node(value)      # Cria um novo nó com o valor fornecido
        if self.is_empty():
            # Se a fila estiver vazia, front e rear apontam para o novo nó
            self.front = self.rear = new_node
        else:
            # Liga o último nó atual ao novo nó, e atualiza o rear
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1             # Incrementa o contador de tamanho

    def dequeue(self):
        # Remove e retorna o valor do início da fila
        if self.is_empty():
            print("Fila vazia.")
            return None
        value = self.front.value        # Armazena o valor do nó que será removido
        self.front = self.front.next    # Move o ponteiro do front para o próximo nó
        if self.front is None:
            # Se a fila ficou vazia após a remoção, rear também deve ser None
            self.rear = None
        self._size -= 1                 # Decrementa o contador de tamanho
        return value                    # Retorna o valor removido

    def peek(self):
        # Retorna o valor do início da fila sem remover
        if self.is_empty():
            return None
        return self.front.value

    def size(self):
        # Retorna o número de elementos na fila
        return self._size

    def display(self):
        # Exibe os valores da fila do início ao fim
        current = self.front
        print("Início -> Fim:", end=" ")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")  # Indica o final da fila

# Bloco principal para teste da fila
if __name__ == "__main__":
    fila = Queue()                     # Cria uma nova fila vazia
    fila.enqueue(10)                   # Insere 10 na fila
    fila.enqueue(20)                   # Insere 20 na fila
    fila.enqueue(30)                   # Insere 30 na fila
    fila.display()                     # Exibe: 10 -> 20 -> 30 -> None

    print("Frente da fila:", fila.peek())  # Exibe: 10

    print("Removido:", fila.dequeue())     # Remove e exibe: 10
    fila.display()                         # Exibe: 20 -> 30 -> None

    print("Tamanho:", fila.size())         # Exibe: 2