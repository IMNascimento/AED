class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.fator_balanceamento = 0

def altura(node):
    if node is None:
        return 0
    return 1 + max(altura(node.left), altura(node.right))

def atualiza_fb(node):
    if node is None:
        return
    h_esq = altura(node.left)
    h_dir = altura(node.right)
    node.fator_balanceamento = h_dir - h_esq

def rotacao_esq(x):
    y = x.right
    x.right = y.left
    y.left = x

    atualiza_fb(x)
    atualiza_fb(y)
    return y

def rotacao_dir(y):
    x = y.left
    y.left = x.right
    x.right = y

    atualiza_fb(y)
    atualiza_fb(x)
    return x

def rotacao_esq_dir(z):
    z.left = rotacao_esq(z.left)
    return rotacao_dir(z)

def rotacao_dir_esq(z):
    z.right = rotacao_dir(z.right)
    return rotacao_esq(z)
