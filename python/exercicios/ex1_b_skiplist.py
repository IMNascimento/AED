class No:
    def __init__(self, x, prox=None, desce=None):
        self.x = x
        self.prox = prox
        self.desce = desce

def contaMenores(head: No, x: int) -> int:
    """
    Retorna a quantidade de nós com valor < x na SkipList.
    """
    atual = head
    count = 0

    while atual:
        # Avança na horizontal enquanto valor for menor que x
        while atual.prox and atual.prox.x < x:
            atual = atual.prox
            count += 1  # Contamos cada valor menor que x
        # Desce um nível
        atual = atual.desce

    return count


if __name__ == "__main__":
    # Criando manualmente uma SkipList simples com dois níveis

    # Nível inferior
    n1 = No(10)
    n2 = No(20)
    n3 = No(30)
    n1.prox = n2
    n2.prox = n3

    # Nível superior
    u1 = No(10, n2)   # 10 -> 20
    u2 = No(30)       # 30
    u1.desce = n1
    u2.desce = n3

    # Conectando head do nível mais alto
    head = No(float("-inf"), u1)
    head.desce = No(float("-inf"), n1)

    print("Quantos menores que 25:", contaMenores(head, 25))  # Deve retornar 2 (10, 20)
    print("Quantos menores que 10:", contaMenores(head, 10))  # Deve retornar 0
    print("Quantos menores que 100:", contaMenores(head, 100))  # Deve retornar 3


# Complexidade
#Tempo médio: O(log n) (graças aos níveis da SkipList)

#Pior caso: O(n) (se degenera para uma lista comum)

#Espaço adicional: O(1) (somente contador)