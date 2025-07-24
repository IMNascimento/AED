def altura_otimizada(node):
    """
    Calcula a altura da árvore AVL visitando apenas o caminho mais profundo.
    """
    if node is None:
        return 0
    # Se for folha
    if node.left is None and node.right is None:
        return 1
    # Se um dos lados é nulo
    if node.left is None:
        return 1 + altura_otimizada(node.right)
    if node.right is None:
        return 1 + altura_otimizada(node.left)
    # Ambos os filhos existem: segue o lado mais alto
    if node.fator_balanceamento >= 0:
        return 1 + altura_otimizada(node.right)
    else:
        return 1 + altura_otimizada(node.left)



# exemplo de uso
#class AVLNode:
#    def __init__(self, key):
#        self.key = key
#        self.left = None
#        self.right = None
#        self.fator_balanceamento = 0

# Exemplo:
#raiz = AVLNode(10)
#raiz.left = AVLNode(5)
#raiz.right = AVLNode(20)
#raiz.right.right = AVLNode(25)
#raiz.fator_balanceamento = 1         # (2 - 1)
#raiz.right.fator_balanceamento = 1   # (1 - 0)
#raiz.left.fator_balanceamento = 0    # (0 - 0)
#raiz.right.right.fator_balanceamento = 0

#print(altura_otimizada(raiz))  # Resultado: 3
