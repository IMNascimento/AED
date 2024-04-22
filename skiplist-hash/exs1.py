class No:
    def __init__(self, x):
        self.x = x
        self.prox = None
        self.desce = None

class SkipList:
    def __init__(self):
        self.head = None

#a) Implementação do algoritmo boolean contido(No head, int k)
def contido(head, k):
    current = head
    while current:
        if current.x == k:
            return True
        current = current.prox
    return False

#b)Implementação do algoritmo int contaMenores(No head, int k)
def contaMenores(head, k):
    count = 0
    current = head
    while current:
        if current.x < k:
            count += 1
        current = current.prox
    return count


# Configuração inicial da SkipList
skip_list = SkipList()
node1 = No(10)
node2 = No(20)
node3 = No(30)

node1.prox = node2  # Conectando os nós
node2.prox = node3

skip_list.head = node1  # Configurando a cabeça da SkipList

#A) Testando a função contido
print("Exercício 1a: Contido")
print("20 está contido?", contido(skip_list.head, 20))  # Esperado: True
print("40 está contido?", contido(skip_list.head, 40))  # Esperado: False

#B) Testando a função contaMenores
print("Exercício 1b: ContaMenores")
print("Quantidade de números menores que 25:", contaMenores(skip_list.head, 25))  # Esperado: 2
print("Quantidade de números menores que 15:", contaMenores(skip_list.head, 15))  # Esperado: 1