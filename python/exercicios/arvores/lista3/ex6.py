class NoBin:
    def __init__(self, chave):
        self.pai = None
        self.filho = None
        self.irmao = None
        self.chave = chave
        self.grau = 0

def unir_arvores(y, z):
    """Unir duas árvores de mesmo grau; y < z"""
    y.pai = z
    y.irmao = z.filho
    z.filho = y
    z.grau += 1
    return z

def uniao_heaps(h1, h2):
    """Unir dois heaps binomiais (h1, h2 são listas de raízes ordenadas por grau)"""
    def merge(h1, h2):
        # Junta as listas ordenadas por grau
        res = []
        i = j = 0
        while i < len(h1) and j < len(h2):
            if h1[i].grau < h2[j].grau:
                res.append(h1[i])
                i += 1
            else:
                res.append(h2[j])
                j += 1
        res += h1[i:] + h2[j:]
        return res

    heap = merge(h1, h2)
    if not heap:
        return []
    i = 0
    while i < len(heap)-1:
        curr = heap[i]
        prox = heap[i+1]
        if curr.grau == prox.grau:
            # Precisa unir!
            if curr.chave < prox.chave:
                unir_arvores(prox, curr)
                heap.pop(i+1)
            else:
                unir_arvores(curr, prox)
                heap.pop(i)
        else:
            i += 1
    return heap
