def eh_sufixo(raiz, q):
    # Percorre toda a trie, verifica se alguma chave termina com q
    def dfs(no, caminho):
        found = False
        if no.ehChave and caminho.endswith(q):
            return True
        for i, filho in enumerate(no.filhos):
            if filho is not None:
                found = found or dfs(filho, caminho + str(i))
        return found
    return dfs(raiz, "")
