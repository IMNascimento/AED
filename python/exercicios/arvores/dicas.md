# 📘 ESTUDO INTENSIVO DE ESTRUTURAS AVANÇADAS DE ÁRVORES E HEAPS

---

## 1. Árvore Binária de Busca (BST)

### Estrutura

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
```

### Inserção

```python
def inserir(node, key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = inserir(node.left, key)
    else:
        node.right = inserir(node.right, key)
    return node
```

### Busca

```python
def buscar(node, key):
    if node is None or node.key == key:
        return node
    if key < node.key:
        return buscar(node.left, key)
    else:
        return buscar(node.right, key)
```

### Remoção

```python
def remover(node, key):
    if node is None:
        return None
    if key < node.key:
        node.left = remover(node.left, key)
    elif key > node.key:
        node.right = remover(node.right, key)
    else:  # Achou
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        temp = node.right
        while temp.left:
            temp = temp.left
        node.key = temp.key
        node.right = remover(node.right, temp.key)
    return node
```

### Percursos

- **Pré-ordem:** raiz, esquerda, direita
- **In-ordem:** esquerda, raiz, direita (ordem crescente em BST)
- **Pós-ordem:** esquerda, direita, raiz

```python
def pre_ordem(node):   # Pré-ordem
    if node:
        print(node.key)
        pre_ordem(node.left)
        pre_ordem(node.right)

def in_ordem(node):    # In-ordem
    if node:
        in_ordem(node.left)
        print(node.key)
        in_ordem(node.right)

def pos_ordem(node):   # Pós-ordem
    if node:
        pos_ordem(node.left)
        pos_ordem(node.right)
        print(node.key)
```

---

## 2. Árvore AVL (Árvore Binária de Busca Balanceada)

### Estrutura

```python
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.fator_balanceamento = 0  # FB = altura direita - altura esquerda
```

### Rotações AVL (COM ATUALIZAÇÃO DO FB)

```python
def altura(node):
    if node is None:
        return 0
    return 1 + max(altura(node.left), altura(node.right))

def atualiza_fb(node):
    if node is None:
        return
    node.fator_balanceamento = altura(node.right) - altura(node.left)

def rotacao_esq(x):
    y = x.right
    x.right = y.left
    y.left = x
    atualiza_fb(x)
    atualiza_fb(y)
    return y

def rotacao_dir(y):
    x = y.left
    y.left = x.right
    x.right = y
    atualiza_fb(y)
    atualiza_fb(x)
    return x

def rotacao_esq_dir(z):
    z.left = rotacao_esq(z.left)
    return rotacao_dir(z)

def rotacao_dir_esq(z):
    z.right = rotacao_dir(z.right)
    return rotacao_esq(z)
```

### Verificar se é AVL

```python
def eh_avl(node):
    if node is None:
        return True, 0
    esq_avl, h_esq = eh_avl(node.left)
    dir_avl, h_dir = eh_avl(node.right)
    fb = h_dir - h_esq
    node.fator_balanceamento = fb
    ok = esq_avl and dir_avl and (fb in [-1, 0, 1])
    altura_no = 1 + max(h_esq, h_dir)
    return ok, altura_no
```

### Altura mais rápida usando FB

```python
def altura_otimizada(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    if node.left is None:
        return 1 + altura_otimizada(node.right)
    if node.right is None:
        return 1 + altura_otimizada(node.left)
    if node.fator_balanceamento >= 0:
        return 1 + altura_otimizada(node.right)
    else:
        return 1 + altura_otimizada(node.left)
```

---

## 3. Heap Binário (Min-heap ou Max-heap)

### Representação em vetor

- Pai: `(i-1)//2`
- Esquerda: `2*i + 1`
- Direita: `2*i + 2`

### Inserção no Min-heap

```python
def inserir_heap(heap, valor):
    heap.append(valor)
    i = len(heap) - 1
    while i > 0 and heap[i] < heap[(i-1)//2]:
        heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
        i = (i-1)//2
```

### Remoção da raiz

```python
def remover_min(heap):
    if len(heap) == 0:
        return None
    raiz = heap[0]
    heap[0] = heap.pop()
    i = 0
    n = len(heap)
    while True:
        menor = i
        e = 2*i + 1
        d = 2*i + 2
        if e < n and heap[e] < heap[menor]:
            menor = e
        if d < n and heap[d] < heap[menor]:
            menor = d
        if menor == i:
            break
        heap[i], heap[menor] = heap[menor], heap[i]
        i = menor
    return raiz
```

---

## 4. Heap Binomial

### Árvore de grau k

- Tem k filhos, altura k, C(k,i) nós no nível i (coeficiente binomial).

### União de heaps binomiais

```python
def unir_arvores_binomiais(y, z):
    y.pai = z
    y.irmao = z.filho
    z.filho = y
    z.grau += 1
    return z
```

---

## 5. Árvores Digitais (TRIE/RWAY)

### Estrutura do nó (dígitos 0-9)

```python
class NoTRIE:
    def __init__(self):
        self.ehChave = False
        self.filhos = [None] * 10  # '0' a '9'
```

### Inserir chave

```python
def inserir_trie(raiz, chave):
    no = raiz
    for c in chave:
        idx = int(c)
        if no.filhos[idx] is None:
            no.filhos[idx] = NoTRIE()
        no = no.filhos[idx]
    no.ehChave = True
```

### Buscar chave

```python
def buscar_trie(raiz, chave):
    no = raiz
    for c in chave:
        idx = int(c)
        if no.filhos[idx] is None:
            return False
        no = no.filhos[idx]
    return no.ehChave
```

### Imprimir todas as chaves com prefixo q

```python
def imprime_chaves_prefixo(raiz, q):
    def dfs(no, prefixo):
        if no.ehChave:
            print(prefixo)
        for i, filho in enumerate(no.filhos):
            if filho:
                dfs(filho, prefixo + str(i))
    no = raiz
    for c in q:
        idx = int(c)
        if no.filhos[idx] is None:
            return
        no = no.filhos[idx]
    dfs(no, q)
```

---

## 5.1. Árvore Digital Compacta (Patricia)

A **árvore Patricia** é uma variação da trie, compactando cadeias de nós que não ramificam, economizando espaço e tornando busca e inserção mais eficientes para grandes conjuntos de strings ou chaves binárias.

### Estrutura do nó (simplificada)

```python
class PatriciaNode:
    def __init__(self, label):
        self.label = label  # String armazenada neste nó (pode ser mais de um caractere)
        self.children = {}  # Dicionário: próximo caractere -> nó filho
        self.is_key = False # Se é fim de chave
```

### Inserção na Patricia

```python
def inserir_patricia(node, chave):
    if not chave:
        node.is_key = True
        return
    for child_label, child in node.children.items():
        # Procura maior prefixo comum
        i = 0
        while i < len(child_label) and i < len(chave) and child_label[i] == chave[i]:
            i += 1
        if i > 0:
            # Precisa dividir o nó
            if i < len(child_label):
                novo_filho = PatriciaNode(child_label[i:])
                novo_filho.children = child.children
                novo_filho.is_key = child.is_key
                child.label = child_label[:i]
                child.children = {child_label[i]: novo_filho}
                child.is_key = child.is_key if i == len(child_label) and child.is_key else False
            inserir_patricia(child, chave[i:])
            return
    # Se não achou prefixo comum, cria novo filho
    node.children[chave[0]] = PatriciaNode(chave)
    node.children[chave[0]].is_key = True
```

### Busca na Patricia

```python
def buscar_patricia(node, chave):
    if not chave:
        return node.is_key
    for child_label, child in node.children.items():
        if chave.startswith(child_label):
            return buscar_patricia(child, chave[len(child_label):])
        if child_label.startswith(chave):
            return False  # chave é prefixo de um label, mas não existe
    return False
```

### Pontos-chave:

- Patricia **compacta caminhos**: economiza espaço e torna busca/inserção mais rápida em dados grandes.
- Cada aresta/arco pode ter uma string inteira, não apenas um caractere.
- Útil para conjuntos grandes de strings, prefixos, IPv4/IPv6, etc.

---

## 6. Huffman (compressão de dados)

### Criar árvore de Huffman manualmente

```python
class HuffmanNo:
    def __init__(self, freq, caractere=None, left=None, right=None):
        self.freq = freq
        self.caractere = caractere
        self.left = left
        self.right = right

def cria_huffman(frequencias):
    nos = []
    for char, freq in frequencias.items():
        nos.append(HuffmanNo(freq, char))
    while len(nos) > 1:
        # Encontra dois menores
        idx_min1 = idx_min2 = -1
        min1 = min2 = float('inf')
        for i, no in enumerate(nos):
            if no.freq < min1:
                min2, idx_min2 = min1, idx_min1
                min1, idx_min1 = no.freq, i
            elif no.freq < min2:
                min2, idx_min2 = no.freq, i
        idxs = sorted([idx_min1, idx_min2], reverse=True)
        no1 = nos.pop(idxs[0])
        no2 = nos.pop(idxs[1])
        novo = HuffmanNo(no1.freq + no2.freq, None, no1, no2)
        nos.append(novo)
    return nos[0]
```

### Gerar tabela de códigos

```python
def tabela_huffman(raiz):
    tabela = []
    def dfs(no, codigo):
        if no is None:
            return
        if getattr(no, "caractere", None) is not None:
            tabela.append([no.caractere, codigo])
        dfs(no.left, codigo + "0")
        dfs(no.right, codigo + "1")
    dfs(raiz, "")
    return tabela
```

### Codificar e decodificar

```python
def codifica_huffman(seq, tabela):
    cod_map = {char: codigo for char, codigo in tabela}
    return "".join(cod_map[c] for c in seq)

def descomprime_huffman(codigo, raiz):
    res = ""
    no = raiz
    for bit in codigo:
        no = no.left if bit == "0" else no.right
        if getattr(no, "caractere", None) is not None:
            res += no.caractere
            no = raiz
    return res
```

---

# DICAS FINAIS PARA ESTUDOS

- Sempre entenda a estrutura (desenhe!) antes de implementar.
- Em BST, AVL: sempre compare, recursivamente, à esquerda ou à direita.
- Em heaps: lembre-se da estrutura de vetor e das posições dos filhos/pais.
- Em TRIE: navegue pelo índice (dígito ou letra) de cada caractere.
- Huffman: é construção por combinação dos menores até restar um só nó (a raiz).
- Entenda as diferenças entre árvores binárias de busca (ordem < ou >), AVL (balanceada), heaps (prioridade no topo), TRIE (prefixos), Huffman (compressão ótima).

> **Revise exemplos, desenhe árvores, e lembre-se dos percursos!**
>
> Se tiver dúvidas nos 5 minutos finais, foque nas funções de **inserção e busca**: caem em todas as estruturas!
>
> **Bons estudos!**

