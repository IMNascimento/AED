def menor_prefixo_comum(raiz):
    prefixo = ""
    no = raiz
    while True:
        filhos = [i for i, f in enumerate(no.filhos) if f is not None]
        if len(filhos) != 1 or no.ehChave:
            break
        idx = filhos[0]
        prefixo += str(idx)
        no = no.filhos[idx]
    return prefixo if prefixo else None  # None se não houver prefixo comum
