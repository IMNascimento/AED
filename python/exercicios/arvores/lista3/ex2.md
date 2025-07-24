Contra-exemplo:
Use mesmo heap inicial: [1, 3, 5, 7, 9, 8, 10]

Pegue 𝑖 = 2 (S[2]=5), 𝑗 = 3 (S[3]=7), S[2] < S[3], então inverta: use i=3 (S[3]=7), j=1 (S[1]=3), S[3] > S[1].

Troque S[1]=3 e S[3]=7: [1, 7, 5, 3, 9, 8, 10]

Árvore:
        1
      /   \
     7     5
    / \   / \
   3   9 8  10
Nó 7 (posição 1) tem filho 3, que é menor — OK.

1 é raiz, seus filhos são 7 e 5, ambos maiores — mantém a propriedade de heap mínimo.

Mas tente trocar S[2]=5 (i=2) com S[6]=10 (j=6):
S[2] < S[6], mas a pergunta é S[i] > S[j], então S[2]=5, S[5]=8, S[2] < S[5].

Pegue S[4]=9, S[6]=10: i=4, j=6, S[4]=9, S[6]=10, S[4] < S[6], não serve.

Agora, tente um caso onde a troca quebra o heap:
Pegue S[1]=3, S[4]=7. Troque: S[1]=7, S[4]=3.
Novo vetor: [1, 7, 5, 3, 9, 8, 10] — já analisado, segue heap.

Para heap mínimo, se S[i] > S[j] e i < j, trocar S[i] por S[j] pode ou não manter a propriedade de heap. Não é garantido!

Conclusão:
A afirmação é FALSA também para esse caso.