Num heap mínimo (implementação em vetor), para cada índice 𝑖, o pai está em pai(𝑖)=[(𝑖−1)/2].

Não é porque 𝑖 < 𝑗 e 𝑆[𝑖] < 𝑆[𝑗] que trocar 𝑆[𝑖] e 𝑆[𝑗] mantém a propriedade de heap.

Contra-exemplo:
Considere o heap mínimo:
Vetor: [1, 3, 5, 7, 9, 8, 10]

        1
      /   \
     3     5
    / \   / \
   7   9 8  10

Pegue 𝑖 = 1 (S[1]=3), 𝑗 = 6 (S[6]=10).
i < j e S[i] < S[j].

Troque S[1] com S[6]: [1, 10, 5, 7, 9, 8, 3]

Árvore:
        1
      /   \
     10    5
    / \   / \
   7   9 8  3
O nó 10 (posição 1) tem filhos 7 e 9, ambos menores — não é heap!

Logo, a afirmação é FALSA.