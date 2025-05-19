#include <iostream>

struct Node {
    int valor;
    Node* prox;
    Node(int v): valor(v), prox(this) {}
};

class CircularList {
    Node* head;
public:
    CircularList(): head(nullptr) {}
    ~CircularList() { clear(); }

    void insert(int v) {
        Node* novo = new Node(v);
        if (!head) head = novo;
        else {
            Node* temp = head;
            while (temp->prox != head) temp = temp->prox;
            temp->prox = novo;
            novo->prox = head;
        }
    }

    void remove(int v) {
        if (!head) return;
        Node* cur = head;
        Node* prev = nullptr;
        // caso único
        if (head->prox == head && head->valor == v) {
            delete head;
            head = nullptr;
            return;
        }
        do {
            if (cur->valor == v) break;
            prev = cur;
            cur = cur->prox;
        } while (cur != head);
        if (cur->valor != v) return;
        prev->prox = cur->prox;
        if (cur == head) head = cur->prox;
        delete cur;
    }

    void print() const {
        if (!head) { std::cout << "Lista vazia
"; return; }
        Node* temp = head;
        do {
            std::cout << temp->valor << " -> ";
            temp = temp->prox;
        } while (temp != head);
        std::cout << "(retorna ao início)
";
    }

    void clear() {
        while (head) remove(head->valor);
    }
};

int main() {
    CircularList cl;
    cl.insert(10);
    cl.insert(20);
    cl.insert(30);
    cl.print();
    cl.remove(20);
    cl.print();
    return 0;
}