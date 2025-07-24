def is_bst(node, min_val=float('-inf'), max_val=float('inf')):
    if node is None:
        return True
    if not (min_val < node.key < max_val):
        return False
    return is_bst(node.left, min_val, node.key) and is_bst(node.right, node.key, max_val)