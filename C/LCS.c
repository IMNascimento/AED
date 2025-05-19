#include <stdio.h>
#include <stdlib.h>

// Definição do nó da lista circular
typedef struct Node {
    int valor;
    struct Node* prox;
} Node;

// Inicializa a lista circular vazia
Node* criar_circular() {
    return NULL;
}

// Insere no final da lista circular
Node* inserir_circular(Node* head, int v) {
    Node* novo = malloc(sizeof(Node));
    if (!novo) return head; // falha na alocação
    novo->valor = v;
    if (!head) {
        novo->prox = novo;  // aponta para si mesmo
        return novo;
    }
    Node* temp = head;
    // percorre até o último (aquele que aponta para head)
    while (temp->prox != head) {
        temp = temp->prox;
    }
    temp->prox = novo;
    novo->prox = head;
    return head;
}

// Remove o nó com valor igual a v (primeira ocorrência)
Node* remover_circular(Node* head, int v) {
    if (!head) return NULL;
    Node* cur = head;
    Node* prev = NULL;
    // lidar se é o único nó
    if (head->prox == head && head->valor == v) {
        free(head);
        return NULL;
    }
    // encontrar o nó a remover
    do {
        if (cur->valor == v) break;
        prev = cur;
        cur = cur->prox;
    } while (cur != head);
    if (cur->valor != v) return head; // não encontrado
    // ajustar ponteiros
    if (prev) {
        prev->prox = cur->prox;
        if (cur == head) head = cur->prox;
    }
    free(cur);
    return head;
}

// Percorre e imprime a lista circular\ nvoid imprimir_circular(Node* head) {
    if (!head) {
        printf("Lista vazia
");
        return;
    }
    Node* temp = head;
    do {
        printf("%d -> ", temp->valor);
        temp = temp->prox;
    } while (temp != head);
    printf("(retorna ao início)
");
}

// Exemplo de uso
int main() {
    Node* head = criar_circular();
    head = inserir_circular(head, 10);
    head = inserir_circular(head, 20);
    head = inserir_circular(head, 30);
    imprimir_circular(head);
    head = remover_circular(head, 20);
    imprimir_circular(head);
    // liberar toda a lista
    while (head) head = remover_circular(head, head->valor);
    return 0;
}