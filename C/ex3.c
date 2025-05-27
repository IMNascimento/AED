// Seja L uma LDE criada para armazenar uma matrizesparsa. Criea estrutura e os metodos de insercao, remocao de um valor
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct no {
    int linha;
    int coluna;
    int valor;
    struct no *proximo;
} No;

typedef struct lista {
    No *inicio;
} Lista;

Lista* criar_lista() {
    Lista *lista = (Lista*)malloc(sizeof(Lista));
    lista->inicio = NULL;
    return lista;
}

void inserir(Lista *lista, int linha, int coluna, int valor) {
    No *novo = (No*)malloc(sizeof(No));
    novo->linha = linha;
    novo->coluna = coluna;
    novo->valor = valor;
    novo->proximo = NULL;

    if (lista->inicio == NULL) {
        lista->inicio = novo;
    } else {
        No *atual = lista->inicio;
        while (atual->proximo != NULL) {
            atual = atual->proximo;
        }
        atual->proximo = novo;
    }
}

void remover(Lista *lista, int linha, int coluna) {
    if (lista->inicio == NULL) {
        printf("Lista vazia.\n");
        return;
    }

    No *atual = lista->inicio;
    No *anterior = NULL;

    while (atual != NULL && (atual->linha != linha || atual->coluna != coluna)) {
        anterior = atual;
        atual = atual->proximo;
    }

    if (atual == NULL) {
        printf("Elemento nao encontrado.\n");
        return;
    }

    if (anterior == NULL) {
        lista->inicio = atual->proximo;
    } else {
        anterior->proximo = atual->proximo;
    }

    free(atual);
}

void imprimir(Lista *lista) {
    No *atual = lista->inicio;
    while (atual != NULL) {
        printf("Linha: %d, Coluna: %d, Valor: %d\n", atual->linha, atual->coluna, atual->valor);
        atual = atual->proximo;
    }
}

void liberar_lista(Lista *lista) {
    No *atual = lista->inicio;
    while (atual != NULL) {
        No *temp = atual;
        atual = atual->proximo;
        free(temp);
    }
    free(lista);
}

int main() {
    Lista *lista = criar_lista();

    inserir(lista, 0, 0, 1);
    inserir(lista, 1, 2, 2);
    inserir(lista, 3, 4, 3);

    printf("Lista antes da remocao:\n");
    imprimir(lista);

    remover(lista, 1, 2);

    printf("Lista apos a remocao:\n");
    imprimir(lista);

    liberar_lista(lista);
    return 0;
}
