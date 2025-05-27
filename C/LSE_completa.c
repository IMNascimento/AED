#include <stdio.h>
#include <stdlib.h>

// Estrutura do nó da lista encadeada simples
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
    newNode->next = NULL;
    return newNode;
}

// Insere no início da lista
void insertAtBeginning(Node** head, int data) {
    Node* newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

// Insere no fim da lista
void insertAtEnd(Node** head, int data) {
    Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        Node* temp = *head;
        while (temp->next)
            temp = temp->next;
        temp->next = newNode;
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
    temp->next = newNode;
}

// Remove nó com valor key
void deleteNode(Node** head, int key) {
    Node* temp = *head;
    Node* prev = NULL;

    // Busca nó a ser removido
    while (temp && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    if (!temp) {
        printf("Valor %d não encontrado.\n", key);
        return;
    }

    // Ajusta ponteiros
    if (prev)
        prev->next = temp->next;
    else
        *head = temp->next;

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
void display(Node* head) {
    printf("Lista: ");
    Node* temp = head;
    while (temp) {
        printf("%d ", temp->data);
        temp = temp->next;
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
    insertAtBeginning(&head, 30);
    insertAtBeginning(&head, 40);
    insertAtEnd(&head, 20);
    insertAfter(head, 30, 35);
    display(head);

    // Busca
    int key = 35;
    Node* found = search(head, key);
    if (found)
        printf("Encontrado nó com valor %d\n", found->data);
    else
        printf("Valor %d não encontrado na lista\n", key);

    // Contagem
    printf("Número de nós: %d\n", countNodes(head));

    // Remoções
    deleteNode(&head, 40);
    deleteNode(&head, 20);
    display(head);

    // Libera lista
    freeList(&head);
    if (!head)
        printf("Lista liberada com sucesso.\n");

    return 0;
}
