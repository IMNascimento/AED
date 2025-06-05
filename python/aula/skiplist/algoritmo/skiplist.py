import random
import time

class SkipListNode:
    """
    Representa um nó da SkipList, que guarda um valor e ponteiros para frente em vários níveis.
    """
    def __init__(self, value, level):
        self.value = value                              # Valor armazenado neste nó
        self.forward = [None] * (level + 1)             # Lista de ponteiros para frente (um para cada nível)

class SkipList:
    """
    Implementa a estrutura de dados SkipList.
    """
    def __init__(self, max_level, p):
        self.max_level = max_level                      # Nível máximo da SkipList
        self.p = p                                      # Probabilidade para sorteio de níveis
        self.header = SkipListNode(None, self.max_level)  # Nó cabeçalho vazio
        self.level = 0                                  # Nível atual mais alto da lista

    def random_level(self):
        """
        Sorteia um nível para o novo nó usando a probabilidade p.
        Aumenta o nível enquanto random.random() < p e não passar do máximo.
        """
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, value):
        """
        Busca um valor na SkipList.
        Retorna o nó se encontrar, ou None se não existir.
        """
        current = self.header                           # Começa do cabeçalho
        # Desce do nível mais alto até o nível 0
        for i in reversed(range(self.level + 1)):
            # Vai para frente enquanto o próximo nó for menor que o valor
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        # No nível 0, avança para o possível nó com o valor
        current = current.forward[0]
        # Retorna o nó se encontrou, senão None
        if current and current.value == value:
            return current
        return None

    def insert(self, value):
        """
        Insere um novo valor na SkipList (se não existir ainda).
        """
        update = [None] * (self.max_level + 1)          # Lista para guardar onde atualizar os ponteiros
        current = self.header

        # Do nível mais alto para baixo, move até encontrar onde inserir
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current                         # Guarda último nó menor em cada nível

        current = current.forward[0]                    # Avança para o próximo no nível 0

        if not current or current.value != value:       # Só insere se não existir ainda
            lvl = self.random_level()                   # Sorteia o nível do novo nó

            # Se o nível for maior que o atual da SkipList, atualiza a lista
            if lvl > self.level:
                for i in range(self.level + 1, lvl + 1):
                    update[i] = self.header
                self.level = lvl

            new_node = SkipListNode(value, lvl)         # Cria o novo nó
            # Atualiza os ponteiros para inserir o novo nó em todos os níveis sorteados
            for i in range(lvl + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def delete(self, value):
        """
        Remove um valor da SkipList, se ele existir.
        """
        update = [None] * (self.max_level + 1)          # Lista de atualização de ponteiros
        current = self.header

        # Move em cada nível até achar o valor (ou saber que não está ali)
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]

        # Se encontrou o nó, remove ajustando os ponteiros em cada nível
        if current and current.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            # Ajusta o nível da SkipList se necessário
            while self.level > 0 and not self.header.forward[self.level]:
                self.level -= 1

    def print_max_height(self):
        """
        Imprime a altura máxima (nível mais alto + 1) da SkipList.
        """
        print(f"Altura máxima da skip list: {self.level + 1}")

    def print_list(self):
        """
        Imprime visualmente a SkipList por nível (do mais alto para o mais baixo).
        """
        print("\n***** Skip List *****")
        # Para cada nível, imprime os valores na ordem
        for lvl in range(self.level, -1, -1):
            node = self.header.forward[lvl]
            print(f"Level {lvl}: ", end="")
            while node:
                print(node.value, end=" ")
                node = node.forward[lvl]
            print("")

def main():
    print("Testando SkipList com 100.000 valores...")
    n = 100_000                             # Quantidade de valores para inserir
    max_level = 16                          # Altura máxima da lista (ajuste se quiser)
    p = 0.5                                 # Probabilidade (quanto menor, mais "baixa" a lista)

    skiplist = SkipList(max_level, p)       # Cria a SkipList

    # Gera 100.000 números aleatórios únicos (entre 1 e n*10)
    data = random.sample(range(1, n * 10), n)

    start = time.time()                     # Marca o início do tempo
    for value in data:                      # Insere todos os valores na lista
        skiplist.insert(value)
    end = time.time()                       # Marca o final do tempo

    print(f"Inserção de {n} elementos em {end - start:.2f} segundos.")
    skiplist.print_max_height()             # Mostra altura final da SkipList

    # Testa busca para 10 valores aleatórios que sabemos que existem
    test_search = random.sample(data, 10)
    for val in test_search:
        node = skiplist.search(val)
        assert node is not None and node.value == val

    # Testa remoção para 10 valores aleatórios que existem
    test_remove = random.sample(data, 10)
    for val in test_remove:
        skiplist.delete(val)
        assert skiplist.search(val) is None

    print("Busca e remoção funcionaram corretamente.")

    # (Opcional) Para ver a lista impressa, use n=20 acima e descomente:
    # skiplist.print_list()

if __name__ == "__main__":
    main()
