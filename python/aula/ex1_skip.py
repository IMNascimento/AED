# faça um algoritmo string busca (int x, No *skiplist) de forma recursiva: 
#aonde nome só existe no nível 0, e retorna o nó se encontrado, senão None.
def busca(x, skiplist):
    """
    Busca um     valor x na SkipList de forma recursiva.
    Retorna o nó se encontrado, ou None se não existir.
    """
    def busca_rec(no, nivel):
        if nivel < 0:  # Se chegou no nível -1, não encontrou
            return None
        if no is None:  # Se o nó é None, não encontrou
            return None
        if no.value == x:  # Se encontrou o valor
            return no
        if nivel == 0:  # No nível 0, só pode avançar para o próximo nó
            return busca_rec(no.forward[0], 0)
        else:  # Nos níveis superiores, pode avançar ou descer
            if no.forward[nivel] and no.forward[nivel].value <= x:
                return busca_rec(no.forward[nivel], nivel)
            else:
                return busca_rec(no.forward[nivel - 1], nivel - 1)

    return busca_rec(skiplist.header, skiplist.level)  # Começa do cabeçalho e nível máximo

# Exemplo de uso:
skiplist = SkipList(max_level=3, p=0.5)
skiplist.insert(10)
skiplist.insert(20)
skiplist.insert(30)
result = busca(20, skiplist)
if result:
    print(f"Encontrado: {result.value}")
else:
    print("Não encontrado")