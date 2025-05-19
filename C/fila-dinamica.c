#include <stdlib.h>
#include <stdio.h>

// Nó da fila
typedef struct Node {
    int valor;
    struct Node *prox;
} Node;

// Fila com ponteiros para frente e tras
typedef struct {
    Node *front, *rear;
    int tamanho;
} Queue;

// Cria fila vazia\ nQueue *criar() {
    Queue *q = malloc(sizeof(Queue));
    q->front = q->rear = NULL;
    q->tamanho = 0;
    return q;
}

// Destrói fila e libera nós
void destruir(Queue *q) {
    while (q->front) {
        Node *tmp = q->front;
        q->front = tmp->prox;
        free(tmp);
    }
    free(q);
}

// Enfileira
void enqueue(Queue *q, int v) {
    Node *node = malloc(sizeof(Node));
    node->valor = v;
    node->prox = NULL;
    if (!q->rear) q->front = node;
    else q->rear->prox = node;
    q->rear = node;
    q->tamanho++;
}

// Desenfileira
int dequeue(Queue *q) {
    if (!q->front) return -1;
    Node *tmp = q->front;
    int v = tmp->valor;
    q->front = tmp->prox;
    if (!q->front) q->rear = NULL;
    free(tmp);
    q->tamanho--;
    return v;
}

// Informações da fila
int tamanho(Queue *q) { return q->tamanho; }
int vazia(Queue *q) { return q->tamanho == 0; }