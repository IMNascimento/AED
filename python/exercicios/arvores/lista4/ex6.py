class HuffmanNo:
    def __init__(self, freq, caractere=None, left=None, right=None):
        self.freq = freq
        self.caractere = caractere
        self.left = left
        self.right = right

def cria_huffman(frequencias):
    # Cria uma lista de nós iniciais (folhas)
    nos = []
    for char, freq in frequencias.items():
        nos.append(HuffmanNo(freq, char))

    # Enquanto houver mais de um nó, combine os dois menores
    while len(nos) > 1:
        # Encontra os dois nós com menor frequência
        idx_min1 = idx_min2 = -1
        min1 = min2 = float('inf')
        for i, no in enumerate(nos):
            if no.freq < min1:
                min2, idx_min2 = min1, idx_min1
                min1, idx_min1 = no.freq, i
            elif no.freq < min2:
                min2, idx_min2 = no.freq, i

        # Tira os dois menores da lista (atenção à ordem dos índices)
        idxs = sorted([idx_min1, idx_min2], reverse=True)
        no1 = nos.pop(idxs[0])
        no2 = nos.pop(idxs[1])

        # Cria novo nó pai
        novo = HuffmanNo(no1.freq + no2.freq, None, no1, no2)
        nos.append(novo)

    # Retorna a raiz da árvore
    return nos[0]





#Exemplo Frequências de teste
#freqs = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
#raiz = cria_huffman(freqs)

# Função para imprimir a árvore (opcional)
#def imprime_huffman(no, prefixo=""):
#    if no is None:
#        return
#    if no.caractere is not None:
#        print(f"{no.caractere}: {prefixo}")
#    imprime_huffman(no.left, prefixo + "0")
#    imprime_huffman(no.right, prefixo + "1")

#imprime_huffman(raiz)