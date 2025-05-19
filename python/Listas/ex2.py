class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def contido(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def inserir(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remover(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False

def soma_grandes(L1, L2):
    carry = 0
    resultado = DoublyLinkedList()

    # Adicionamos None no final para facilitar a iteração até o último nó
    L1.inserir(None)
    L2.inserir(None)

    # Começamos pelo início das listas, que representam os dígitos menos significativos
    current_L1 = L1.head
    current_L2 = L2.head
    
    while current_L1.value is not None or current_L2.value is not None or carry:
        val1 = current_L1.value if current_L1.value is not None else 0
        val2 = current_L2.value if current_L2.value is not None else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        resultado.inserir(total % 10)
        
        if current_L1.value is not None:
            current_L1 = current_L1.next
        if current_L2.value is not None:
            current_L2 = current_L2.next
    
    # Removemos os None do final das listas
    L1.remover(None)
    L2.remover(None)
    resultado.remover(None)
    
    return resultado




# Exemplo de execução para o Exercício 2 (Soma de Dois Inteiros Grandes)
# A implementação assume que os métodos necessários estão corretamente definidos como discutido anteriormente.

# Lista para armazenar os dígitos dos números grandes. Usaremos a lista duplamente encadeada definida anteriormente.

L1 = DoublyLinkedList()
L2 = DoublyLinkedList()
for digit in [1, 2, 3]:  # Representa o número 321
    L1.inserir(digit)
for digit in [4, 5, 6]:  # Representa o número 654
    L2.inserir(digit)

# Digamos que L1 representa o número 123 e L2 representa o número 456
L3 = soma_grandes(L1, L2)
current = L3.head
while current:
    print(current.value, end=" ")  # Esperado: 579 (para 123 + 456 = 579)
    current = current.next