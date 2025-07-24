class PatriciaNode:
    def __init__(self, label):
        self.label = label
        self.children = {}
        self.is_end = False

class PatriciaTrie:
    def __init__(self):
        self.root = PatriciaNode("")

    def insert(self, word):
        node = self.root
        while word:
            for key in node.children:
                label = key
                # encontra o prefixo comum
                i = 0
                while i < min(len(word), len(label)) and word[i] == label[i]:
                    i += 1
                if i == 0:
                    continue
                if i < len(label):
                    # split do nó
                    child = node.children[label]
                    new_child = PatriciaNode(label[i:])
                    new_child.children = child.children
                    new_child.is_end = child.is_end
                    child.label = label[:i]
                    child.children = {label[i:]: new_child}
                    child.is_end = False
                if i < len(word):
                    word = word[i:]
                    node = node.children[label[:i]]
                else:
                    node.children[label[:i]].is_end = True
                    return
                break
            else:
                node.children[word] = PatriciaNode(word)
                node.children[word].is_end = True
                return

    def search(self, word):
        node = self.root
        while word:
            found = False
            for key in node.children:
                label = key
                if word.startswith(label):
                    word = word[len(label):]
                    node = node.children[label]
                    found = True
                    break
            if not found:
                return False
        return node.is_end
