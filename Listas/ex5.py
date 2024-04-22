class SparseMatrix:
    def __init__(self):
        # Utilizaremos um dicionário para armazenar os elementos não-nulos.
        # As chaves serão tuplas (i, j) representando as posições da matriz.
        self.elements = {}

    def insert(self, i, j, value):
        """ Insere ou atualiza um valor na matriz esparsa na posição (i, j). """
        if value != 0:
            self.elements[(i, j)] = value
        elif (i, j) in self.elements:
            # Remove o elemento se o valor for zero para manter a esparsidade.
            del self.elements[(i, j)]

    def locate(self, i, j):
        """ Retorna o valor na posição (i, j) da matriz, ou 0 se a posição estiver vazia. """
        return self.elements.get((i, j), 0)

    def compute_square(self):
        """ Calcula o quadrado da matriz esparsa. """
        result = SparseMatrix()
        # Percorrendo cada elemento da matriz original.
        for (i, j), value in self.elements.items():
            for (k, l), v in self.elements.items():
                if j == k:
                    result.insert(i, l, result.locate(i, l) + value * v)
        return result

# Exemplo de uso da classe SparseMatrix EX5-A
sparse_matrix = SparseMatrix()
sparse_matrix.insert(0, 0, 1)
sparse_matrix.insert(0, 1, 2)
sparse_matrix.insert(1, 0, 3)
sparse_matrix.insert(1, 1, 4)

# Localizando um elemento específico EX5-B
element_at_1_1 = sparse_matrix.locate(1, 1)
print("Elemento na posição (1,1):", element_at_1_1)

# Calculando o quadrado da matriz EX5-C
squared_matrix = sparse_matrix.compute_square()
print("Elementos na matriz ao quadrado:")
for key, value in squared_matrix.elements.items():
    print(f"Posição {key}: {value}")

# EX5-D
print("A complexidade da função compute_square seria O(n^2 * k) no pior caso, onde k é o número de elementos não nulos.")


