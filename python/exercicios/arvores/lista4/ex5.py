def descomprime_huffman(codigo, raiz):
    res = ""
    no = raiz
    for bit in codigo:
        if bit == "0":
            no = no.left
        else:
            no = no.right
        if getattr(no, "caractere", None) is not None:
            res += no.caractere
            no = raiz
    return res
