def conta_substring(raiz, q):
    def dfs(no, caminho):
        count = 0
        if no.ehChave:
            count += caminho.count(q)
        for i, filho in enumerate(no.filhos):
            if filho is not None:
                count += dfs(filho, caminho + str(i))
        return count
    return dfs(raiz, "")
