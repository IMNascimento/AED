class NoPatricia:
    def __init__(self, desvio, chave, info=None, m=26):
        self.desvio = desvio
        self.filhos = [None] * m
        self.chave = chave
        self.info = info

def buscar_patricia(no, s):
    if no is None:
        return False

    # Verifica se o prefixo até o desvio bate
    if no.chave[:no.desvio] != s[:no.desvio]:
        return False

    if no.chave == s:
        return True

    if no.desvio >= len(s):
        return False

    indice = ord(s[no.desvio]) - ord('a')
    if 0 <= indice < len(no.filhos):
        return buscar_patricia(no.filhos[indice], s)
    return False
