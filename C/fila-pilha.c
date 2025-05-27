#include <stdio.h>
#include <stdlib.h>

// -----------------------
// Implementação de Pilha
// -----------------------

typedef struct StackNode {
    int data;
    struct StackNode* next;
} StackNode;

// Cria nó da pilha
StackNode* createStackNode(int data) {
    StackNode* node = (StackNode*)malloc(sizeof(StackNode));
    if (!node) {
        printf("Erro ao alocar memória para pilha.\n");
        exit(EXIT_FAILURE);
    }
    node->data = data;
    node->next = NULL;
    return node;
}

// Empilha (push)
void push(StackNode** top, int data) {
    StackNode* node = createStackNode(data);
    node->next = *top;
    *top = node;
}

// Desempilha (pop)
int pop(StackNode** top) {
    if (*top == NULL) {
        printf("Pilha vazia.\n");
        return -1; // ou outro código de erro
    }
    StackNode* temp = *top;
    int value = temp->data;
    *top = temp->next;
    free(temp);
    return value;
}

// Espia o topo sem remover (peek)
int peek(StackNode* top) {
    if (top == NULL) {
        printf("Pilha vazia.\n");
        return -1;
    }
    return top->data;
}

// Verifica se pilha está vazia
int isStackEmpty(StackNode* top) {
    return top == NULL;
}

// Exibe pilha
void displayStack(StackNode* top) {
    printf("Pilha (top -> bottom): ");
    while (top) {
        printf("%d ", top->data);
        top = top->next;
    }
    printf("\n");
}

// -----------------------
// Implementação de Fila
// -----------------------

typedef struct QueueNode {
    int data;
    struct QueueNode* next;
} QueueNode;

typedef struct Queue {
    QueueNode* front;
    QueueNode* rear;
} Queue;

// Cria fila vazia
Queue* createQueue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    if (!q) {
        printf("Erro ao alocar memória para fila.\n");
        exit(EXIT_FAILURE);
    }
    q->front = q->rear = NULL;
    return q;
}

// Enfileira (enqueue)
void enqueue(Queue* q, int data) {
    QueueNode* node = (QueueNode*)malloc(sizeof(QueueNode));
    if (!node) {
        printf("Erro ao alocar memória para nó da fila.\n");
        exit(EXIT_FAILURE);
    }
    node->data = data;
    node->next = NULL;
    if (q->rear == NULL) {
        q->front = q->rear = node;
    } else {
        q->rear->next = node;
        q->rear = node;
    }
}

// Desenfileira (dequeue)
int dequeue(Queue* q) {
    if (q->front == NULL) {
        printf("Fila vazia.\n");
        return -1;
    }
    QueueNode* temp = q->front;
    int value = temp->data;
    q->front = temp->next;
    if (q->front == NULL)
        q->rear = NULL;
    free(temp);
    return value;
}

// Verifica se fila está vazia
int isQueueEmpty(Queue* q) {
    return q->front == NULL;
}

// Espia o elemento da frente sem remover
int front(Queue* q) {
    if (q->front == NULL) {
        printf("Fila vazia.\n");
        return -1;
    }
    return q->front->data;
}

// Exibe fila
void displayQueue(Queue* q) {
    printf("Fila (front -> rear): ");
    QueueNode* temp = q->front;
    while (temp) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

// -----------------------
// Função principal
// -----------------------
int main() {
    // Teste de pilha
    StackNode* stack = NULL;
    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);
    displayStack(stack);
    printf("Pop: %d\n", pop(&stack));
    displayStack(stack);
    printf("Peek: %d\n", peek(stack));
    printf("Empty? %s\n", isStackEmpty(stack) ? "Sim" : "Não");

    printf("\n");

    // Teste de fila
    Queue* queue = createQueue();
    enqueue(queue, 100);
    enqueue(queue, 200);
    enqueue(queue, 300);
    displayQueue(queue);
    printf("Dequeue: %d\n", dequeue(queue));
    displayQueue(queue);
    printf("Front: %d\n", front(queue));
    printf("Empty? %s\n", isQueueEmpty(queue) ? "Sim" : "Não");

    return 0;
}