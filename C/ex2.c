// Será possivel criar uma lisrta ligada sem ponteiro
#include <stdio.h>

#define MAX 10

int valores[MAX];
int prox[MAX];

int main() {
    int i, j, n, k, m;
    int cont = 0;

    printf("Digite o tamanho do vetor: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("Digite o valor %d: ", i + 1);
        scanf("%d", &valores[i]);
        prox[i] = -1;
    }

    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++) {
            if (valores[i] == valores[j]) {
                prox[i] = j;
                cont++;
            }
        }
    }

    printf("Valores repetidos:\n");
    for (i = 0; i < n; i++) {
        if (prox[i] != -1) {
            printf("%d ", valores[i]);
            prox[i] = -1;
        }
    }
    printf("\n");

    return 0;
}