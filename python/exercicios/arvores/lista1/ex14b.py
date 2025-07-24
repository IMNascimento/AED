def is_bst_inorder(root):
    stack = []
    node = root
    prev = float('-inf')
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if node.key <= prev:
            return False
        prev = node.key
        node = node.right
    return True
