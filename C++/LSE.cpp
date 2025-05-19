#include <iostream>
#include <forward_list>

int main() {
    std::forward_list<int> lst;
    // Inserir no início
    lst.push_front(10);
    lst.push_front(20);
    // Remover do início
    int v = lst.front();
    lst.pop_front();
    std::cout << "Removido: " << v << "\n";
    return 0;
}