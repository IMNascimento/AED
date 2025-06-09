# Classe que representa um nó da pilha
class Node:
    def __init__(self, value):
        self.value = value    # Valor armazenado no nó
        self.next = None      # Ponteiro para o próximo nó (abaixo na pilha)

# Classe que representa a pilha (estrutura LIFO)
class Stack:
    def __init__(self):
        self.top = None       # Ponteiro para o topo da pilha
        self._size = 0        # Contador de elementos na pilha

    def is_empty(self):
        # Retorna True se a pilha estiver vazia
        return self.top is None

    def push(self, value):
        # Insere um novo valor no topo da pilha
        new_node = Node(value)    # Cria um novo nó com o valor dado
        new_node.next = self.top  # Aponta o novo nó para o antigo topo
        self.top = new_node       # Atualiza o topo da pilha para o novo nó
        self._size += 1           # Incrementa o tamanho da pilha

    def pop(self):
        # Remove e retorna o valor do topo da pilha
        if self.is_empty():
            print("Pilha vazia.")
            return None
        value = self.top.value        # Armazena o valor do topo
        self.top = self.top.next      # Move o topo para o próximo nó
        self._size -= 1               # Decrementa o tamanho
        return value                  # Retorna o valor removido

    def peek(self):
        # Retorna o valor do topo da pilha sem remover
        if self.is_empty():
            return None
        return self.top.value

    def size(self):
        # Retorna a quantidade de elementos na pilha
        return self._size

    def display(self):
        # Exibe os elementos da pilha do topo à base
        current = self.top
        print("Topo -> Base:", end=" ")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")  # Indica o final da pilha

# Bloco principal de testes
if __name__ == "__main__":
    pilha = Stack()                # Cria uma nova pilha vazia
    pilha.push(10)                 # Insere 10 no topo
    pilha.push(20)                 # Insere 20 no topo
    pilha.push(30)                 # Insere 30 no topo
    pilha.display()               # Exibe: 30 -> 20 -> 10 -> None

    print("Topo da pilha:", pilha.peek())  # Mostra o topo: 30

    print("Pop:", pilha.pop())             # Remove e exibe o topo: 30
    pilha.display()                        # Agora: 20 -> 10 -> None

    print("Tamanho:", pilha.size())        # Tamanho atual: 2