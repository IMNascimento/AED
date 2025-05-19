#include <iostream>
#include <queue>

int main() {
    std::queue<int> q;
    q.push(1);
    q.push(2);
    std::cout << "Front: " << q.front() << "\n";
    q.pop();
    std::cout << "Tamanho: " << q.size() << "\n";
    return 0;
}