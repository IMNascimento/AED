class Stack:
    """
    Implementação simples de pilha usando lista interna em Python.
    Métodos:
      - push(item): adiciona item ao topo
      - pop(): remove e retorna o item do topo
      - peek(): retorna o item do topo sem remover
      - is_empty(): verifica se a pilha está vazia
      - size(): retorna o número de elementos
    """
    def __init__(self):
        self._items = []

    def push(self, item):
        """Adiciona um elemento ao topo da pilha"""
        self._items.append(item)

    def pop(self):
        """Remove e retorna o elemento do topo"""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Retorna o elemento do topo sem remover"""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Verifica se a pilha está vazia"""
        return len(self._items) == 0

    def size(self):
        """Retorna o número de elementos na pilha"""
        return len(self._items)

    def __repr__(self):
        return f"Stack(top -> {list(reversed(self._items))})"

#seja uma string verifique se ela é um polindrome
def is_palindrome(s):
    pilha = Stack()
    s = s.replace(" ", "").lower()  # Remove espaços e converte para minúsculas 
    for c in s:
        pilha.push(c)
    for c in s:
        if pilha.pop() != c:
            return False


    return True

string  = input("Digite uma string: ")

if is_palindrome(string):
    print(f"A string '{string}' é um palíndromo.")
else:   
    print(f"A string '{string}' não é um palíndromo.")


