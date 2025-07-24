class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.cod = ""

def preenche_codigos(node, cod=""):
    if node is None:
        return
    node.cod = cod
    preenche_codigos(node.left, cod + "0")
    preenche_codigos(node.right, cod + "1")