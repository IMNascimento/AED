def tabela_huffman(raiz):
    tabela = []
    def dfs(no, codigo):
        if no is None:
            return
        if getattr(no, "caractere", None) is not None:
            tabela.append([no.caractere, codigo])
        dfs(no.left, codigo + "0")
        dfs(no.right, codigo + "1")
    dfs(raiz, "")
    return tabela  # lista de [caractere, codigo]
