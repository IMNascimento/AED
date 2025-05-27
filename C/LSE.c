#include <stdlib.h>
#include <stdio.h>


typedef struct List {
    int legth;
    struct Node *head, tail;
} List; 

// Definição do nó
typedef struct Node {
    int valor;
    struct Node *prox;
} Node;

// Inserção no início
Node *inserir(Node *head, int v) {
    Node *n = malloc(sizeof(Node));
    n->valor = v;
    n->prox = head;
    return n;
}

// Remover valor do início
Node *remover(Node *head, int *ret) {
    if (!head) return NULL;
    Node *tmp = head;
    *ret = tmp->valor;
    head = head->prox;
    free(tmp);
    return head;
}