class NoTRIE:
    def __init__(self):
        self.ehChave = False
        self.filhos = [None] * 10  # Alfabeto: '0' a '9'



def eh_prefixo(raiz, q):
    no = raiz
    for c in q:
        idx = int(c)
        if no.filhos[idx] is None:
            return False
        no = no.filhos[idx]
    # Se existe caminho para q, é prefixo (de si mesmo ou de outros)
    return True
