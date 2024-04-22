class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def contido(self, value):
        current = self.top
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def inserir(self, value):
        new_node = StackNode(value)
        new_node.next = self.top
        self.top = new_node

    def remover(self):
        if not self.top:
            return None
        removed_value = self.top.value
        self.top = self.top.next
        return removed_value
    

# Exemplo de execução para Exercício 1.c:
stack = Stack()
stack.inserir(1)
stack.inserir(2)
stack.inserir(3)
exercicio_1c_contido = stack.contido(2)  # Deve retornar True
exercicio_1c_removido = stack.remover()  # Deve retornar 3
print(exercicio_1c_contido)
print(exercicio_1c_removido)

