class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)  # Simples inserção no fim da lista

    def search(self, key):
        index = self.hash_function(key)
        for item in self.table[index]:
            if item == key:
                return True
        return False

# Exemplo de uso
hash_table = HashTable(10)
keys = [15, 25, 35, 5]
for key in keys:
    hash_table.insert(key)

# Busca sem sucesso
print("Busca por um elemento não presente (45):", hash_table.search(45))

# Discussão sobre complexidade
print("Complexidade de inclusão: O(1)")
print("Complexidade de busca sem sucesso: O(lambda), onde lambda é o fator de carga da tabela")