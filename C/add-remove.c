#include <stdio.h>
#include <stdlib.h>

// Insere no final (push)
void inserir(int **vet, int *n, int valor) {
    *vet = realloc(*vet, (*n + 1) * sizeof(int));
    (*vet)[*n] = valor;
    (*n)++;
}

// Remove último (pop)
int remover(int *vet, int *n) {
    if (*n == 0) return -1; // vazio
    int valor = vet[*n - 1];
    *n -= 1;
    return valor;
}

int main() {
    int *vet = NULL;
    int n = 0;

    inserir(&vet, &n, 10);
    inserir(&vet, &n, 20);
    printf("Removido: %d\n", remover(vet, &n));

    free(vet);
    return 0;
}