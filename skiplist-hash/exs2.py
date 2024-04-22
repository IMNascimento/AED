class No:
    def __init__(self, x):
        self.x = x
        self.prox = None

class HTable:
    def __init__(self, m):
        self.table = [None] * m
        self.m = m

def h(k, m):
    return k % m  # Uma função hash simples para demonstração

# A)
def inserir(ht, k):
    index = h(k, ht.m)
    new_node = No(k)
    new_node.prox = ht.table[index]
    ht.table[index] = new_node

#B)
def destruir_hash(ht):
    ht.table = [None] * ht.m

# C)
def contaMaiores(ht, k):
    count = 0
    for i in range(ht.m):
        current = ht.table[i]
        while current:
            if current.x > k:
                count += 1
            current = current.prox
    return count

# Configuração inicial da tabela hash
tabela_hash = HTable(10)  # Suponhamos que m=10

#A) Inserindo elementos na tabela hash 
inserir(tabela_hash, 15)
inserir(tabela_hash, 25)
inserir(tabela_hash, 35)
inserir(tabela_hash, 5)

#C) Testando a inserção e a função contaMaiores 
print("Exercício 2c: ContaMaiores")
print("Quantos valores maiores que 20?", contaMaiores(tabela_hash, 20))  # Esperado: 2 (25 e 35)

#b) Destruição do hash  
destruir_hash(tabela_hash)
print("Exercício 2b: Destruição de todo o hash")
print("Estado da tabela após destruição:", ["None" if x is None else "Not None" for x in tabela_hash.table])

#d) Resposta sobre complexidade
complexidade_respostas = """
Exercício 2d: Complexidade das Funções Implementadas

1. Inserção de um elemento na tabela hash (inserir):
   - Complexidade: O(1) no caso médio.
   - Justificativa: A inserção é geralmente considerada O(1) porque ocorre no início da lista ligada no índice calculado pela função hash.
     Em caso de má distribuição dos valores pela função hash, isso poderia degenerar para O(n) no pior caso.

2. Destruição de todo o hash (destruir_hash):
   - Complexidade: O(m), onde m é o número de baldes na tabela.
   - Justificativa: A função passa por todos os baldes e os reinicializa, o que é uma operação linear em relação ao número de baldes.

3. Contagem de valores maiores que k no hash (contaMaiores):
   - Complexidade: O(n) no pior caso.
   - Justificativa: A função verifica cada elemento em todas as listas ligadas para contar quantos são maiores que k. Em uma distribuição
     uniforme ou no pior caso de todos os elementos em uma única lista, isso requer visitar cada elemento na tabela.
"""

print(complexidade_respostas)