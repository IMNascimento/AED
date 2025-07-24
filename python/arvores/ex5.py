def contar_maiores(heap, i, x):
    if i >= len(heap):
        return 0

    if heap[i] <= x:
        return 0  # Nenhum filho será maior

    # heap[i] > x, conta ele e verifica filhos
    esq = contar_maiores(heap, 2 * i + 1, x)
    dir = contar_maiores(heap, 2 * i + 2, x)
    return 1 + esq + dir

# Exemplo
heap = [100, 90, 80, 70, 60, 50, 40]
x = 65
print(contar_maiores(heap, 0, x))  # Deve contar: 100, 90, 80, 70 → 4
