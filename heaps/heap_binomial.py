class BinomialTree:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.degree = 0

    def add_child(self, child_tree):
        self.children.append(child_tree)
        self.degree += 1

class BinomialHeap:
    def __init__(self):
        self.trees = []

    def _merge_trees(self, tree1, tree2):
        if tree1.key > tree2.key:
            tree1, tree2 = tree2, tree1
        tree1.add_child(tree2)
        return tree1

    def insert(self, key):
        new_tree = BinomialTree(key)
        self._union(new_tree)

    def _union(self, new_tree):
        temp_trees = self.trees[:]
        self.trees = []
        carry = new_tree

        while temp_trees or carry:
            if not temp_trees:
                self.trees.append(carry)
                carry = None
            elif not carry:
                self.trees.append(temp_trees.pop(0))
            elif temp_trees[0].degree < carry.degree:
                self.trees.append(temp_trees.pop(0))
            elif temp_trees[0].degree > carry.degree:
                self.trees.append(carry)
                carry = None
            else:
                carry = self._merge_trees(temp_trees.pop(0), carry)

    def get_min(self):
        if not self.trees:
            return None
        min_tree = min(self.trees, key=lambda tree: tree.key)
        return min_tree.key

    def extract_min(self):
        if not self.trees:
            return None

        min_tree_index = min(range(len(self.trees)), key=lambda i: self.trees[i].key)
        min_tree = self.trees.pop(min_tree_index)
        removed_children = min_tree.children[::-1]

        for child in removed_children:
            self._union(child)

        return min_tree.key

    def __str__(self):
        return ' '.join(str(tree.key) for tree in self.trees)

# Exemplo de uso
if __name__ == "__main__":
    bh = BinomialHeap()
    bh.insert(10)
    bh.insert(5)
    bh.insert(20)
    bh.insert(2)

    print("Heap binomial após inserções:")
    print(bh)

    print("\nMenor elemento:", bh.get_min())
    print("\nMenor elemento extraído:", bh.extract_min())
    print("Heap binomial após extração do menor elemento:")
    print(bh)

    print("\nMenor elemento:", bh.get_min())