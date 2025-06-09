class MatrizEsparsa:
    def __init__(self, n, m):
        self.n = n                          # número de linhas
        self.m = m                          # número de colunas
        self.linhas = [{} for _ in range(n)]  # lista de dicionários por linha

    def get(self, i, j):
        # Retorna o valor da posição (i,j) ou 0 se não existir
        return self.linhas[i].get(j, 0)
    
    def set(self, i, j, value):
        if value != 0:
            self.linhas[i][j] = value
        elif j in self.linhas[i]:
            del self.linhas[i][j]  # remove se estiver zerando

    def multiplicar_por(self, outra):
        if self.m != outra.n:
            raise ValueError("Dimensões incompatíveis para multiplicação")

        resultado = MatrizEsparsa(self.n, outra.m)

        for i in range(self.n):
            for k1, v1 in self.linhas[i].items():       # A[i][k1]
                if k1 < outra.n:
                    for k2, v2 in outra.linhas[k1].items():  # A[k1][k2]
                        atual = resultado.get(i, k2)
                        resultado.set(i, k2, atual + v1 * v2)

        return resultado
    

if __name__ == "__main__":
    A = MatrizEsparsa(3, 3)
    A.set(0, 1, 2)
    A.set(1, 2, 3)
    A.set(2, 0, 4)

    A2 = A.multiplicar_por(A)

    for i in range(3):
        for j in range(3):
            print(f"A²[{i}][{j}] = {A2.get(i, j)}")