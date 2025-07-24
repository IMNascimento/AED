def is_complete(root):
    if root is None:
        return True
    fila = [root]
    encontrou_filho_faltando = False
    while fila:
        node = fila.pop(0)
        if node.left:
            if encontrou_filho_faltando:
                return False
            fila.append(node.left)
        else:
            encontrou_filho_faltando = True
        if node.right:
            if encontrou_filho_faltando:
                return False
            fila.append(node.right)
        else:
            encontrou_filho_faltando = True
    return True
