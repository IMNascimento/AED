class NoAVL:
    def __init__(self, fb=0, esq=None, dir=None):
        self.fb = fb
        self.esq = esq
        self.dir = dir

def altura_avl(no):
    if no is None:
        return 0

    if no.fb == 0:
        he = altura_avl(no.esq)  # ou no.dir
        return he + 1
    elif no.fb == -1:
        he = altura_avl(no.esq)
        return he + 1
    elif no.fb == 1:
        hd = altura_avl(no.dir)
        return hd + 1
