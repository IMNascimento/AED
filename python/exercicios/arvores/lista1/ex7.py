def is_strictly_binary(node):
    if node is None:
        return True
    if (node.left is None and node.right is None):
        return True
    if (node.left is not None and node.right is not None):
        return is_strictly_binary(node.left) and is_strictly_binary(node.right)
    return False
