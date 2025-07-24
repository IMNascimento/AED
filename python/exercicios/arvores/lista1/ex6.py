def contar_nos_recursivo(node):
    if node is None:
        return 0
    return 1 + contar_nos_recursivo(node.left) + contar_nos_recursivo(node.right)
