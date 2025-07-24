def imprime_chaves_prefixo(raiz, q):
    def dfs(no, prefixo):
        if no.ehChave:
            print(prefixo)
        for i, filho in enumerate(no.filhos):
            if filho is not None:
                dfs(filho, prefixo + str(i))

    # Caminha até o nó do prefixo
    no = raiz
    for c in q:
        idx = int(c)
        if no.filhos[idx] is None:
            return  # Nenhuma chave com esse prefixo
        no = no.filhos[idx]
    dfs(no, q)
