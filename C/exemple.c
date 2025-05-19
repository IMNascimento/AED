/*
 * estruturas.c
 * Exemplo Completo: Listas, Pilhas e Filas em C
 * Inclui dicas e explicações passo a passo
 * Autor: ChatGPT
 */

 #include <stdio.h>
 #include <stdlib.h>
 
 // --------------------------------------------------
 // 1. Lista Simplesmente Encadeada (LSI)
 // --------------------------------------------------
 // Cada nó contém um valor inteiro e ponteiro para o próximo nó.
 typedef struct Node {
     int valor;
     struct Node* prox;
 } Node;
 
 // Cria lista vazia (head = NULL)
 Node* criar_lista() {
     return NULL;
 }
 
 // Insere um novo nó no início da lista (O(1))
 Node* inserir_lista(Node* head, int valor) {
     Node* novo = malloc(sizeof(Node));
     if (!novo) {
         fprintf(stderr, "[ERRO] Falha ao alocar memória para nó da lista.\n");
         exit(EXIT_FAILURE);
     }
     novo->valor = valor;
     novo->prox  = head;
     return novo; // novo passa a ser a cabeça
 }
 
 // Remove o primeiro nó e retorna o valor através de ret_valor
 Node* remover_lista(Node* head, int* ret_valor) {
     if (!head) return NULL; // lista vazia
     Node* temp = head;
     *ret_valor = temp->valor;
     head = temp->prox;
     free(temp);
     return head;
 }
 
 // Imprime todos os valores da lista
 void imprimir_lista(Node* head) {
     printf("Lista: ");
     for (Node* cur = head; cur; cur = cur->prox) {
         printf("%d -> ", cur->valor);
     }
     printf("NULL\n");
 }
 
 // --------------------------------------------------
 // 2. Pilha (Stack) usando Lista Encadeada
 // --------------------------------------------------
 // LIFO: último a entrar, primeiro a sair.
 typedef Node Stack;
 
 // Empilha: insere no início da lista
 void push(Stack** top, int valor) {
     *top = inserir_lista(*top, valor);
 }
 
 // Desempilha: remove do início da lista
 int pop(Stack** top) {
     if (!*top) {
         fprintf(stderr, "[ERRO] Pilha vazia.\n");
         exit(EXIT_FAILURE);
     }
     int valor;
     *top = remover_lista(*top, &valor);
     return valor;
 }
 
 // Imprime a pilha do topo até a base
 void imprimir_pilha(Stack* top) {
     printf("Pilha (topo -> base): ");
     for (Node* cur = top; cur; cur = cur->prox) {
         printf("%d | ", cur->valor);
     }
     printf("NULL\n");
 }
 
 // --------------------------------------------------
 // 3. Fila Dinâmica (Queue) usando Lista Encadeada
 // --------------------------------------------------
 // FIFO: primeiro a entrar, primeiro a sair.
 typedef struct QueueNode {
     int valor;
     struct QueueNode* prox;
 } QueueNode;
 
 typedef struct {
     QueueNode* front;  // aponta para o primeiro elemento
     QueueNode* rear;   // aponta para o último elemento
 } Queue;
 
 // Cria fila vazia
 Queue* criar_fila() {
     Queue* q = malloc(sizeof(Queue));
     if (!q) {
         fprintf(stderr, "[ERRO] Falha ao alocar memória para fila.\n");
         exit(EXIT_FAILURE);
     }
     q->front = q->rear = NULL;
     return q;
 }
 
 // Adiciona valor no final da fila
 void enqueue(Queue* q, int valor) {
     QueueNode* novo = malloc(sizeof(QueueNode));
     if (!novo) {
         fprintf(stderr, "[ERRO] Falha ao alocar nó da fila.\n");
         exit(EXIT_FAILURE);
     }
     novo->valor = valor;
     novo->prox  = NULL;
     if (!q->rear) {
         // fila vazia
         q->front = q->rear = novo;
     } else {
         q->rear->prox = novo;
         q->rear = novo;
     }
 }
 
 // Remove valor da frente da fila
 int dequeue(Queue* q) {
     if (!q->front) {
         fprintf(stderr, "[ERRO] Fila vazia.\n");
         exit(EXIT_FAILURE);
     }
     QueueNode* temp = q->front;
     int valor = temp->valor;
     q->front = temp->prox;
     if (!q->front) q->rear = NULL; // fila esvaziou
     free(temp);
     return valor;
 }
 
 // Imprime todos os valores da fila
 void imprimir_fila(Queue* q) {
     printf("Fila (frente -> tras): ");
     for (QueueNode* cur = q->front; cur; cur = cur->prox) {
         printf("%d -> ", cur->valor);
     }
     printf("NULL\n");
 }
 
 // --------------------------------------------------
 // Função principal: demonstra uso de lista, pilha e fila
 // --------------------------------------------------
 int main() {
     int ret;
 
     // ---- Lista ----
     printf("\n=== Operações em Lista Encadeada ===\n");
     Node* lista = criar_lista();
     lista = inserir_lista(lista, 10);
     lista = inserir_lista(lista, 20);
     lista = inserir_lista(lista, 30);
     imprimir_lista(lista);
     lista = remover_lista(lista, &ret);
     printf("Removido da lista: %d\n", ret);
     imprimir_lista(lista);
 
     // ---- Pilha ----
     printf("\n=== Operações em Pilha ===\n");
     Stack* pilha = NULL;
     push(&pilha, 100);
     push(&pilha, 200);
     push(&pilha, 300);
     imprimir_pilha(pilha);
     printf("Desempilhado: %d\n", pop(&pilha));
     imprimir_pilha(pilha);
 
     // ---- Fila ----
     printf("\n=== Operações em Fila ===\n");
     Queue* fila = criar_fila();
     enqueue(fila, 1000);
     enqueue(fila, 2000);
     enqueue(fila, 3000);
     imprimir_fila(fila);
     printf("Desenfileirado: %d\n", dequeue(fila));
     imprimir_fila(fila);
 
     return 0;
 }