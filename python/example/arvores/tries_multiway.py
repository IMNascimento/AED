class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        node = self.root
        for char in word:
            idx = self._char_to_index(char)
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            idx = self._char_to_index(char)
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            idx = self._char_to_index(char)
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True
