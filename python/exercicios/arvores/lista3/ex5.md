1. Possui k filhos.
Por definição, a árvore binomial de grau k (Bk) é construída ligando duas árvores de grau k-1.

O nó raiz passa a ter exatamente k filhos.

2. Possui altura k.
Cada vez que liga duas B(k-1), aumenta a altura em 1.

Para B0: altura 0 (só raiz)

B1: altura 1

... logo, Bk tem altura k.

3. Possui C(k, i) nós no nível i
Prova por indução:

Para k = 0: só a raiz, nível 0 → 1 = C(0,0)

Ao construir Bk a partir de duas B(k-1), os nós no nível i vêm de:

os próprios filhos do nível i da subárvore à esquerda

os filhos do nível i-1 da subárvore à direita

No final, o número de nós no nível i é C(k, i).