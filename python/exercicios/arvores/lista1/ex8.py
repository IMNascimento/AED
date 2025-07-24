def busca(item, l, r, raiz, valor):
    if raiz == 0:
        return 0
    if item[raiz] == valor:
        return raiz
    if valor < item[raiz]:
        return busca(item, l, r, l[raiz], valor)
    else:
        return busca(item, l, r, r[raiz], valor)

def insere(item, l, r, raiz, valor, idx_vazio):
    if raiz == 0:
        item[idx_vazio] = valor
        l[idx_vazio] = 0
        r[idx_vazio] = 0
        return idx_vazio
    if valor < item[raiz]:
        l[raiz] = insere(item, l, r, l[raiz], valor, idx_vazio)
    else:
        r[raiz] = insere(item, l, r, r[raiz], valor, idx_vazio)
    return raiz


def remove(item, l, r, raiz, valor):
    """
    Remove valor da árvore com vetores paralelos e retorna o novo índice da raiz.
    item: vetor de valores
    l: vetor de índices de filho esquerdo
    r: vetor de índices de filho direito
    raiz: índice do nó raiz
    valor: valor a ser removido
    """
    # Caso base: árvore vazia
    if raiz == 0:
        return 0

    if valor < item[raiz]:
        l[raiz] = remove(item, l, r, l[raiz], valor)
        return raiz
    elif valor > item[raiz]:
        r[raiz] = remove(item, l, r, r[raiz], valor)
        return raiz
    else:
        # Achou o nó a ser removido!
        # Caso 1: não tem filho esquerdo
        if l[raiz] == 0:
            return r[raiz]
        # Caso 2: não tem filho direito
        if r[raiz] == 0:
            return l[raiz]
        # Caso 3: dois filhos
        # Encontra o menor na subárvore direita
        succ = r[raiz]
        while l[succ] != 0:
            succ = l[succ]
        # Troca o valor do nó atual pelo sucessor
        item[raiz] = item[succ]
        # Remove o sucessor da subárvore direita
        r[raiz] = remove(item, l, r, r[raiz], item[succ])
        return raiz