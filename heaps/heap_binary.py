class Heap:
    def __init__(self):
        self.heap = []  # Inicializa uma lista vazia para o heap

    def insert(self, element):
        # Insere um novo elemento no heap
        self.heap.append(element)  # Adiciona o elemento ao final da lista
        self._heapify_up(len(self.heap) - 1)  # Corrige a posição do novo elemento

    def extract_max(self):
        # Remove e retorna o maior elemento do heap
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move o último elemento para a raiz
        self._heapify_down(0)  # Corrige a posição do novo elemento na raiz
        return root

    def _heapify_up(self, index):
        # Corrige a posição do elemento subindo no heap
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        # Corrige a posição do elemento descendo no heap
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def get_max(self):
        # Retorna o maior elemento do heap sem removê-lo
        if not self.heap:
            return None
        return self.heap[0]

    def __str__(self):
        # Retorna a representação em string do heap
        return str(self.heap)

# Exemplo de uso
if __name__ == "__main__":
    heap = Heap()
    heap.insert(10)
    heap.insert(5)
    heap.insert(3)
    heap.insert(2)
    heap.insert(8)
    heap.insert(15)

    print("Heap após inserções:")
    print(heap)

    print("\nMaior elemento extraído:", heap.extract_max())
    print("Heap após extração:")
    print(heap)

    print("\nMaior elemento atual:", heap.get_max())