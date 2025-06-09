#3) Seja L uma lista simplesmente encadeada. Escreva um algoritmo que, percorrendo a lista uma
#única vez, constrói:
#A. Uma lista L’ que possui os valores de L em ordem inversa
#B. Uma lista L’' que possui a metade dos nós da lista L, onde o primeiro nó de L’' contém a
#soma do primeiro nó de L com o último nó de L, o segundo nó de L’ contém a soma do
#segundo nó de L com o penúltimo nó de L e assim por diante: L''= < L1+Ln, L2+Ln-1,
#L3+Ln-2, ... , Ln/2 + Ln/2+1>, onde n é sempre par.

# Nó da lista encadeada
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Cria lista encadeada a partir de lista Python
def criar_lista_encadeada(valores):
    head = None
    tail = None
    for v in valores:
        novo = Node(v)
        if head is None:
            head = tail = novo
        else:
            tail.next = novo
            tail = novo
    return head

# Exibe uma lista encadeada
def exibir_lista(head, nome="Lista"):
    print(f"{nome}: ", end="")
    atual = head
    while atual:
        print(atual.value, end=" -> ")
        atual = atual.next
    print("None")

# Constrói L' (inversa) e L'' (somas) em uma única passagem por L
def construir_L_primeduas(L):
    valores = []       # Armazena os valores para montar L''
    L_inversa = None   # L'
    
    atual = L
    while atual:
        valores.append(atual.value)
        
        # Insere no início de L' para formar a lista invertida
        novo = Node(atual.value)
        novo.next = L_inversa
        L_inversa = novo
        
        atual = atual.next

    n = len(valores)
    if n % 2 != 0:
        raise ValueError("A lista deve ter número par de elementos para construir L''")

    # Construção de L''
    L_somas = None
    tail_somas = None
    for i in range(n // 2):
        soma = valores[i] + valores[n - 1 - i]
        novo = Node(soma)
        if L_somas is None:
            L_somas = tail_somas = novo
        else:
            tail_somas.next = novo
            tail_somas = novo

    return L_inversa, L_somas

# Código principal (teste)
if __name__ == "__main__":
    # Lista original com número par de elementos
    L = criar_lista_encadeada([1, 2, 3, 4, 5, 6])

    exibir_lista(L, "L original")

    L_inversa, L_somas = construir_L_primeduas(L)

    exibir_lista(L_inversa, "L' (inversa)")
    exibir_lista(L_somas, "L'' (somas L1+Ln...)")


# exemplo de uso: L = [1, 2, 3, 4, 5, 6]
#saida 
# L original:        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
# L' (inversa):      6 -> 5 -> 4 -> 3 -> 2 -> 1 -> None
# L'' (somas L1+Ln): 7 -> 7 -> 7 -> None


# complexibilidade:
#Parte A: Construção de L' (lista inversa)
#Lógica:
#Percorremos L uma vez e, a cada nó, criamos um novo nó com o mesmo valor e o inserimos no início da nova lista L'.

#Complexidade:
#Tempo: O(n)
# Cada nó de L é processado uma vez e a inserção no início é O(1), então no total é O(n).

#Espaço: O(n)
# Porque criamos uma nova lista com n nós (nova L').

#Parte B: Construção de L'' (somas L1+Ln, L2+Ln−1, etc)
#Lógica:
#Durante a única passada por L, salvamos os valores em uma lista Python auxiliar: valores = [1, 2, 3, ..., n].

#Depois, fazemos n/2 somas: valores[i] + valores[n-1-i] e criamos nós para L''.

#Complexidade:
#Tempo:

#Passar por L uma vez: O(n)

#Fazer n/2 somas: O(n)
# Total: O(n)

#Espaço:

#Lista auxiliar valores: O(n)

#Nova lista L'': O(n/2) → simplifica para O(n)
# Total: O(n)