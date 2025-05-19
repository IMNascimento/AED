import random

class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)  # Ponteiros para os nós nos diferentes níveis

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level  # Nível máximo da Skip List
        self.header = Node(None, self.max_level)  # Nó cabeça com o nível máximo
        self.level = 0  # Nível atual da Skip List

    def random_level(self):
        # Gera um nível aleatório para o novo nó
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, value):
        # Insere um valor na Skip List
        update = [None] * (self.max_level + 1)
        current = self.header

        # Encontra a posição para inserção
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        level = self.random_level()
        if level > self.level:
            for i in range(self.level + 1, level + 1):
                update[i] = self.header
            self.level = level

        new_node = Node(value, level)
        for i in range(level + 1):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, value):
        # Procura um valor na Skip List
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.value == value:
            return True
        return False

    def delete(self, value):
        # Remove um valor da Skip List
        update = [None] * (self.max_level + 1)
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]
        if current and current.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1

    def display(self):
        # Exibe os níveis da Skip List
        print("Skip List:")
        for i in range(self.level + 1):
            current = self.header.forward[i]
            print(f"Level {i}: ", end=" ")
            while current:
                print(current.value, end=" ")
                current = current.forward[i]
            print("")

# Exemplo de uso
if __name__ == "__main__":
    skiplist = SkipList(max_level=3)
    skiplist.insert(3)
    skiplist.insert(6)
    skiplist.insert(7)
    skiplist.insert(9)
    skiplist.insert(12)
    skiplist.insert(19)
    skiplist.insert(17)
    skiplist.insert(26)
    skiplist.insert(21)
    skiplist.insert(25)

    skiplist.display()

    print("\nSearch for 19:", skiplist.search(19))
    print("Search for 15:", skiplist.search(15))

    skiplist.delete(19)
    print("\nAfter deleting 19:")
    skiplist.display()