# uma skiplist armazena uma distribuição qualquer um programador quer retornar os valores para 
# gerar um grafico de media movel com uma janela de x e [2, log n] como fazer ?
#É aceitavel uma solução aproximada, mas é importante ser rapida

import random
import math
from collections import deque

import random
import time

class SkipListNode:
    """
    Representa um nó da SkipList, que guarda um valor e ponteiros para frente em vários níveis.
    """
    def __init__(self, value, level):
        self.value = value                              # Valor armazenado neste nó
        self.forward = [None] * (level + 1)             # Lista de ponteiros para frente (um para cada nível)
        self.nome = f" Nome de {value}"  # Atributo adicional para nome, se necessário

class SkipList:
    """
    Implementa a estrutura de dados SkipList.
    """
    def __init__(self, max_level, p):
        self.max_level = max_level                      # Nível máximo da SkipList
        self.p = p                                      # Probabilidade para sorteio de níveis
        self.header = SkipListNode(None, self.max_level)  # Nó cabeçalho vazio
        self.level = 0                                  # Nível atual mais alto da lista

    def random_level(self):
        """
        Sorteia um nível para o novo nó usando a probabilidade p.
        Aumenta o nível enquanto random.random() < p e não passar do máximo.
        """
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl


    def insert(self, value):
        """
        Insere um novo valor na SkipList (se não existir ainda).
        """
        update = [None] * (self.max_level + 1)          # Lista para guardar onde atualizar os ponteiros
        current = self.header

        # Do nível mais alto para baixo, move até encontrar onde inserir
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current                         # Guarda último nó menor em cada nível

        current = current.forward[0]                    # Avança para o próximo no nível 0

        if not current or current.value != value:       # Só insere se não existir ainda
            lvl = self.random_level()                   # Sorteia o nível do novo nó

            # Se o nível for maior que o atual da SkipList, atualiza a lista
            if lvl > self.level:
                for i in range(self.level + 1, lvl + 1):
                    update[i] = self.header
                self.level = lvl

            new_node = SkipListNode(value, lvl)         # Cria o novo nó
            # Atualiza os ponteiros para inserir o novo nó em todos os níveis sorteados
            for i in range(lvl + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def delete(self, value):
        """
        Remove um valor da SkipList, se ele existir.
        """
        update = [None] * (self.max_level + 1)          # Lista de atualização de ponteiros
        current = self.header

        # Move em cada nível até achar o valor (ou saber que não está ali)
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]

        # Se encontrou o nó, remove ajustando os ponteiros em cada nível
        if current and current.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            # Ajusta o nível da SkipList se necessário
            while self.level > 0 and not self.header.forward[self.level]:
                self.level -= 1


def moving_average(data, window_size):
    """
    Calcula a média móvel de uma lista de dados com uma janela de tamanho especificado.
    """
    if window_size <= 0 or window_size > len(data):
        return []

    averages = []
    window = deque(maxlen=window_size)  # Usando deque para manter a janela de tamanho fixo

    for value in data:
        window.append(value)
        averages.append(sum(window) / len(window))  # Calcula a média da janela atual

    return averages
def generate_skiplist_data(skiplist, n):
    """
    Gera uma lista de valores da SkipList para calcular a média móvel.
    """
    data = []
    current = skiplist.header.forward[0]  # Começa do nível 0
    while current:
        data.append(current.value)
        current = current.forward[0]  # Avança para o próximo nó no nível 0
    return data
def moving_average_skiplist(skiplist, window_size):
    """
    Calcula a média móvel dos valores armazenados na SkipList.
    """
    data = generate_skiplist_data(skiplist, skiplist.level)
    return moving_average(data, window_size)




# Exemplo de uso:
skiplist = SkipList(max_level=3, p=0.5)
skiplist.insert(10)                   
skiplist.insert(20)
skiplist.insert(30)
skiplist.insert(40)
skiplist.insert(50)
window_size = 4
averages = moving_average_skiplist(skiplist, window_size)
print("Média móvel:", averages)
#Exemplo de uso:
#skiplist = SkipList(max_level=3, p=0.5)
# skiplist.insert(10)
# skiplist.insert(20)
# skiplist.insert(30)
# window_size = 2
# averages = moving_average_skiplist(skiplist, window_size)
# print("Média móvel:", averages)
# Exemplo de uso:
# skiplist = SkipList(max_level=3, p=0.5)
# skiplist.insert(10)
# skiplist.insert(20)
# skiplist.insert(30)
# window_size = 2
# averages = moving_average_skiplist(skiplist, window_size)