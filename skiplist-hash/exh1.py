class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def primary_hash(self, key):
        return key % self.size

    def secondary_hash(self, key):
        # A função hash secundária deve ser escolhida de forma a garantir que,
        # após 'size' tentativas, todas as posições sejam testadas.
        # Uma abordagem comum é usar um número primo menor que o tamanho da tabela.
        # A função hash secundária nunca deve retornar 0.
        return 1 + (key % (self.size - 1))

    def insert(self, key):
        initial_index = self.primary_hash(key)
        step = self.secondary_hash(key)
        index = initial_index

        i = 0
        while self.table[index] is not None and i < self.size:
            index = (initial_index + i * step) % self.size
            i += 1

        if i == self.size:
            raise Exception("HashTable is full")
        self.table[index] = key

# Exemplo de uso
hash_table = HashTable(10)  # Tabela hash de tamanho 10
try:
    hash_table.insert(12)  # Insere o valor 12
    hash_table.insert(22)  # Insere o valor 22, que terá uma colisão inicial com 12
    print("Estado da tabela hash após inserções:", hash_table.table)
except Exception as e:
    print(e)