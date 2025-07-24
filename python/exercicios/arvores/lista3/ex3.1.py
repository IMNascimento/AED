def subir(heap, i, m):
    while i > 0:
        pai = (i - 1) // m
        if heap[i] < heap[pai]:
            heap[i], heap[pai] = heap[pai], heap[i]
            i = pai
        else:
            break

def descer(heap, i, m, n):
    while True:
        menor = i
        for k in range(1, m+1):
            filho = m*i + k
            if filho < n and heap[filho] < heap[menor]:
                menor = filho
        if menor != i:
            heap[i], heap[menor] = heap[menor], heap[i]
            i = menor
        else:
            break
