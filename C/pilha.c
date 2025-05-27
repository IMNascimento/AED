#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100  // Tamanho máximo da pilha

typedef struct Stack {
    int data[MAX_SIZE];
    int top;
} Stack;

// Inicializa a pilha
void initStack(Stack* s) {
    s->top = -1;
}

// Verifica se a pilha está vazia
int isEmpty(Stack* s) {
    return s->top == -1;
}

// Verifica se a pilha está cheia
int isFull(Stack* s) {
    return s->top == MAX_SIZE - 1;
}

// Insere elemento na pilha (push)
void push(Stack* s, int value) {
    if (isFull(s)) {
        printf("Erro: pilha cheia.\n");
        return;
    }
    s->data[++(s->top)] = value;
}

// Remove elemento da pilha (pop) e retorna valor
int pop(Stack* s) {
    if (isEmpty(s)) {
        printf("Erro: pilha vazia.\n");
        return -1; // valor de erro
    }
    return s->data[(s->top)--];
}

// Retorna elemento do topo sem remover (peek)
int peek(Stack* s) {
    if (isEmpty(s)) {
        printf("Erro: pilha vazia.\n");
        return -1;
    }
    return s->data[s->top];
}

// Exibe a pilha
void display(Stack* s) {
    if (isEmpty(s)) {
        printf("Pilha vazia.\n");
        return;
    }
    printf("Pilha (topo -> base): ");
    for (int i = s->top; i >= 0; i--) {
        printf("%d ", s->data[i]);
    }
    printf("\n");
}

int main() {
    Stack stack;
    initStack(&stack);

    // Operações de teste
    push(&stack, 10);
    push(&stack, 20);
    push(&stack, 30);
    display(&stack);
    printf("Peek: %d\n", peek(&stack));
    printf("Pop: %d\n", pop(&stack));
    display(&stack);
    printf("Is empty? %s\n", isEmpty(&stack) ? "Sim" : "Não");

    // Teste de overflow
    for (int i = 0; i < MAX_SIZE; i++) {
        push(&stack, i);
    }
    // Deve exibir erro quando passar do limite
    push(&stack, 1000);

    return 0;
}