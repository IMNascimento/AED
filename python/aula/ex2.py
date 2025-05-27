#verifique se uma expressão em uma linguagem de programação é valida por seus parenteses e colchetes e etc: exemplo s=t[s]+u/(v*(w+y))

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
    

def is_valid_expression(expr):
    pilha = Stack()


  
    
    for char in expr:
        if char == '(':
            pilha.push(char)
        elif char == ')':
            if pilha.is_empty() or pilha.pop() != '(':
                return False
        elif char == '{':
            pilha.push(char)
        elif char == '}':
            if pilha.is_empty() or pilha.pop() != '{':
                return False
        elif char == '[':
            pilha.push(char)
        elif char == ']':
            if pilha.is_empty() or pilha.pop() != '[':
                return False
        
    
    return pilha.is_empty()  # Retorna True se todos os delimitadores foram fechados corretamente



# Exemplo de uso
if __name__ == "__main__":
    expression = input("Digite uma expressão: ")
    
    if is_valid_expression(expression):
        print(f"A expressão '{expression}' é válida.")
    else:
        print(f"A expressão '{expression}' não é válida.")  