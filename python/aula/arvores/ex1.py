#suponha uma arvore n-aria implementada como uma arvore binaria faça os algoritmos:
# pre-ordem, in-ordem e pos-ordem e largura

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)


class NodeBinario:
    def __init__(self, value):
        self.value = value
        self.children = None
        self.sibling = None