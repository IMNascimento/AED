#include <stdio.h>
#define MAXQ 100

int frente = 0, tras = 0;
int fila[MAXQ];

void enqueue(int v) {
    if ((tras + 1) % MAXQ != frente) {
        fila[tras] = v;
        tras = (tras + 1) % MAXQ;
    }
}

int dequeue() {
    if (frente != tras) {
        int v = fila[frente];
        frente = (frente + 1) % MAXQ;
        return v;
    }
    return -1; // vazia
}