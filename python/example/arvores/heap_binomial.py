class BinomialHeapNode:
    def __init__(self, key):
        self.key = key
        self.children = []
        self.degree = 0

class BinomialHeap:
    def __init__(self):
        self.trees = []

    def merge(self, other):
        self.trees += other.trees
        self.trees.sort(key=lambda x: x.degree)
        i = 0
        while i+1 < len(self.trees):
            if self.trees[i].degree == self.trees[i+1].degree:
                if (i+2 < len(self.trees) and 
                    self.trees[i].degree == self.trees[i+2].degree):
                    i += 1
                    continue
                if self.trees[i].key < self.trees[i+1].key:
                    self.trees[i].children.append(self.trees[i+1])
                    self.trees[i].degree += 1
                    del self.trees[i+1]
                else:
                    self.trees[i+1].children.append(self.trees[i])
                    self.trees[i+1].degree += 1
                    del self.trees[i]
            else:
                i += 1

    def insert(self, key):
        new_heap = BinomialHeap()
        new_heap.trees.append(BinomialHeapNode(key))
        self.merge(new_heap)

    def get_min(self):
        if not self.trees:
            return None
        min_tree = min(self.trees, key=lambda x: x.key)
        return min_tree.key
