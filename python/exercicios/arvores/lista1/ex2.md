Em uma árvore binária completa, todos os níveis são preenchidos da esquerda para a direita.
Seja h o número de níveis.
O número máximo de nós até nível h é 2ℎ−1.
Para n nós, precisamos do menor h tal que 𝑛 ≤ 2ℎ − 1 ou seja, ℎ ≥ log2(𝑛+1).

Como a altura conta o número de níveis:
ℎ=1+[log2𝑛]
Ou seja, a altura de uma árvore binária completa com 𝑛 nós é 1 + lower(log n).