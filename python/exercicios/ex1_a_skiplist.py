class No:
    def __init__(self, x, prox=None, desce=None):
        self.x = x
        self.prox = prox
        self.desce = desce


def contido(head: No, k: int) -> bool:
    atual = head
    while atual:
        # Avança na horizontal enquanto valor for menor
        while atual.prox and atual.prox.x < k:
            atual = atual.prox
        # Se encontrar o valor exato, retorna True
        if atual.prox and atual.prox.x == k:
            return True
        # Desce um nível
        atual = atual.desce
    return False  # Não encontrou em nenhum nível



if __name__ == "__main__":
    # Exemplo de construção manual (nível único)
    n1 = No(10)
    n2 = No(20)
    n3 = No(30)
    n1.prox = n2
    n2.prox = n3

    head = No(float("-inf"), n1)  # Sentinela com ponteiro para n1

    print(contido(head, 20))  # True
    print(contido(head, 15))  # False


#Complexidade
#Tempo médio: O(log n) (graças aos níveis da SkipList)

#Pior caso: O(n) (se degenera em lista comum)