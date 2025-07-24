def eh_arvore_prefixo(raiz):
    def dfs(no, encontrou_chave):
        # Se encontrou_chave=True e tem filhos, falha!
        if encontrou_chave and any(f is not None for f in no.filhos):
            return False
        ok = True
        for f in no.filhos:
            if f is not None:
                ok = ok and dfs(f, encontrou_chave or no.ehChave)
        return ok
    return dfs(raiz, False)
