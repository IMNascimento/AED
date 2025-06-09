#d) Complexidade da multiplicação (A²)
# Notação:
#k = número total de elementos não nulos

# Tempo:
#Para cada entrada não-nula A[i][k1] com valor v1:

#Verificamos todos A[k1][k2] com valor v2

#Isso depende de quantos não nulos há na linha k1 (vamos chamar de t)

# No pior caso, cada par de entradas não nulas pode interagir com outros → O(k²) no pior caso.
# No caso médio (matriz realmente esparsa), tende a ser O(k·r) onde r é a média de elementos por linha.

# Espaço:
#A matriz resultante também terá no máximo k² posições não nulas, mas na prática muito menos.

#Usa espaço O(k'), onde k' é o número de elementos relevantes em A².

