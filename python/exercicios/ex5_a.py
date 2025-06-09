class MatrizEsparsa:
    def __init__(self, n, m):
        self.n = n                          # número de linhas
        self.m = m                          # número de colunas
        self.linhas = [{} for _ in range(n)]  # lista de dicionários por linha
