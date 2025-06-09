import random

class No:
    def __init__(self, x, prox=None, desce=None):
        self.x = x            # valor armazenado
        self.prox = prox      # próximo nó no mesmo nível
        self.desce = desce    # nó correspondente no nível inferior

class SkipList:
    def __init__(self):
        # cria o primeiro nível com valor sentinela (-inf)
        self.head = No(float("-inf"))

    def buscar(self, k):
        atual = self.head
        while atual:
            while atual.prox and atual.prox.x < k:
                atual = atual.prox
            if atual.prox and atual.prox.x == k:
                return True
            atual = atual.desce
        return False
    
    def inserir(self, k):
        caminho = []                # Posição de inserção em cada nível
        atual = self.head

        # Caminho de cima para baixo
        while atual:
            while atual.prox and atual.prox.x < k:
                atual = atual.prox
            caminho.append(atual)
            atual = atual.desce

        # Inserção do nível mais baixo para cima
        abaixo = None
        promover = True

        while promover and caminho:
            anterior = caminho.pop()
            novo = No(k, anterior.prox, abaixo)
            anterior.prox = novo
            abaixo = novo
            promover = random.choice([True, False])

        # Se sobrou promoção, cria novo nível acima
        if promover:
            novo_head = No(float("-inf"), None, self.head)
            novo = No(k, None, abaixo)
            novo_head.prox = novo
            self.head = novo_head

    def remover(self, k):
        atual = self.head
        while atual:
            while atual.prox and atual.prox.x < k:
                atual = atual.prox
            if atual.prox and atual.prox.x == k:
                atual.prox = atual.prox.prox  # remove o nó
            atual = atual.desce

        # Remove níveis superiores vazios
        while self.head and not self.head.prox and self.head.desce:
            self.head = self.head.desce

    def mostrar(self):
            nivel = 0
            atual_nivel = self.head
            while atual_nivel:
                linha = f"Nível {nivel}: "
                atual = atual_nivel.prox
                while atual:
                    linha += f"{atual.x} -> "
                    atual = atual.prox
                print(linha + "None")
                atual_nivel = atual_nivel.desce
                nivel += 1

if __name__ == "__main__":
    sl = SkipList()

    for val in [10, 20, 15, 7, 25, 30]:
        sl.inserir(val)

    print("SkipList após inserções:")
    sl.mostrar()

    print("Buscar 15:", sl.buscar(15))
    print("Buscar 100:", sl.buscar(100))

    sl.remover(15)
    print("SkipList após remover 15:")
    sl.mostrar()


#Complexidades
#Operação	Tempo médio	Espaço médio
#Buscar	     O(log n)	O(n)
#Inserir	 O(log n)	O(n)
#Remover	 O(log n)	O(n)