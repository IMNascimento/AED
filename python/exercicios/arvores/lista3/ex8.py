def alterar_prioridade(no, nova_chave):
    if nova_chave > no.chave:
        raise Exception("Nova chave maior, para heap mínimo só diminui prioridade.")
    no.chave = nova_chave
    y = no
    z = no.pai
    while z is not None and y.chave < z.chave:
        y.chave, z.chave = z.chave, y.chave
        y = z
        z = y.pai
