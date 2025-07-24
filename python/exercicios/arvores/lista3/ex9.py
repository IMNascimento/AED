def buscar_binomial(raiz, chave):
    """Procura recursivamente em toda a floresta"""
    if raiz is None:
        return None
    if raiz.chave == chave:
        return raiz
    res = buscar_binomial(raiz.filho, chave)
    if res is not None:
        return res
    return buscar_binomial(raiz.irmao, chave)
