class CircularArray:
    """
    Implementação de lista circular contígua (buffer circular) em Python.

    Métodos:
      - __init__(capacity): define capacidade
      - is_empty(): verifica se vazia
      - is_full(): verifica se cheia
      - insert_end(value): insere no final
      - insert_beginning(value): insere no início
      - delete_end(): remove e retorna do final
      - delete_beginning(): remove e retorna do início
      - delete_value(value): remove a primeira ocorrência
      - search(value): retorna índice ou -1
      - display(): retorna lista de elementos em ordem
      - is_at_end(index): verifica se índice é o último elemento (tail)
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.head = 0
        self.tail = -1
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def insert_end(self, value):
        if self.is_full():
            raise OverflowError("Lista cheia")
        self.tail = (self.tail + 1) % self.capacity
        self.data[self.tail] = value
        self.size += 1
        if self.size == 1:
            self.head = self.tail

    def insert_beginning(self, value):
        if self.is_full():
            raise OverflowError("Lista cheia")
        self.head = (self.head - 1 + self.capacity) % self.capacity
        self.data[self.head] = value
        self.size += 1
        if self.size == 1:
            self.tail = self.head

    def delete_end(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        value = self.data[self.tail]
        self.data[self.tail] = None
        self.tail = (self.tail - 1 + self.capacity) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.head = 0
            self.tail = -1
        return value

    def delete_beginning(self):
        if self.is_empty():
            raise IndexError("Lista vazia")
        value = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.head = 0
            self.tail = -1
        return value

    def delete_value(self, value):
        idx = self.search(value)
        if idx == -1:
            raise ValueError(f"Valor {value} não encontrado")
        # shift elements
        next_idx = (idx + 1) % self.capacity
        while next_idx != (self.tail + 1) % self.capacity:
            self.data[idx] = self.data[next_idx]
            idx = next_idx
            next_idx = (next_idx + 1) % self.capacity
        # clear last
        self.data[self.tail] = None
        self.tail = (self.tail - 1 + self.capacity) % self.capacity
        self.size -= 1
        if self.size == 0:
            self.head = 0
            self.tail = -1

    def search(self, value):
        if self.is_empty():
            return -1
        idx = self.head
        for _ in range(self.size):
            if self.data[idx] == value:
                return idx
            idx = (idx + 1) % self.capacity
        return -1

    def display(self):
        result = []
        idx = self.head
        for _ in range(self.size):
            result.append(self.data[idx])
            idx = (idx + 1) % self.capacity
        return result

    def is_at_end(self, index):
        """Retorna True se o índice (0..capacity-1) for a cauda atual"""
        return index == self.tail

    def __repr__(self):
        return f"CircularArray({self.display()})"

# Exemplo de uso
if __name__ == "__main__":
    ca = CircularArray(5)
    ca.insert_end(1)
    ca.insert_end(2)
    ca.insert_beginning(0)
    print("Lista:", ca)
    print("Search 2 at idx:", ca.search(2))
    print("Is at end?", ca.is_at_end(ca.tail))
    print("Delete beginning:", ca.delete_beginning())
    print("Delete value 2")
    ca.delete_value(2)
    print("Lista final:", ca)