class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def build_list(values):
    """ Constrói uma lista encadeada a partir de uma lista de valores e retorna a cabeça da lista. """
    head = None
    current = None
    for value in values:
        new_node = ListNode(value)
        if head is None:
            head = current = new_node
        else:
            current.next = new_node
            current = new_node
    return head

def print_list(head):
    """ Imprime os valores de uma lista encadeada. """
    current = head
    while current:
        print(current.value, end=' ')
        current = current.next
    print()  # Nova linha para separar as saídas

def is_palindrome(head):
    """ Verifica se a lista encadeada é um palíndromo. """
    values = []
    current = head
    while current:
        values.append(current.value)
        current = current.next
    return values == values[::-1]

# Exemplo de uso da função is_palindrome

# Lista que é um palíndromo
palindrome_values = ['r', 'a', 'd', 'a', 'r']
palindrome_list = build_list(palindrome_values)
print("Exercício 4: Lista Palíndroma")
print("Lista original (palíndroma):")
print_list(palindrome_list)
print("É palíndromo?:", is_palindrome(palindrome_list))  # Esperado: True

# Lista que não é um palíndromo
non_palindrome_values = ['h', 'e', 'l', 'l', 'o']
non_palindrome_list = build_list(non_palindrome_values)
print("Lista original (não palíndroma):")
print_list(non_palindrome_list)
print("É palíndromo?:", is_palindrome(non_palindrome_list))  # Esperado: False