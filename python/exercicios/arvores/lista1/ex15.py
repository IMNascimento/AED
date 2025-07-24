def is_symmetric(root):
    def check(left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (left.key == right.key and
                check(left.left, right.right) and
                check(left.right, right.left))
    if root is None:
        return True
    return check(root.left, root.right)
