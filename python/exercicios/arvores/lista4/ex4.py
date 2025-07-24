def codifica_huffman(seq, tabela):
    # tabela = [[char, codigo], ...]
    cod_map = {char: codigo for char, codigo in tabela}
    return "".join(cod_map[c] for c in seq)
