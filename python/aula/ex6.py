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