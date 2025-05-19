class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.num_elements = 0

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)
        self.num_elements += 1

    def calculate_load_factor(self):
        return self.num_elements / self.size

# Exemplo de uso
hash_table = HashTable(5)  # Tabela com 5 baldes
keys = [1, 2, 3, 4, 5, 6]  # Inserindo 6 elementos
for key in keys:
    hash_table.insert(key)

load_factor = hash_table.calculate_load_factor()
print("Fator de Carga da Tabela Hash:", load_factor)