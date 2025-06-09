class MatrizEsparsa:
    def __init__(self, n, m):
        self.n = n                          # número de linhas
        self.m = m                          # número de colunas
        self.linhas = [{} for _ in range(n)]  # lista de dicionários por linha

    def get(self, i, j):
        # Retorna o valor da posição (i,j) ou 0 se não existir
        return self.linhas[i].get(j, 0)