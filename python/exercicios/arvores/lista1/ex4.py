class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.is_leaf = False
        self.valor = None

def reconstrua_arvore(codigos_e_valores):
    raiz = Node()
    for codigo, valor in codigos_e_valores:
        atual = raiz
        for c in codigo:
            if c == "0":
                if atual.left is None:
                    atual.left = Node()
                atual = atual.left
            else:
                if atual.right is None:
                    atual.right = Node()
                atual = atual.right
        atual.is_leaf = True
        atual.valor = valor
    return raiz
