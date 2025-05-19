def cluster_growth_probability(cluster_size, table_size):
    return (cluster_size + 1) / table_size

# Exemplo de uso
cluster_size = 3  # Tamanho atual do agrupamento
table_size = 10   # Tamanho total da tabela hash

probability = cluster_growth_probability(cluster_size, table_size)
print(f"Probabilidade de o agrupamento de tamanho {cluster_size} aumentar após uma inserção: {probability:.2f}")