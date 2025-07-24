class NoAVL:
    def __init__(self, fb=0, esq=None, dir=None):
        self.fb = fb
        self.esq = esq
        self.dir = dir

# Quando p.fb == +2, o filho direito u existe
# Para que o desequilíbrio venha de u, fb(u) deve ser +1
