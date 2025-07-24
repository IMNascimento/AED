def eh_substring(raiz, q):
    def dfs(no, caminho):
        found = False
        if no.ehChave and q in caminho:
            return True
        for i, filho in enumerate(no.filhos):
            if filho is not None:
                found = found or dfs(filho, caminho + str(i))
        return found
    return dfs(raiz, "")
