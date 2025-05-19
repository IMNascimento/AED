#include <stdio.h>
#define MAX 100

int topo = 0;
int pilha[MAX];

void push(int v) {
    if (topo < MAX)
        pilha[topo++] = v;
}

int pop() {
    if (topo > 0)
        return pilha[--topo];
    return -1; // vazia
}

int main() {
    push(1);
    push(2);
    printf("Pop: %d\n", pop());
    return 0;
}