Vantagem: A altura da árvore diminui conforme m aumenta ⇒ menos níveis para descer/subir.
Desvantagem: Em cada descer(), precisa comparar com m filhos (mais comparações por nível).
Para heaps grandes (em disco, sistemas com caches), m-heaps podem ser vantajosos, pois reduzem o número de acessos por caminho.
Na prática, d-ary heaps (m = 4, 8, etc.) são usados em alguns algoritmos de prioridade porque a diminuição da altura pode compensar o aumento nas comparações.