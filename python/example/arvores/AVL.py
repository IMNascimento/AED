class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def right_rotate(z):
    y = z.left
    T3 = y.right

    y.right = z
    z.left = T3

    z.height = max(height(z.left), height(z.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1
    return y

def left_rotate(z):
    y = z.right
    T2 = y.left

    y.left = z
    z.right = T2

    z.height = max(height(z.left), height(z.right)) + 1
    y.height = max(height(y.left), height(y.right)) + 1
    return y


def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)
    

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current



def avl_insert(root, key):
    if not root:
        return AVLNode(key)
    elif key < root.key:
        root.left = avl_insert(root.left, key)
    else:
        root.right = avl_insert(root.right, key)

    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)

    # Left Left
    if balance > 1 and key < root.left.key:
        return right_rotate(root)
    # Right Right
    if balance < -1 and key > root.right.key:
        return left_rotate(root)
    # Left Right
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # Right Left
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def avl_delete(root, key):
    if not root:
        return root
    elif key < root.key:
        root.left = avl_delete(root.left, key)
    elif key > root.key:
        root.right = avl_delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = avl_delete(root.right, temp.key)

    root.height = 1 + max(height(root.left), height(root.right))
    balance = get_balance(root)

    # Rotations
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)
    return root