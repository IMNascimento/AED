#4) Escreva um algoritmo para reconhecer se uma dada palavra é um palíndromo. Considere que a
#palavra está contida em uma lista simplesmente encadeada, onde cada caractere está em um nó
#da lista.

# Nó da lista encadeada (cada caractere da palavra)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Função que verifica se a lista representa um palíndromo
def eh_palindromo(head):
    stack = []  # Usado para armazenar os caracteres na ordem direta

    atual = head
    while atual:
        stack.append(atual.value)  # Salva os caracteres
        atual = atual.next

    atual = head
    while atual:
        topo = stack.pop()         # Pega o último caractere armazenado
        if atual.value != topo:    # Compara com o caractere atual
            return False           # Se for diferente, não é palíndromo
        atual = atual.next

    return True  # Se passou por toda a lista sem falhas, é palíndromo

#funções auxiliares
# Converte uma string para lista encadeada
def string_para_lista(s):
    head = None
    tail = None
    for ch in s:
        node = Node(ch)
        if not head:
            head = tail = node
        else:
            tail.next = node
            tail = node
    return head

# Exibe a lista encadeada (debug)
def exibir_lista(head):
    atual = head
    while atual:
        print(atual.value, end=" -> ")
        atual = atual.next
    print("None")


if __name__ == "__main__":
    palavra = "reviver"  # Palíndromo
    head = string_para_lista(palavra)

    exibir_lista(head)
    if eh_palindromo(head):
        print(f"'{palavra}' é um palíndromo!")
    else:
        print(f"'{palavra}' NÃO é um palíndromo.")



# Complexidade
#Tempo: O(n)
# Uma passagem para empilhar + uma para comparar

#Espaço: O(n)