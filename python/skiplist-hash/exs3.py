def hash_function(k):
    return k % 15

# Vamos verificar se há colisões com esta função hash
def test_hash_function(values):
    hash_table = [None] * 15
    collisions = 0
    for value in values:
        index = hash_function(value)
        if hash_table[index] is not None:
            collisions += 1
            print(f"Colisão detectada: {value} na posição {index}, que já contém {hash_table[index]}")
        hash_table[index] = value
    print(f"Número total de colisões: {collisions}")
    return hash_table


#EX3 - A)
# Conjunto S
S = [16385, 2, 17, 3, 33, 513, 8193, 1025, 65, 5, 129, 2049, 9, 257, 4097]

# Testando a função hash
hash_table = test_hash_function(S)

# Mostrar a distribuição na tabela hash
print("Distribuição na tabela hash:")
for i, value in enumerate(hash_table):
    print(f"Posição {i}: {value}")


#EX3-B)

def average_list_size(hash_table):
    filled_positions = sum(1 for i in hash_table if i is not None)
    return filled_positions / len(hash_table)

# Calculando o tamanho médio
avg_size = average_list_size(hash_table)
print(f"Tamanho médio das listas na tabela hash: {avg_size}")    