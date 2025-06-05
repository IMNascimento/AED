import random

class SkipListNode:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level=4, p=0.5):
        self.max_level = max_level
        self.p = p
        self.header = SkipListNode("Header", self.max_level)
        self.level = 0

    def random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, value):
        current = self.header
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        return current if current and current.value == value else None

    def insert(self, value, level=None):
        update = [None] * (self.max_level + 1)
        current = self.header
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if not current or current.value != value:
            if level is None:
                lvl = self.random_level()
            else:
                lvl = level
            if lvl > self.level:
                for i in range(self.level + 1, lvl + 1):
                    update[i] = self.header
                self.level = lvl
            new_node = SkipListNode(value, lvl)
            for i in range(lvl + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node


    def delete(self, value):
        update = [None] * (self.max_level + 1)
        current = self.header
        for i in reversed(range(self.level + 1)):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current and current.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]
            while self.level > 0 and not self.header.forward[self.level]:
                self.level -= 1

    def print_skiplist_ascii(self):
        out = ""
        for lvl in range(self.level, -1, -1):
            node = self.header.forward[lvl]
            level_nodes = []
            while node:
                level_nodes.append(str(node.value))
                node = node.forward[lvl]
            out += f"Level {lvl}: {' -> '.join(level_nodes)}\n"
        return out
