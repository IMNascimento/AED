def simplified_hashcode(s):
    return hash(''.join(s[i] for i in range(0, len(s), 2)))

# Exemplo de strings
strings = [
    "aaaaaaaaaa",  # Todos os caracteres iguais
    "aabbaabbaa",  # Padrão alterna a cada dois caracteres
    "aaaabbbbba",  # Padrão alterna na metade
    "bbaaaaaabb"   # Padrão alterna no início e no fim
]

# Calculando o hashcode para cada string
hashes = set()
for s in strings:
    hashes.add(simplified_hashcode(s))

# Se todos os hashes são iguais, significa que o método está propenso a colisões
print("Todos os hashes são iguais?", len(hashes) == 1)