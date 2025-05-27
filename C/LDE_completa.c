#include <stdio.h>
#include <stdlib.h>

// Estrutura do nó da lista duplamente encadeada
typedef struct Node {
    int data;
    struct Node* prev;
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
    newNode->prev = newNode->next = NULL;
    return newNode;
}

// Insere no início da lista
void insertAtBeginning(Node** head, int data) {
    Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        newNode->next = *head;
        (*head)->prev = newNode;
        *head = newNode;
    }
}

// Insere no fim da lista
void insertAtEnd(Node** head, int data) {
    Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        Node* temp = *head;
        while (temp->next) temp = temp->next;
        temp->next = newNode;
        newNode->prev = temp;
    }
}

// Insere após um nó que contenha key
void insertAfter(Node* head, int key, int data) {
    Node* temp = head;
    while (temp && temp->data != key)
        temp = temp->next;

    if (!temp) {
        printf("Chave %d não encontrada.\n", key);
        return;
    }
    Node* newNode = createNode(data);
    newNode->next = temp->next;
    newNode->prev = temp;
    if (temp->next)
        temp->next->prev = newNode;
    temp->next = newNode;
}

// Remove nó com valor key
void deleteNode(Node** head, int key) {
    Node* temp = *head;
    while (temp && temp->data != key)
        temp = temp->next;

    if (!temp) {
        printf("Valor %d não encontrado.\n", key);
        return;
    }
    if (temp->prev)
        temp->prev->next = temp->next;
    else
        *head = temp->next;

    if (temp->next)
        temp->next->prev = temp->prev;

    free(temp);
}

// Busca pelo valor key; retorna ponteiro ou NULL
Node* search(Node* head, int key) {
    Node* temp = head;
    while (temp) {
        if (temp->data == key)
            return temp;
        temp = temp->next;
    }
    return NULL;
}

// Exibe lista do início ao fim
void displayForward(Node* head) {
    printf("Lista (forward): ");
    Node* temp = head;
    while (temp) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

// Exibe lista do fim ao início
void displayBackward(Node* head) {
    if (!head) return;
    Node* temp = head;
    while (temp->next)
        temp = temp->next;

    printf("Lista (backward): ");
    while (temp) {
        printf("%d ", temp->data);
        temp = temp->prev;
    }
    printf("\n");
}

// Conta nós da lista
int countNodes(Node* head) {
    int count = 0;
    Node* temp = head;
    while (temp) {
        count++;
        temp = temp->next;
    }
    return count;
}

// Libera toda a lista
void freeList(Node** head) {
    Node* temp = *head;
    while (temp) {
        Node* next = temp->next;
        free(temp);
        temp = next;
    }
    *head = NULL;
}

int main() {
    Node* head = NULL;

    // Inserções
    insertAtBeginning(&head, 10);
    insertAtBeginning(&head, 20);
    insertAtEnd(&head, 5);
    insertAfter(head, 10, 15);
    displayForward(head);
    displayBackward(head);

    // Busca
    int key = 15;
    Node* found = search(head, key);
    if (found)
        printf("Encontrado nó com valor %d\n", found->data);
    else
        printf("Valor %d não encontrado na lista\n", key);

    // Contagem
    printf("Número de nós: %d\n", countNodes(head));

    // Remoções
    deleteNode(&head, 20);
    deleteNode(&head, 5);
    displayForward(head);

    // Libera lista
    freeList(&head);
    if (!head)
        printf("Lista liberada com sucesso.\n");

    return 0;
}
