#include <stdio.h>

// Busca sequencial em vetor (lista linear estática)
int busca(int *vet, int n, int chave) {
    // Percorre do índice 0 até n-1
    for (int i = 0; i < n; i++) {
        if (vet[i] == chave) {
            return i; // Encontrou: retorna posição
        }
    }
    return -1; // Não encontrou
}

int main() {
    int vet[] = { 10, 20, 30, 40, 50 };
    int pos = busca(vet, 5, 30);
    if (pos != -1)
        printf("Encontrado na posição %d\n", pos);
    else
        printf("Não encontrado\n");
    return 0;
}