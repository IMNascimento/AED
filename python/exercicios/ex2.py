class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_list(head):
    prev = None
    atual = head
    while atual:
        prox = atual.next
        atual.next = prev
        prev = atual
        atual = prox
    return prev

def add_big_numbers(l1, l2):
    # Inverte as listas
    l1 = reverse_list(l1)
    l2 = reverse_list(l2)

    carry = 0
    dummy = Node(0)
    atual = dummy

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        atual.next = Node(total % 10)
        atual = atual.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    # Resultado está invertido, inverter de volta
    return reverse_list(dummy.next)

# Funções utilitárias para criar e imprimir listas
def create_list_from_digits(digits):
    head = None
    for d in digits:
        novo = Node(int(d))
        novo.next = head
        head = novo
    return reverse_list(head)

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    return ''.join(res)

# Exemplo de uso
if __name__ == "__main__":
    num1 = create_list_from_digits("987654321")
    num2 = create_list_from_digits("123456789")

    resultado = add_big_numbers(num1, num2)
    print("Resultado da soma:", print_list(resultado))  # 1111111110
