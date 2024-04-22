def no_collision_probability(m, n):
    """ Calcula a probabilidade de não haver colisões para n chaves em m baldes. """
    if n > m:
        return 0  # Não faz sentido ter mais chaves do que baldes sem colisões.
    numerator = 1
    for i in range(n):
        numerator *= (m - i)
    denominator = m ** n
    return numerator / denominator

# Exemplo de uso
m = 15  # Número de baldes
n = 15  # Número de chaves

probability = no_collision_probability(m, n)
print(f"A probabilidade de que não haja colisões com {n} chaves em {m} baldes é {probability:.10f}")