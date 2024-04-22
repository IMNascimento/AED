class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def build_list(values):
    """Constrói uma lista encadeada a partir de uma lista de valores e retorna a cabeça da lista."""
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
    """Imprime os valores de uma lista encadeada."""
    current = head
    while current:
        print(current.value, end=' ')
        current = current.next
    print()  # Nova linha para separar as saídas


def invert_list(head):
    """ Inverte uma lista encadeada e retorna a nova cabeça da lista invertida. """
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def sum_opposite_elements(head):
    """Soma os elementos opostos de uma lista encadeada e retorna uma nova lista com os resultados na ordem inversa."""
    size = 0
    current = head
    while current:
        size += 1
        current = current.next
    
    # Para calcular a metade da lista
    half_size = size // 2
    
    # Criamos uma lista para armazenar os primeiros n/2 elementos
    first_half = []
    current = head
    for _ in range(half_size):
        first_half.append(current.value)
        current = current.next
    
    # Agora calculamos as somas e criamos a nova lista L'' na ordem inversa
    sum_list_head = None
    for i in range(half_size):
        summed_value = first_half[half_size - 1 - i] + current.value
        new_node = ListNode(summed_value)
        new_node.next = sum_list_head
        sum_list_head = new_node
        current = current.next
    
    return sum_list_head








# Primeiro, crie a lista para inversão EX3-A
values_for_inversion = [1, 2, 3, 4, 5, 6]
list_head_for_inversion = build_list(values_for_inversion)

# Invertendo a lista
inverted_list_head = invert_list(list_head_for_inversion)

print("Exercício 3A: Inversão de Lista")
print("Lista original:")
print_list(build_list(values_for_inversion))  # Recriando a lista para mostrar
print("Lista invertida:")
print_list(inverted_list_head)  # Deve mostrar 6 5 4 3 2 1

# Recriando a lista original para somar elementos opostos EX3-B
values_for_sum_opposites = [1, 2, 3, 4, 5, 6]
list_head_for_sum_opposites = build_list(values_for_sum_opposites)

# Somando os elementos opostos
resulting_list_from_sum_opposites = sum_opposite_elements(list_head_for_sum_opposites)

print("Exercício 3B: Soma de Elementos Opostos")
print("Lista original:")
print_list(build_list(values_for_sum_opposites))  # Recriando a lista para mostrar
print("Lista resultante da soma dos elementos opostos:")
print_list(resulting_list_from_sum_opposites)  # Deve mostrar 7 7 7