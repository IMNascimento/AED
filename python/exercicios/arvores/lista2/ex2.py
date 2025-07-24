class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.fator_balanceamento = 0


def eh_avl(node):
    """
    Retorna (True, altura) se for AVL; (False, altura) se não for.
    """
    if node is None:
        return True, 0

    # Checa recursivamente as subárvores esquerda e direita
    esq_avl, h_esq = eh_avl(node.left)
    dir_avl, h_dir = eh_avl(node.right)

    # Fator de balanceamento para este nó
    fb = h_dir - h_esq

    # Atualiza o nó se desejar (opcional)
    node.fator_balanceamento = fb

    # Confere se este nó está balanceado
    ok = esq_avl and dir_avl and (fb in [-1, 0, 1])

    altura_no = 1 + max(h_esq, h_dir)
    return ok, altura_no



# como usar
#raiz = AVLNode(10)
#raiz.left = AVLNode(5)
#raiz.right = AVLNode(15)
#resultado, _ = eh_avl(raiz)
#print(resultado)