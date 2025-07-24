class TSTNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.eq = None
        self.right = None
        self.is_end = False

class TernarySearchTrie:
    def __init__(self):
        self.root = None

    def insert(self, word):
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, idx):
        char = word[idx]
        if node is None:
            node = TSTNode(char)
        if char < node.char:
            node.left = self._insert(node.left, word, idx)
        elif char > node.char:
            node.right = self._insert(node.right, word, idx)
        else:
            if idx + 1 == len(word):
                node.is_end = True
            else:
                node.eq = self._insert(node.eq, word, idx+1)
        return node

    def search(self, word):
        return self._search(self.root, word, 0)

    def _search(self, node, word, idx):
        if not node:
            return False
        char = word[idx]
        if char < node.char:
            return self._search(node.left, word, idx)
        elif char > node.char:
            return self._search(node.right, word, idx)
        else:
            if idx + 1 == len(word):
                return node.is_end
            return self._search(node.eq, word, idx+1)
