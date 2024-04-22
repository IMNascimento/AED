def count_collisions(keys, mod_value):
    hash_buckets = [0] * mod_value
    for key in keys:
        index = key % mod_value
        hash_buckets[index] += 1
    
    # Contar colisões: qualquer valor maior que 1 em hash_buckets indica colisões
    collisions = sum(x - 1 for x in hash_buckets if x > 1)
    return collisions

# Número de múltiplos de 7
n = 10
multiples_of_7 = [7 * i for i in range(1, n+1)]

# Calcular colisões para diferentes funções de hash
#A)
collisions_mod_7 = count_collisions(multiples_of_7, 7)
#B)
collisions_mod_14 = count_collisions(multiples_of_7, 14)
#C)
collisions_mod_5 = count_collisions(multiples_of_7, 5)

print(f"Colisões para x mod 7: {collisions_mod_7}")
print(f"Colisões para x mod 14: {collisions_mod_14}")
print(f"Colisões para x mod 5: {collisions_mod_5}")