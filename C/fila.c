#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100  // Tamanho máximo da fila

typedef struct Queue {
    int data[MAX_SIZE];
    int front;
    int rear;
    int size;
} Queue;

// Inicializa a fila
void initQueue(Queue* q) {
    q->front = 0;
    q->rear = -1;
    q->size = 0;
}

// Verifica se a fila está vazia
int isQueueEmpty(Queue* q) {
    return q->size == 0;
}

// Verifica se a fila está cheia
int isQueueFull(Queue* q) {
    return q->size == MAX_SIZE;
}

// Enfileira (enqueue)
void enqueue(Queue* q, int value) {
    if (isQueueFull(q)) {
        printf("Erro: fila cheia.\n");
        return;
    }
    q->rear = (q->rear + 1) % MAX_SIZE;
    q->data[q->rear] = value;
    q->size++;
}

// Desenfileira (dequeue) e retorna valor
int dequeue(Queue* q) {
    if (isQueueEmpty(q)) {
        printf("Erro: fila vazia.\n");
        return -1; // valor de erro
    }
    int value = q->data[q->front];
    q->front = (q->front + 1) % MAX_SIZE;
    q->size--;
    return value;
}

// Retorna elemento da frente sem remover (peek)
int peekQueue(Queue* q) {
    if (isQueueEmpty(q)) {
        printf("Erro: fila vazia.\n");
        return -1;
    }
    return q->data[q->front];
}

// Exibe a fila desde a frente até o final
void displayQueue(Queue* q) {
    if (isQueueEmpty(q)) {
        printf("Fila vazia.\n");
        return;
    }
    printf("Fila (frente -> traseira): ");
    for (int i = 0; i < q->size; i++) {
        int index = (q->front + i) % MAX_SIZE;
        printf("%d ", q->data[index]);
    }
    printf("\n");
}

int main() {
    Queue q;
    initQueue(&q);

    // Teste de operações
    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);
    displayQueue(&q);
    printf("Peek: %d\n", peekQueue(&q));
    printf("Dequeue: %d\n", dequeue(&q));
    displayQueue(&q);
    printf("Empty? %s\n", isQueueEmpty(&q) ? "Sim" : "Não");

    // Teste de overflow
    for (int i = 0; i < MAX_SIZE; i++) {
        enqueue(&q, i);
    }
    enqueue(&q, 1000);  // Deve exibir erro de fila cheia

    return 0;
}