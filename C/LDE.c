#include <stdio.h>
#include <stdlib.h>

// Definição do nó duplamente encadeado
typedef struct DNode {
    int valor;
    struct DNode* ant;
    struct DNode* prox;
} DNode;

// Cria lista vazia
DNode* criar_lde() {
    return NULL;
}

// Insere no início
DNode* insere_lde(DNode* head, int v) {
    DNode* novo = malloc(sizeof(DNode));
    if (!novo) return head;
    novo->valor = v;
    novo->ant = NULL;
    novo->prox = head;
    if (head) head->ant = novo;
    return novo;
}

// Remove nó do meio dado o ponteiro para ele
DNode* remove_lde(DNode* head, DNode* node) {
    if (!node) return head;
    if (node->ant) node->ant->prox = node->prox;
    else head = node->prox;          // se era head
    if (node->prox) node->prox->ant = node->ant;
    free(node);
    return head;
}

// Imprime lista para frente
void imprimir_lde(DNode* head) {
    DNode* temp = head;
    while (temp) {
        printf("%d <-> ", temp->valor);
        temp = temp->prox;
    }
    printf("NULL\n");
}

// Imprime lista para trás
void imprimir_lde_reverso(DNode* head) {
    if (!head) { 
        printf("Lista vazia\n"); 
        return; 
    }
    DNode* temp = head;
    while (temp->prox) temp = temp->prox;  // vai até o fim
    while (temp) {
        printf("%d <-> ", temp->valor);
        temp = temp->ant;
    }
    printf("NULL\n");  // Corrigido: faltava \n correto
}

// Função para liberar toda a memória da lista
void liberar_lista(DNode* head) {
    DNode* atual = head;
    DNode* proximo;
    
    while (atual) {
        proximo = atual->prox;
        free(atual);
        atual = proximo;
    }
}

int main() {
    DNode* head = criar_lde();
    head = insere_lde(head, 10);
    head = insere_lde(head, 20);
    head = insere_lde(head, 30);
    
    printf("Lista original:\n");
    imprimir_lde(head);
    
    printf("Lista reversa:\n");
    imprimir_lde_reverso(head);
    
    // remover o segundo nó
    head = remove_lde(head, head->prox);
    printf("Lista após remoção do segundo elemento:\n");
    imprimir_lde(head);
    
    // Liberar memória antes de encerrar
    liberar_lista(head);
    
    return 0;
}