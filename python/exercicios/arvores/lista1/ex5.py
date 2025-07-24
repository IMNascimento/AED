def contar_nos_iterativo(root):
    if root is None:
        return 0
    fila = [root]
    count = 0
    while fila:
        node = fila.pop(0)
        count += 1
        if node.left:
            fila.append(node.left)
        if node.right:
            fila.append(node.right)
    return count
