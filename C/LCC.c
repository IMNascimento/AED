#include <stdio.h>
#include <stdlib.h>

// Estrutura do nó da lista circular simples
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// Cria um novo nó com o valor informado
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (!newNode) {
        printf("Erro ao alocar memória.\n");
        exit(EXIT_FAILURE);
    }
    newNode->data = data;
    newNode->next = newNode; // Aponta para si mesmo
    return newNode;
}

// Insere no início da lista
void insertAtBeginning(Node** head, int data) {
    Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        Node* tail = *head;
        while (tail->next != *head)
            tail = tail->next;
        newNode->next = *head;
        tail->next = newNode;
        *head = newNode;
    }
}

// Insere no fim da lista
void insertAtEnd(Node** head, int data) {
    Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        Node* tail = *head;
        while (tail->next != *head)
            tail = tail->next;
        tail->next = newNode;
        newNode->next = *head;
    }
}

// Insere após um nó que contenha key
void insertAfter(Node* head, int key, int data) {
    if (head == NULL) {
        printf("Lista vazia.\n");
        return;
    }
    Node* curr = head;
    do {
        if (curr->data == key) {
            Node* newNode = createNode(data);
            newNode->next = curr->next;
            curr->next = newNode;
            return;
        }
        curr = curr->next;
    } while (curr != head);
    printf("Chave %d não encontrada.\n", key);
}

// Remove nó com valor key
void deleteNode(Node** head, int key) {
    if (*head == NULL) {
        printf("Lista vazia.\n");
        return;
    }
    Node *curr = *head, *prev = NULL;
    // Procura nó a remover
    do {
        if (curr->data == key)
            break;
        prev = curr;
        curr = curr->next;
    } while (curr != *head);

    if (curr->data != key) {
        printf("Valor %d não encontrado.\n", key);
        return;
    }
    // Único nó
    if (curr->next == curr) {
        free(curr);
        *head = NULL;
        return;
    }
    // Removendo head
    if (curr == *head) {
        Node* tail = *head;
        while (tail->next != *head)
            tail = tail->next;
        *head = curr->next;
        tail->next = *head;
        free(curr);
    } else {
        prev->next = curr->next;
        free(curr);
    }
}

// Busca pelo valor key; retorna ponteiro ou NULL
Node* search(Node* head, int key) {
    if (head == NULL) return NULL;
    Node* curr = head;
    do {
        if (curr->data == key)
            return curr;
        curr = curr->next;
    } while (curr != head);
    return NULL;
}

// Exibe lista a partir da cabeça
void display(Node* head) {
    if (head == NULL) {
        printf("Lista vazia.\n");
        return;
    }
    printf("Lista circular: ");
    Node* curr = head;
    do {
        printf("%d ", curr->data);
        curr = curr->next;
    } while (curr != head);
    printf("\n");
}

// Conta nós da lista
int countNodes(Node* head) {
    if (head == NULL) return 0;
    int count = 0;
    Node* curr = head;
    do {
        count++;
        curr = curr->next;
    } while (curr != head);
    return count;
}

// Libera toda a lista
void freeList(Node** head) {
    if (*head == NULL) return;
    Node* curr = (*head)->next;
    while (curr != *head) {
        Node* next = curr->next;
        free(curr);
        curr = next;
    }
    free(*head);
    *head = NULL;
}

int main() {
    Node* head = NULL;

    // Testes de inserção
    insertAtEnd(&head, 10);
    insertAtBeginning(&head, 20);
    insertAtEnd(&head, 30);
    insertAfter(head, 10, 25);
    display(head);

    // Busca
    int key = 25;
    Node* found = search(head, key);
    if (found)
        printf("Encontrado: %d\n", found->data);
    else
        printf("%d não encontrado.\n", key);

    // Contagem
    printf("Total de nós: %d\n", countNodes(head));

    // Remoções
    deleteNode(&head, 20);
    deleteNode(&head, 30);
    display(head);

    // Libera lista
    freeList(&head);
    if (!head)
        printf("Lista liberada.\n");

    return 0;
}