#2) Listas são usadas para representar números muito grandes (p.ex, com 1000 dígitos), uma vez
#que seria impossível representá-lo em máquinas de 64bits. Para representar inteiros grandes com
#listas, é usada uma representação em que cada dígito do inteiro é armazenado em um nó da lista.
#Considere duas listas encadeadas L1 e L2 representando números grandes (cada digito por nó).
#Faça um algoritmo que faça a soma de dois inteiros grandes e retorne a lista L3 = L1 + L2.

# Nó de uma lista encadeada
class Node:
    def __init__(self, value):
        self.value = value  # Armazena um dígito
        self.next = None    # Ponteiro para o próximo nó

# Função para adicionar dois números representados por listas encadeadas
def somar_listas(L1, L2):
    p1 = L1  # Ponteiro para a primeira lista
    p2 = L2  # Ponteiro para a segunda lista
    carry = 0  # Vai-um da soma
    head = tail = None  # Início da lista resultado (L3)

    while p1 or p2 or carry:
        # Obtem os valores atuais (ou 0 se a lista acabou)
        val1 = p1.value if p1 else 0
        val2 = p2.value if p2 else 0

        # Soma os dois valores com o carry anterior
        total = val1 + val2 + carry
        carry = total // 10            # Calcula o vai-um
        digit = total % 10             # Dígito a ser armazenado no nó atual

        # Cria o novo nó com o dígito da soma
        new_node = Node(digit)

        if not head:
            # Primeiro nó da lista resultado
            head = tail = new_node
        else:
            # Encadeia o novo nó ao final da lista
            tail.next = new_node
            tail = new_node

        # Avança os ponteiros das listas, se houver próximos nós
        if p1: p1 = p1.next
        if p2: p2 = p2.next

    return head  # Retorna o início da nova lista (soma)

# Função auxiliar para converter um número inteiro (string ou int) em lista encadeada de dígitos
def numero_para_lista(num):
    head = None
    for d in str(num)[::-1]:  # Inverte a string para começar do menor dígito
        node = Node(int(d))
        node.next = head
        head = node
    return head

# Função auxiliar para exibir uma lista de forma legível
def exibir_lista(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Função auxiliar para converter a lista encadeada de volta para inteiro (para checagem)
def lista_para_numero(head):
    result = 0
    mult = 1
    current = head
    while current:
        result += current.value * mult
        mult *= 10
        current = current.next
    return result

# Testando com números grandes
if __name__ == "__main__":
    L1 = numero_para_lista("999999999999999999999999")
    L2 = numero_para_lista("1")

    L3 = somar_listas(L1, L2)

    print("L1:", end=" "); exibir_lista(L1)
    print("L2:", end=" "); exibir_lista(L2)
    print("Soma L3:", end=" "); exibir_lista(L3)
    print("Resultado inteiro:", lista_para_numero(L3))


# complexidade de tempo:
# O(max(n, m)) — onde n e m são os tamanhos das listas (número de dígitos).